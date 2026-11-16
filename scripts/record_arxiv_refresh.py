#!/usr/bin/env python3
"""Record verified source refreshes against an immutable Git baseline.

The conference argument to build_receipt is a (baseline, current) pair. The
CLI additionally compares the conference source bytes, so an arXiv-only
receipt cannot hide a conference refresh or even an unrelated source edit.
An explicit --allow-conference-refresh opt-in records both source layers.
Historical receipts are immutable: rerunning an identical build is allowed,
but neither output may overwrite different existing content.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

from freshness import title_key

ROOT = Path(__file__).resolve().parents[1]
ARXIV_SOURCE = "data/arxiv_recent.json"
CONFERENCE_SOURCE = "data/papers.json"


def iso_day(value: str) -> str:
    if date.fromisoformat(value).isoformat() != value:
        raise ValueError("snapshot date must use ISO YYYY-MM-DD")
    return value


def canonical_hash(value: dict) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate_snapshot(payload: dict, *, require_verified: bool) -> None:
    source = payload["source"]
    records = payload["papers"]
    candidate_count = source["candidate_records"]
    if type(candidate_count) is not int or candidate_count < len(records):
        raise ValueError("invalid arXiv candidate count")
    if source.get("classified_records") != len(records):
        raise ValueError("arXiv admitted count does not match records")
    if source.get("unclassified_records") != candidate_count - len(records):
        raise ValueError("arXiv unclassified count is inconsistent")
    if require_verified and source.get("candidate_coverage_verified") is not True:
        raise ValueError("API candidate coverage must be verified before recording a refresh")
    if source.get("candidate_coverage_verified") is True:
        declared = source.get("api_declared_candidate_records")
        if type(declared) is not int or declared != candidate_count:
            raise ValueError("observed candidates differ from API-declared count")
    start, end = (iso_day(payload["window"][key]) for key in ("start", "end"))
    if start > end or payload["as_of"] != end or source.get("snapshot_date") != end:
        raise ValueError("arXiv snapshot and window dates are inconsistent")
    seen = set()
    for paper in records:
        if paper["arxiv_id"] in seen:
            raise ValueError("duplicate arXiv ID in snapshot")
        seen.add(paper["arxiv_id"])
        if not start <= iso_day(paper["published"]) <= end:
            raise ValueError("arXiv publication date is outside its snapshot window")


def record_summary(paper: dict, classification_source: str) -> dict:
    return {
        "id": paper["arxiv_id"],
        "title": paper["title"],
        "published": paper["published"],
        "paper_url": paper["paper_url"],
        "track": paper["track"],
        "subcategory": paper["subcategory"],
        "specialty": paper["specialty"],
        "classification_status": paper.get("classification_status", "unknown"),
        "classification_source": classification_source,
    }


def snapshot_counts(payload: dict, conference: dict) -> dict:
    papers = payload["papers"]
    source = payload["source"]
    conference_titles = {title_key(p["title"]) for p in conference["papers"]}
    titles = [title_key(p["title"]) for p in papers]
    unique_titles = set(titles)
    return {
        "candidate_records": source["candidate_records"],
        "api_declared_candidate_records": source.get("api_declared_candidate_records"),
        "candidate_coverage_verified": source.get("candidate_coverage_verified", False),
        "classified_records": len(papers),
        "unclassified_records": source["unclassified_records"],
        "conference_title_duplicates": sum(title in conference_titles for title in titles),
        "conference_unique_title_overlap": len(conference_titles & unique_titles),
        "arxiv_normalized_title_duplicates": len(titles) - len(unique_titles),
        "combined_unique_records": len(conference_titles | unique_titles),
        "latest_published": max((p["published"] for p in papers), default=None),
    }


def conference_records(payload: dict) -> dict[str, dict]:
    """Index source IDs, or stable bibliographic keys; URLs are not identities."""
    records = {}
    for paper in payload["papers"]:
        if type(paper["year"]) is not int:
            raise ValueError("conference record requires an integer year")
        field = next((field for field in ("id", "paper_id", "paperId")
                      if paper.get(field) is not None), None)
        if field:
            value = paper[field]
            if isinstance(value, bool) or not isinstance(value, (str, int)) or not str(value).strip():
                raise ValueError("conference source ID must be nonempty text or an integer")
            identifier, strategy = f"{field}:{value}", f"source:{field}"
        else:
            key = {"title": title_key(paper["title"]), "venue": paper["venue"]}
            if not key["title"] or not key["venue"]:
                raise ValueError("conference bibliographic identity requires title and venue")
            identifier = "bibliographic:" + canonical_hash(key)
            strategy = "normalized_title+venue"
        if identifier in records:
            raise ValueError(f"duplicate conference identity: {identifier}")
        records[identifier] = {"paper": paper, "identity_strategy": strategy}
    return records


def conference_summary(identifier: str, entry: dict) -> dict:
    paper = entry["paper"]
    return {"id": identifier, "identity_strategy": entry["identity_strategy"],
            **{field: paper[field] for field in ("title", "year", "venue", "paper_url", "official_url")}}


def conference_refresh(before: dict, after: dict, snapshot_date: str) -> dict:
    if iso_day(after["as_of"]) != snapshot_date:
        raise ValueError("conference refresh date must match this snapshot")
    if after.get("census", {}).get("snapshot_date") != snapshot_date:
        raise ValueError("conference census date must match this snapshot")
    if iso_day(before["as_of"]) > after["as_of"]:
        raise ValueError("a refresh cannot move the conference snapshot backwards")
    for payload in (before, after):
        if payload.get("census", {}).get("snapshot_date", payload["as_of"]) != payload["as_of"]:
            raise ValueError("conference census and snapshot dates are inconsistent")
    old, new = conference_records(before), conference_records(after)
    changed = sorted(key for key in old.keys() & new.keys() if old[key]["paper"] != new[key]["paper"])
    return {
        "snapshot_before": before["as_of"], "snapshot_after": after["as_of"],
        "window_before": before.get("window"), "window_after": after.get("window"),
        "records_before": len(old), "records_after": len(new),
        "source_unchanged": before == after,
        "source_before_sha256": canonical_hash(before), "source_after_sha256": canonical_hash(after),
        "identity_strategy": "source ID when available; otherwise normalized_title+venue (SHA-256 bibliographic key) in this title-deduplicated catalog; year and URLs are mutable metadata; title matching is not full-paper version verification",
        "added": [conference_summary(key, new[key]) for key in sorted(new.keys() - old.keys())],
        "removed": [conference_summary(key, old[key]) for key in sorted(old.keys() - new.keys())],
        "retained_records": len(old.keys() & new.keys()),
        "retained_metadata_changes": len(changed),
        "retained_metadata_change_ids": changed,
        "retained_metadata_changed_records": [conference_summary(key, new[key]) for key in changed],
    }


def build_receipt(before: dict, after: dict, conference: tuple[dict, dict],
                  baseline: str, snapshot_date: str, admission_review: dict | None = None,
                  *, allow_conference_refresh: bool = False) -> dict:
    """Build deterministic evidence without reading files or mutating inputs."""
    iso_day(snapshot_date)
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", baseline):
        raise ValueError("baseline must be a resolved Git commit SHA")
    before_conference, after_conference = conference
    if not allow_conference_refresh and before_conference != after_conference:
        raise ValueError("conference source changed; this receipt is arXiv-only")
    conference_evidence = (conference_refresh(before_conference, after_conference, snapshot_date)
                           if allow_conference_refresh else {
        "snapshot_before": before_conference["as_of"],
        "snapshot_after": after_conference["as_of"],
        "records_before": len(before_conference["papers"]),
        "records_after": len(after_conference["papers"]),
        "source_unchanged": True,
        "source_sha256": canonical_hash(after_conference),
    })
    validate_snapshot(before, require_verified=False)
    validate_snapshot(after, require_verified=True)
    if snapshot_date != after["as_of"]:
        raise ValueError("receipt date must match the new arXiv snapshot date")
    if after["as_of"] < before["as_of"]:
        raise ValueError("a refresh cannot move the arXiv snapshot backwards")
    old = {p["arxiv_id"]: p for p in before["papers"]}
    new = {p["arxiv_id"]: p for p in after["papers"]}
    added = [record_summary(new[key], "refreshed_snapshot") for key in sorted(new.keys() - old.keys())]
    removed = []
    start, end = after["window"]["start"], after["window"]["end"]
    for key in sorted(old.keys() - new.keys()):
        paper = old[key]
        summary = record_summary(paper, "baseline_last_observed")
        summary["reason"] = ("outside_new_window" if not start <= paper["published"] <= end
                             else "missing_within_new_window")
        removed.append(summary)
    reviewed = {}
    if admission_review is not None:
        if (admission_review.get("snapshot_date") != snapshot_date
                or admission_review.get("checked_on") != snapshot_date):
            raise ValueError("admission review date must match this snapshot")
        missing_ids = {p["id"] for p in removed if p["reason"] == "missing_within_new_window"}
        for review in admission_review.get("records", []):
            identifier = review["id"]
            if identifier not in missing_ids or identifier in reviewed:
                raise ValueError("admission review must identify unique in-window missing records")
            if (review.get("cs_ro_present") is not True
                    or "current_admission_result" not in review
                    or review["current_admission_result"] is not None
                    or not review.get("reason")
                    or review.get("paper_url") != f"https://arxiv.org/abs/{identifier}"):
                raise ValueError("admission review lacks source/category/non-admission evidence")
            reviewed[identifier] = review
        for summary in removed:
            if summary["id"] in reviewed:
                summary["admission_review"] = reviewed[summary["id"]]
        if "conference_records" in admission_review:
            if not allow_conference_refresh:
                raise ValueError("conference admission review requires explicit conference refresh")
            conference_reviews = admission_review["conference_records"]
            if not isinstance(conference_reviews, list):
                raise ValueError("conference admission review must be an array")
            verified_conference = {}
            for review in conference_reviews:
                if (not isinstance(review, dict) or not isinstance(review.get("title"), str)
                        or not isinstance(review.get("venue"), str)
                        or type(review.get("year")) is not int
                        or "current_admission_result" not in review
                        or review["current_admission_result"] is not None
                        or not isinstance(review.get("reason"), str) or not review["reason"].strip()):
                    raise ValueError("conference admission review lacks identity/non-admission evidence")
                key = (title_key(review["title"]), review["venue"])
                matches = [p for p in conference_evidence["removed"]
                           if (title_key(p["title"]), p["venue"]) == key]
                if len(matches) != 1 or key in verified_conference:
                    raise ValueError("conference admission review must identify unique removed records")
                if (review["year"] != matches[0]["year"]
                        or review.get("official_url") != matches[0]["official_url"]):
                    raise ValueError("conference admission review lacks matching year/source evidence")
                verified_conference[key] = review
            conference_evidence["removal_admission_review"] = [verified_conference[key] for key in sorted(verified_conference)]
    changed_ids = sorted(key for key in old.keys() & new.keys() if old[key] != new[key])
    counts_before = snapshot_counts(before, before_conference)
    counts_after = snapshot_counts(after, after_conference)
    for payload, counts in ((before, counts_before), (after, counts_after)):
        for field in ("conference_title_duplicates", "conference_unique_title_overlap",
                      "arxiv_normalized_title_duplicates", "combined_unique_records"):
            if field in payload["source"] and payload["source"][field] != counts[field]:
                raise ValueError(f"arXiv {field} ledger is inconsistent")
    return {
        "schema_version": 1,
        "date": snapshot_date,
        "timezone": "Asia/Hong_Kong",
        "baseline_commit": baseline,
        "source_refresh": True,
        "refresh_scope": "conference-and-arxiv" if allow_conference_refresh else "arxiv-only",
        "layers": {
            "papers.json": conference_evidence,
            "arxiv_recent.json": {
                "snapshot_before": before["as_of"],
                "snapshot_after": after["as_of"],
                "window_before": before["window"],
                "window_after": after["window"],
                "source_before_sha256": canonical_hash(before),
                "source_after_sha256": canonical_hash(after),
                "records_before": len(old),
                "records_after": len(new),
                "counts_before": counts_before,
                "counts_after": counts_after,
                "added": added,
                "added_published_after_previous_snapshot": sum(p["published"] > before["as_of"] for p in added),
                "added_published_on_or_before_previous_snapshot": sum(p["published"] <= before["as_of"] for p in added),
                "added_publication_date_counts": dict(sorted(Counter(p["published"] for p in added).items())),
                "title_abstract_reviewed_added_ids": [p["id"] for p in added if p["classification_status"] == "reviewed"],
                "removed": removed,
                "removed_outside_new_window": sum(p["reason"] == "outside_new_window" for p in removed),
                "missing_within_new_window": sum(p["reason"] == "missing_within_new_window" for p in removed),
                "verified_no_longer_admitted": len(reviewed),
                "unresolved_in_window_absences": sum(p["reason"] == "missing_within_new_window" for p in removed) - len(reviewed),
                "retained_records": len(old.keys() & new.keys()),
                "retained_metadata_changes": len(changed_ids),
                "retained_metadata_change_ids": changed_ids,
                "taxonomy_version": after.get("taxonomy", {}).get("version"),
                "classification_status_counts": dict(sorted(Counter(
                    p.get("classification_status", "unknown") for p in after["papers"]
                ).items())),
            },
        },
        "limitations": [
            ("Conference scope is the declared source window and venue/admission rules; the arXiv layer covers only cs.RO including cross-listings and its rolling three-year submitted-date window."
             if allow_conference_refresh else
             "Only cs.RO including cross-listings and the declared rolling three-year submitted-date window are covered."),
            "Candidate reconciliation verifies counts, not perfect admission rules or semantic classification.",
            "In-window absences are unresolved unless accompanied by an explicit source/admission review; absence is not evidence of withdrawal.",
            "Removed records show their last observed baseline classification, not a newly verified current classification.",
            "Taxonomy and title/abstract review are not evidence that every paper has been manually read in full or reproduced.",
        ],
        "publication_status": "Receipt preparation does not merge PR #1 or publish the main branch/site; verify GitHub status separately.",
    }


def cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_receipt(receipt: dict) -> str:
    arxiv = receipt["layers"]["arxiv_recent.json"]
    conference = receipt["layers"]["papers.json"]
    before, after = arxiv["counts_before"], arxiv["counts_after"]
    dual = receipt.get("refresh_scope") == "conference-and-arxiv"
    title = "顶会与 arXiv 来源刷新记录" if dual else "arXiv 来源刷新记录"
    scope = "本次分别刷新顶会索引与 arXiv 两个来源层" if dual else "本次只刷新 arXiv"
    conference_change = (
        f"- 顶会来源快照由 {conference['snapshot_before']} 更新为 {conference['snapshot_after']}；"
        f"记录由 {conference['records_before']:,} 变为 {conference['records_after']:,}，"
        f"新增 {len(conference['added']):,}、移出 {len(conference['removed']):,}，"
        f"保留记录元数据变化 {conference['retained_metadata_changes']:,} 条。"
        if dual else
        f"- 顶会来源内容保持不变：{conference['records_after']:,} 条，实际快照仍为 {conference['snapshot_after']}。"
    )
    lines = [
        f"# {title} · {receipt['date']}", "",
        f"基准提交：`{receipt['baseline_commit']}`。{scope}，不通过改日期制造更新或完整性证明。",
        "", "| 指标 | 刷新前 | 刷新后 |", "|---|---:|---:|",
        f"| arXiv 快照 | {arxiv['snapshot_before']} | {arxiv['snapshot_after']} |",
        f"| 原始提交日期窗口（含首尾） | {arxiv['window_before']['start']} 至 {arxiv['window_before']['end']} | {arxiv['window_after']['start']} 至 {arxiv['window_after']['end']} |",
    ]
    if dual:
        lines.extend([
            f"| 顶会索引快照（非论文发表日期） | {conference['snapshot_before']} | {conference['snapshot_after']} |",
            f"| 顶会来源记录 | {conference['records_before']:,} | {conference['records_after']:,} |",
        ])
    for field, label in (
        ("candidate_records", "实际候选"),
        ("api_declared_candidate_records", "API 声明候选"),
        ("classified_records", "规则纳入"),
        ("unclassified_records", "未满足纳入规则"),
        ("conference_title_duplicates", "与顶会标题重合的预印本记录"),
        ("conference_unique_title_overlap", "与顶会重合的唯一标题"),
        ("arxiv_normalized_title_duplicates", "arXiv 内部标准化标题重复"),
        ("combined_unique_records", "合并标题去重阅读记录"),
        ("latest_published", "最新已纳入原始发表日期"),
    ):
        lines.append(f"| {label} | {before[field] if before[field] is not None else '未记录'} | {after[field] if after[field] is not None else '未记录'} |")
    lines.extend([
        "", "## 实际变化与数量核对", "",
        f"- API 数量校验：刷新后实际 {after['candidate_records']:,} 条，与 API 声明 {after['api_declared_candidate_records']:,} 条一致。",
        f"- 新增 {len(arxiv['added']):,} 条，移出 {len(arxiv['removed']):,} 条；其中滚动窗口移出 {arxiv['removed_outside_new_window']:,} 条，仍在新窗口但本次未出现 {arxiv['missing_within_new_window']:,} 条。",
        f"- 新增收录中，{arxiv['added_published_after_previous_snapshot']:,} 条原始发表于旧快照之后；{arxiv['added_published_on_or_before_previous_snapshot']:,} 条原始发表于旧快照截止日或更早。新增收录不等于全部是本周新发表。",
        f"- 保留 {arxiv['retained_records']:,} 条；完整记录字段发生变化的保留记录 {arxiv['retained_metadata_changes']:,} 条。数量变化不是新增数量，元数据变化也不等于新论文。",
        conference_change,
        f"- 窗口内未收录中，{arxiv['verified_no_longer_admitted']} 条已核对为来源元数据修订后不再满足现有纳入规则；{arxiv['unresolved_in_window_absences']} 条原因待核实。窗口移出不表示撤稿，规则排除也不证明论文无关。",
        "", "## arXiv 新增与移出明细" if dual else "## 新增与移出明细", "",
        "新增使用刷新后当前三级分类；移出展示基准中最后已观察分类，不冒充本次重新核实。",
    ])
    for name, records in (("新增", arxiv["added"]), ("移出", arxiv["removed"])):
        lines.extend(["", f"### {name}（{len(records):,} 条）", ""])
        if not records:
            lines.append("无。")
            continue
        lines.extend(["| arXiv ID | 论文 | 原始发表日期 | 一级 → 二级 → 三级 | 分类状态 | 变化原因 |",
                      "|---|---|---|---|---|---|"])
        for paper in records:
            reason = {"outside_new_window": "滚动窗口外", "missing_within_new_window": "窗口内未出现，原因未确认"}.get(paper.get("reason"), "本次新增纳入")
            if paper.get("admission_review"):
                reason = "元数据修订后未满足现有纳入规则（非已确认撤稿）"
            path = " → ".join(cell(paper[key]) for key in ("track", "subcategory", "specialty"))
            lines.append(f"| {cell(paper['id'])} | [{cell(paper['title'])}]({paper['paper_url']}) | {paper['published']} | {path} | {cell(paper['classification_status'])} | {reason} |")
    if dual:
        lines.extend([
            "", "## 顶会来源变化", "",
            f"- 索引年份范围：刷新前 {conference['window_before']}，刷新后 {conference['window_after']}；具体检索会议和纳入边界以来源数据及覆盖报告为准。",
            "- 本仓库来源目录已经按标题去重；身份匹配优先使用来源 ID，否则使用标准化标题与 venue 的确定性书目键。year 和 URL 是可更新元数据，纠正年份或换链接不是新增论文；同题匹配不是全文版本认证。",
            "- 以下 year、venue、阅读及来源链接均保留索引原值；本次新增收录不表示新近发表或录用，移出也不表示撤稿。保留记录明细展示刷新后元数据。",
        ])
        for label, records in (("新增", conference["added"]), ("移出", conference["removed"]),
                               ("保留记录的元数据变化", conference["retained_metadata_changed_records"])):
            lines.extend(["", f"### 顶会{label}（{len(records):,} 条）", ""])
            displayed = records
            if label == "保留记录的元数据变化":
                displayed = records[:20]
                omitted = f"；其余 {len(records) - 20:,} 条已截断" if len(records) > 20 else "；未截断"
                lines.extend([f"本节共 {len(records):,} 条，当前展示前 {len(displayed)} 条{omitted}。完整明细保留在[同日 JSON 收据](../data/catalog-refresh-{receipt['date']}.json)。", ""])
            if not records:
                lines.append("无。")
                continue
            lines.extend(["| 记录 ID | 标题 | year | venue | 来源链接 | 身份策略 |",
                          "|---|---|---:|---|---|---|"])
            for paper in displayed:
                lines.append(f"| {cell(paper['id'])} | [{cell(paper['title'])}]({paper['paper_url']}) | {paper['year']} | {cell(paper['venue'])} | [来源]({paper['official_url']}) | {cell(paper['identity_strategy'])} |")
        if conference.get("removal_admission_review"):
            lines.extend(["", "### 顶会移出记录的来源复核", "",
                          "以下依据输入的来源核验理由记录：摘要补全后不满足现有纳入条件（触发现有排除规则），非撤稿；不把规则排除等同于论文无关。", ""])
            for review in conference["removal_admission_review"]:
                lines.append(f"- [{cell(review['title'])}]({review['official_url']}) · {cell(review['venue'])} {review['year']} · {cell(review['reason'])}")
    if arxiv["verified_no_longer_admitted"]:
        lines.extend(["", "### 窗口内未收录的来源复核", "",
                      "以下记录仍含 cs.RO 分类，官方 API 按 ID 复核后，当前标题/摘要的纳入函数均返回空结果。不是类别移出或已确认撤稿；现有词表可能漏掉相关工作。", ""])
        for paper in arxiv["removed"]:
            review = paper.get("admission_review")
            if review:
                lines.append(f"- [{paper['id']}]({review['paper_url']}) · 官方元数据修订 {review['updated_on']} · {review['reason']}")
    lines.extend([
        "", "## 分类、覆盖与发布边界", "",
        f"- 现有分类版本：{arxiv['taxonomy_version']}；刷新后状态计数：{arxiv['classification_status_counts']}。",
        f"- 新增收录中有 {len(arxiv['title_abstract_reviewed_added_ids'])} 条使用标题/摘要审核例外；其 arXiv ID 为 {arxiv['title_abstract_reviewed_added_ids']}。这些例外不代表全文精读或实验认证。",
        "- 检索范围仅为 cs.RO（含交叉分类）与声明的滚动三年窗口；未纳入不证明论文不相关，不宣称“全网最全”。",
        "- API 候选数量一致只说明数量核对通过，不能证明纳入规则、分页身份或语义分类完美。",
        "- 使用现有分类与标题/摘要审核例外，不代表每篇已经人工全文精读或完成实验复现。",
        "- 论文原始发表日期、既有分析审核日期和历史收据保留；当前文档同步不等于正文重新精读。",
        "- 本收据的生成不会合并 PR #1，也不会发布主分支或公开网站；PR 未合并期间这些内容仍仅在更新分支上，远端状态需另行核验。",
        "", f"[机器可读刷新收据](../data/catalog-refresh-{receipt['date']}.json) · [日期与覆盖报告](coverage-report.md) · [分类图谱](../papers/taxonomy/README.md)", "",
    ])
    return "\n".join(lines)


def save_outputs(outputs: dict[Path, str], *, check: bool = False) -> None:
    """Preflight every target before writing; never alter a conflicting receipt."""
    for path, content in outputs.items():
        if path.exists():
            if path.read_text(encoding="utf-8") != content:
                raise ValueError(f"immutable receipt differs: {path}")
        elif check:
            raise ValueError(f"receipt is missing: {path}")
    if not check:
        for path, content in outputs.items():
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="immutable baseline Git commit/ref")
    parser.add_argument("--date", required=True, help="snapshot day YYYY-MM-DD")
    parser.add_argument("--check", action="store_true", help="compare saved receipts without writing")
    parser.add_argument("--admission-review", type=Path, help="optional verified in-window absence review JSON")
    parser.add_argument("--allow-conference-refresh", action="store_true",
                        help="explicitly record a separately refreshed conference source alongside arXiv")
    args = parser.parse_args(argv)
    try:
        snapshot_date = iso_day(args.date)
        baseline = subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", f"{args.baseline}^{{commit}}"],
            cwd=ROOT, text=True,
        ).strip()
        before_bytes = subprocess.check_output(["git", "show", f"{baseline}:{ARXIV_SOURCE}"], cwd=ROOT)
        old_conference_bytes = subprocess.check_output(["git", "show", f"{baseline}:{CONFERENCE_SOURCE}"], cwd=ROOT)
        conference_bytes = (ROOT / CONFERENCE_SOURCE).read_bytes()
        if not args.allow_conference_refresh and old_conference_bytes != conference_bytes:
            raise ValueError("conference source bytes changed; this receipt is arXiv-only")
        receipt = build_receipt(
            json.loads(before_bytes), json.loads((ROOT / ARXIV_SOURCE).read_text(encoding="utf-8")),
            (json.loads(old_conference_bytes), json.loads(conference_bytes)), baseline, snapshot_date,
            admission_review=(json.loads(args.admission_review.read_text(encoding="utf-8"))
                              if args.admission_review else None),
            allow_conference_refresh=args.allow_conference_refresh,
        )
        outputs = {
            ROOT / "docs" / f"catalog-refresh-{snapshot_date}.md": render_receipt(receipt),
            ROOT / "data" / f"catalog-refresh-{snapshot_date}.json": json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        }
        save_outputs(outputs, check=args.check)
        arxiv = receipt["layers"]["arxiv_recent.json"]
        print(json.dumps({"date": snapshot_date, "baseline_commit": baseline,
                          "added": len(arxiv["added"]), "removed": len(arxiv["removed"]),
                          "retained_metadata_changes": arxiv["retained_metadata_changes"],
                          "check": args.check}, ensure_ascii=False))
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print(f"Cannot record arXiv refresh: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

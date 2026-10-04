"""Single source for active-document dates and bounded coverage status."""
from collections import Counter
from datetime import date, datetime
from zoneinfo import ZoneInfo
import re

BEGIN = "<!-- catalog-freshness:start -->"
END = "<!-- catalog-freshness:end -->"


def hong_kong_today():
    return datetime.now(ZoneInfo("Asia/Hong_Kong")).date().isoformat()


def title_key(title):
    return re.sub(r"[^a-z0-9]+", " ", title.casefold().replace("π", "pi")).strip()


def build_status(catalog, arxiv, updated_on):
    updated = date.fromisoformat(updated_on)
    for layer in (catalog, arxiv):
        if date.fromisoformat(layer["as_of"]) > updated:
            raise ValueError("document update date cannot precede a source snapshot")
    return {
        "schema_version": 1,
        "documents_updated_on": updated_on,
        "timezone": "Asia/Hong_Kong",
        "conference_snapshot_on": catalog["as_of"],
        "arxiv_snapshot_on": arxiv["as_of"],
        "arxiv_window": arxiv["window"],
        "latest_arxiv_published": max((p["published"] for p in arxiv["papers"]), default=None),
        "conference_records": len(catalog["papers"]),
        "arxiv_records": len(arxiv["papers"]),
        "combined_unique_records": len({title_key(p["title"]) for p in catalog["papers"] + arxiv["papers"]}),
        "arxiv_candidates": arxiv["source"]["candidate_records"],
        "arxiv_outside_admission_rules": arxiv["source"]["unclassified_records"],
        "api_candidate_count_verified": arxiv["source"].get("candidate_coverage_verified", False),
        "api_declared_candidate_records": arxiv["source"].get("api_declared_candidate_records"),
        "conference_source_age_days": (updated - date.fromisoformat(catalog["as_of"])).days,
        "arxiv_source_age_days": (updated - date.fromisoformat(arxiv["as_of"])).days,
        "classification_status_counts": dict(Counter(p["classification_status"] for p in catalog["papers"] + arxiv["papers"])),
        "coverage_claim": "Exhaustive only within the declared retrieval/admission boundary, not all embodied-AI literature.",
        "limitations": [
            "Conference discovery uses ten venue indexes and a robot keyword query; bibliographic indexes may lag and miss papers.",
            "The arXiv layer is limited to cs.RO including cross-listings and the declared rolling three-year window.",
            "Admission/exclusion rules and automatic classification are imperfect; rejected candidates are not proof of irrelevance.",
            "A recent document date is not evidence of a fresh source harvest, full-paper review or experiment reproduction.",
        ],
    }


def stamp_markdown(content, status):
    content = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*", "", content, flags=re.S)
    lines = content.splitlines()
    heading = next((i for i, line in enumerate(lines) if line.startswith("# ")), 0)
    block = (
        f"{BEGIN}\n"
        f"> 文档同步 / Docs synced: **{status['documents_updated_on']}** · "
        f"顶会快照 / Conference: **{status['conference_snapshot_on']}** · "
        f"arXiv 快照: **{status['arxiv_snapshot_on']}** · Asia/Hong_Kong\n"
        f"{END}"
    )
    lines[heading + 1:heading + 1] = ["", block, ""]
    # Idempotent whitespace: one blank before the original body.
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).rstrip() + "\n"


def render_coverage(status, catalog):
    verified = "已核对 API 声明数量 / verified" if status["api_candidate_count_verified"] else "未额外核对 API 声明数量 / not independently reconciled"
    lines = ["# 更新日期与覆盖报告 · Freshness and coverage", "",
             "该报告由实际来源快照生成，不通过改日期制造更新或完整性证明。", "",
             "| 项目 | 当前状态 |", "|---|---|",
             f"| 文档同步日期 | {status['documents_updated_on']} · Asia/Hong_Kong |",
             f"| 顶会来源快照 | {status['conference_snapshot_on']} · {status['conference_records']:,} 条 |",
             f"| arXiv 来源快照 | {status['arxiv_snapshot_on']} · {status['arxiv_records']:,} 条 |",
             f"| arXiv 原始提交日期窗口 | {status['arxiv_window']['start']} 至 {status['arxiv_window']['end']} |",
             f"| 最新已收录 arXiv 原始发表日期 | {status['latest_arxiv_published']} |",
             f"| arXiv 候选核对 | {status['arxiv_candidates']:,} 条；{verified} |",
             f"| 未满足现有纳入规则 | {status['arxiv_outside_admission_rules']:,} 条，不等于这些论文不相关 |",
             f"| 合并标题去重阅读记录 | {status['combined_unique_records']:,} 条，不保证发现所有版本或所有不同标题的同一论文 |",
             "", "## 顶会来源发现范围", "",
             "| 会议 | 索引匹配 | 规则纳入 | 最终收录 |", "|---|---:|---:|---:|"]
    for venue, values in catalog["census"]["venue_discovery"].items():
        lines.append(f"| {venue} | {values['matched_records']:,} | {values['classified_records']:,} | {values['included_records']:,} |")
    lines.extend(["", "## 分类待审状态", "", str(status["classification_status_counts"]), "",
                  "## 完整性边界", "",
                  "- 顶会检索范围是十个会议索引、滚动五年及 robot 关键词，可能漏掉标题/索引不含该关键词的论文；来源索引也可能延迟。",
                  "- arXiv 范围是 cs.RO（含交叉分类）和滚动三年，不覆盖未归入 cs.RO 的相关论文、全部期刊、工作坊、学位论文或未公开研究。",
                  "- 候选数量核对只验证分页收集一致性，不证明纳入词表或语义分类完美。",
                  "- 分页数量核对依据 [arXiv API 的 totalResults 元数据](https://info.arxiv.org/help/api/user-manual.html)，不把接口返回数量等同于全部具身智能论文。",
                  "- 文档同步日期不等于正文重新精读。论文发表日期、已有分析审核日期、历史迁移与刷新记录保留原值。",
                  "- 本项目争取明确范围内的系统覆盖，不宣称“全网最全”或所有记录已人工审阅。",
                  "", "[分类图谱](../papers/taxonomy/README.md) · [分类说明](taxonomy-guide.md) · [数据状态](../data/catalog_status.json)", ""])
    return "\n".join(lines)

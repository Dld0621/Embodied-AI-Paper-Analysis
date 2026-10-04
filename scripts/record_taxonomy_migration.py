"""Record taxonomy-only changes against a specific immutable Git baseline."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ANNOTATIONS = {"track", "subcategory", "specialty", "taxonomy_evidence", "primary_evidence",
               "classification_status", "subcategory_status", "method_tags", "embodiment_tags",
               "data_tags", "related_topics", "related_taxonomy_paths"}


def source_hash(records):
    source = [{key: value for key, value in p.items() if key not in ANNOTATIONS} for p in records]
    encoded = json.dumps(source, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def hand_counts(records):
    primary = [p for p in records if p["subcategory"] == "Dexterous Hand Retargeting"]
    related = [p for p in records if "Hand Retargeting" in p.get("related_topics", [])]
    title_key = lambda p: re.sub(r"[^a-z0-9]+", " ", p["title"].casefold().replace("π", "pi")).strip()
    return {"primary_records": len(primary),
            "unique_primary_titles": len({title_key(p) for p in primary}),
            "related_records": len(related),
            "unique_related_titles": len({title_key(p) for p in related}),
            "specialties": dict(Counter(p["specialty"] for p in primary))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    baseline = subprocess.check_output(["git", "rev-parse", args.baseline], cwd=ROOT, text=True).strip()
    ledger = {"baseline_commit": baseline, "date": args.date, "source_refresh": False, "layers": {}}
    before_all, after_all = [], []
    for filename in ("papers.json", "arxiv_recent.json"):
        before = json.loads(subprocess.check_output(["git", "show", f"{baseline}:data/{filename}"], cwd=ROOT, text=True))
        after = json.loads((ROOT / "data" / filename).read_text())
        old, new = before["papers"], after["papers"]
        assert len(old) == len(new)
        assert source_hash(old) == source_hash(new), "Source records changed; not a taxonomy-only migration"
        ledger["organization_version"] = after["taxonomy"]["version"]
        transfers = Counter((tuple(a[f] for f in ("track", "subcategory", "specialty")),
                             tuple(b[f] for f in ("track", "subcategory", "specialty"))) for a, b in zip(old, new))
        evidence = {
            "records_before": len(old), "records_after": len(new), "source_fields_unchanged": True,
            "source_fields_sha256": source_hash(new),
            "changed_primary_paths": sum(count for (a, b), count in transfers.items() if a != b),
            "changed_related_topics": sum(a["related_topics"] != b["related_topics"] for a, b in zip(old, new)),
            "old_track_counts": dict(Counter(p["track"] for p in old)),
            "new_track_counts": dict(Counter(p["track"] for p in new)),
            "classification_status_counts": dict(Counter(p["classification_status"] for p in new)),
            "provisional_subfield_records": sum(p["subcategory_status"] == "provisional" for p in new),
            "path_transfers": [{"from": list(a), "to": list(b), "records": count} for (a, b), count in sorted(transfers.items())],
        }
        ledger["layers"][filename] = evidence
        before_all.extend(old)
        after_all.extend(new)
    ledger["hand_retargeting_before"] = hand_counts(before_all)
    ledger["hand_retargeting_after"] = hand_counts(after_all)
    destination = ROOT / "data" / f"taxonomy-migration-{args.date}.json"
    destination.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    lines = [f"# 重新分类记录 · {args.date}", "",
             f"基准提交：`{baseline}`。保留既定 9 个一级、42 个二级、126 个具体三级专题和 42 个待审专题。未新增抓取、删除论文或改写来源。",
             "", "## 实际修正", "",
             "- 原来的二级兜底默认为灵巧手重定向，造成大量普通灵巧操作记录误挂及关联标签污染。本次移除这种推断。",
             "- 优先按标题定位二级研究问题，摘要只用于允许的候选内细分。多个背景词不能超过标题中的明确贡献。",
             "- 修正手设计、反馈手套、仿真框架、感知估计、手内操作及抓取的边界；否定标题不支持相应正向分类。",
             "- 二级缺乏支持时标明 provisional（暂定），三级缺乏证据时保留待审，不制造精确分类。",
             "", "## 数量对照", "",
             "| 来源层 | 记录保留 | 主路径改变 | 关联主题改变 | 待审记录 | 二级暂定记录 |",
             "|---|---:|---:|---:|---:|---:|"]
    for name, evidence in ledger["layers"].items():
        lines.append(f"| {name} | {evidence['records_after']:,} | {evidence['changed_primary_paths']:,} | {evidence['changed_related_topics']:,} | {evidence['classification_status_counts'].get('needs-review', 0):,} | {evidence['provisional_subfield_records']:,} |")
    lines.extend(["", "## 灵巧手重定向核对", "",
                  "| 指标 | 修正前 | 修正后 |", "|---|---:|---:|"])
    for key, label in (("primary_records", "主要归属来源记录"), ("unique_primary_titles", "主归属标题去重"),
                       ("related_records", "关联主题来源记录"), ("unique_related_titles", "关联主题标题去重")):
        lines.append(f"| {label} | {ledger['hand_retargeting_before'][key]} | {ledger['hand_retargeting_after'][key]} |")
    lines.extend(["", f"修正后各三级专题的来源记录数量：{ledger['hand_retargeting_after']['specialties']}。", "",
                  "DexMachina、SPIDER、GeoRT、AnyDexRT 的标题/摘要核查例外保持不变。新规则结果仍需语义复核，计数不等于全文精读或实验认证。",
                  "", "## 证据与限制", "",
                  f"[完整路径转移账本](../data/taxonomy-migration-{args.date}.json)记录每条新旧路径的数量和来源字段哈希。记录顺序与所有非分类字段（含标题、作者、日期、链接、摘要、纳入标签）对比一致。",
                  "", "规则归类与待审数量只是处理结果，不保证每篇语义正确。来源快照日期未改变；旧迁移记录作为历史保留。",
                  "", "更新现有 PR #1；未授权合并 main 或发布公开网站。[新版分类图谱](../papers/taxonomy/README.md) · [分类说明](taxonomy-guide.md) · [待审清单](../papers/classification-review/README.md)", ""])
    (ROOT / "docs" / f"taxonomy-migration-{args.date}.md").write_text("\n".join(lines))
    print(json.dumps({name: {key: value for key, value in evidence.items() if key not in {"path_transfers", "old_track_counts", "new_track_counts"}} for name, evidence in ledger["layers"].items()}))
    print(json.dumps(ledger["hand_retargeting_after"]))


if __name__ == "__main__":
    main()

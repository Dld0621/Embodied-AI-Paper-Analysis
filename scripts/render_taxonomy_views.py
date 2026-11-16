"""Supplementary cross-topic and review views; never primary leaf attachments."""
from collections import Counter
from urllib.parse import urlencode
import re


def render_views(root, catalog, arxiv):
    outputs = {}
    layers = {"conference": catalog["papers"], "arxiv": arxiv["papers"]}
    review_dir = root / "papers" / "classification-review"
    lines = ["# Classification review queue · 分类待审清单", "",
             "[Classification guide](../../docs/taxonomy-guide.md) · [Taxonomy](../taxonomy/README.md)", "",
             "Rule assignments are suggestions, not full-paper reviews. Pending lists preserve provisional paths and their evidence.",
             "规则归类不等于全文精读。待审清单保留暂定路径和判定依据；不确定的二级位置也需要复核。", ""]
    for layer, papers in layers.items():
        statuses = Counter(p["classification_status"] for p in papers)
        lines.extend([f"## {layer}", "", f"Status counts: {dict(statuses)}", ""])
        pending = sorted((p for p in papers if p["classification_status"] == "needs-review"),
                         key=lambda p: (-p["year"], p["title"].casefold()))
        for start in range(0, len(pending), 200):
            filename = f"{layer}-{start // 200 + 1:03d}.md"
            chunk = pending[start:start + 200]
            lines.append(f"- [Records {start + 1}–{start + len(chunk)}]({filename})")
            page = [f"# {layer} classification review · {start + 1}–{start + len(chunk)}", "",
                    "[← Review queue](README.md)", "",
                    "| Paper | Year / layer | Provisional primary path | Evidence |",
                    "|---|---|---|---|"]
            for p in chunk:
                clean = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
                path = ("暂定二级 / provisional: " if p.get("subcategory_status") == "provisional" else "") + " → ".join(p[f] for f in ("track", "subcategory", "specialty"))
                page.append(f"| [{clean(p['title'])}]({p['paper_url']}) | {p['year']} · {layer} | {clean(path)} | {clean(p['primary_evidence'])}; {clean(p['taxonomy_evidence'])} |")
            outputs[review_dir / filename] = "\n".join(page) + "\n"
        lines.append("")
    outputs[review_dir / "README.md"] = "\n".join(lines) + "\n"

    topic_dir = root / "papers" / "topics"
    topics = ("Retargeting", "Hand Retargeting", "Whole-body Retargeting")
    overview = ["# Cross-topic views · 跨分类主题入口", "",
                "These are associated views, not extra primary assignments. Both source layers remain distinct.",
                "这些是关联入口，不重复计入主目录。顶会和 arXiv 保留各自的来源。", ""]
    for topic in topics:
        slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
        matching = [(layer, p) for layer, papers in layers.items() for p in papers if topic in p["related_topics"]]
        view = ["# " + topic, "", "[← Cross-topic views](README.md)", "",
                f"> {len(matching)} source records; rule-derived tags may need review. These counts are not unique-paper totals.", "",
                f"[Interactive cross-category filter](../../?{urlencode({'related_topics': topic})}#research-workbench)",
                "", "| Paper | Source layer | Primary path | Classification status |", "|---|---|---|---|"]
        # Partition to keep GitHub Markdown renderable.
        filenames = []
        for start in range(0, len(matching), 200):
            filename = f"{slug}-{start // 200 + 1:03d}.md"
            filenames.append(filename)
            page = [f"# {topic} · {start + 1}–{min(start + 200, len(matching))}", "",
                    f"[← Topic index]({slug}.md)", "", *view[-2:]]
            for layer, p in matching[start:start + 200]:
                title = p["title"].replace("|", "\\|")
                path = " → ".join(p[f] for f in ("track", "subcategory", "specialty")).replace("|", "\\|")
                page.append(f"| [{title}]({p['paper_url']}) | {layer} · {p['venue']} | {path} | {p['classification_status']} |")
            outputs[topic_dir / filename] = "\n".join(page) + "\n"
        view = view[:-2] + [f"- [Part {index + 1}]({name})" for index, name in enumerate(filenames)]
        outputs[topic_dir / f"{slug}.md"] = "\n".join(view) + "\n"
        overview.append(f"- [{topic}]({slug}.md): {len(matching)} source records")
    outputs[topic_dir / "README.md"] = "\n".join(overview) + "\n"
    return outputs

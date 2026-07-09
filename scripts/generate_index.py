#!/usr/bin/env python3
"""扫描 notes/ 下所有笔记，整体重建 notes/README.md 索引。

本脚本是主题分级的唯一数据源：SECTIONS 定义了主线、主题编号、目录名与显示名。
运行后会重写 notes/README.md，把每个主题目录下的 .md 笔记（除 README.md）
列为链接。文件头部的说明会保留。

用法：
    python scripts/generate_index.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "notes"
INDEX_FILE = NOTES_DIR / "README.md"

# 主线 -> [(目录名, 显示名), ...]。新增/调整主题只改这里。
SECTIONS: list[tuple[str, list[tuple[str, str]]]] = [
    ("感知与表示", [
        ("01-foundation-models", "基础模型"),
        ("02-3d-vision", "3D视觉"),
        ("03-gaussian-splatting", "高斯泼溅"),
        ("04-motion-tracking", "运动追踪"),
        ("05-tactile", "触觉感知"),
    ]),
    ("操作与抓取", [
        ("06-manipulation", "操作"),
        ("07-grasping", "抓取"),
        ("08-retargeting", "重定向/运动映射"),
    ]),
    ("运动与导航", [
        ("09-locomotion", "运动控制"),
        ("10-humanoid", "人形机器人"),
        ("11-navigation", "导航"),
    ]),
    ("策略学习", [
        ("12-diffusion-policy", "扩散策略"),
        ("13-rl", "强化学习"),
        ("14-vla", "VLA"),
    ]),
    ("仿真与数据", [
        ("15-simulation", "仿真"),
        ("16-data-generation", "数据生成"),
    ]),
    ("世界模型与生成", [
        ("17-world-model", "世界模型"),
        ("18-video-generation", "视频生成"),
    ]),
    ("遥操作与硬件", [
        ("19-teleoperation", "遥操作"),
        ("20-hardware", "硬件"),
    ]),
    ("其他", [
        ("21-others", "其他"),
    ]),
]

HEADER = (
    "# 笔记索引\n\n"
    "> 本文件由 `scripts/generate_index.py` 自动生成，请勿手动编辑。"
    "如需新增主题或调整顺序，编辑 `scripts/generate_index.py` 中的 SECTIONS 后重新运行。\n\n"
)


def collect_notes(topic: str) -> list[str]:
    """返回某主题目录下笔记的 markdown 链接行，按文件名排序。"""
    topic_dir = NOTES_DIR / topic
    if not topic_dir.is_dir():
        return []
    lines: list[str] = []
    for md in sorted(topic_dir.glob("*.md")):
        if md.name.lower() == "readme.md":
            continue
        title = md.stem
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                title = line.lstrip("# ").strip()
                break
        rel = md.relative_to(ROOT).as_posix()
        lines.append(f"- [{title}]({rel})")
    return lines


def build_index() -> str:
    out: list[str] = [HEADER]
    for section_name, topics in SECTIONS:
        out.append(f"## {section_name}\n")
        for dirname, display in topics:
            out.append(f"### {dirname.split('-', 1)[1]} · {display}\n")
            notes = collect_notes(dirname)
            if notes:
                out.append("\n".join(notes) + "\n")
            else:
                out.append("_暂无笔记_\n")
            out.append("\n")
    return "".join(out).rstrip() + "\n"


def main() -> None:
    new_text = build_index()
    INDEX_FILE.write_text(new_text, encoding="utf-8")
    print(f"已更新索引：{INDEX_FILE}")


if __name__ == "__main__":
    main()

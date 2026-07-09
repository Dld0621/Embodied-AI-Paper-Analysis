#!/usr/bin/env node
/**
 * 扫描 notes/ 下所有笔记，整体重建 notes/README.md 索引。
 *
 * 本脚本是主题分级的唯一数据源：SECTIONS 定义了主线、主题编号、目录名与显示名。
 * 运行后会重写 notes/README.md，把每个主题目录下的 .md 笔记（除 README.md）
 * 列为链接。文件头部的说明会保留。
 *
 * 用法：
 *     node scripts/generate_index.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const NOTES_DIR = path.join(ROOT, "notes");
const INDEX_FILE = path.join(NOTES_DIR, "README.md");

// 主线 -> [{ dirname, display }, ...]。新增/调整主题只改这里。
const SECTIONS = [
  ["感知与表示", [
    ["01-foundation-models", "基础模型"],
    ["02-3d-vision", "3D视觉"],
    ["03-gaussian-splatting", "高斯泼溅"],
    ["04-motion-tracking", "运动追踪"],
    ["05-tactile", "触觉感知"],
  ]],
  ["操作与抓取", [
    ["06-manipulation", "操作"],
    ["07-grasping", "抓取"],
    ["08-retargeting", "重定向/运动映射"],
  ]],
  ["运动与导航", [
    ["09-locomotion", "运动控制"],
    ["10-humanoid", "人形机器人"],
    ["11-navigation", "导航"],
  ]],
  ["策略学习", [
    ["12-diffusion-policy", "扩散策略"],
    ["13-rl", "强化学习"],
    ["14-vla", "VLA"],
  ]],
  ["仿真与数据", [
    ["15-simulation", "仿真"],
    ["16-data-generation", "数据生成"],
  ]],
  ["世界模型与生成", [
    ["17-world-model", "世界模型"],
    ["18-video-generation", "视频生成"],
  ]],
  ["遥操作与硬件", [
    ["19-teleoperation", "遥操作"],
    ["20-hardware", "硬件"],
  ]],
  ["其他", [
    ["21-others", "其他"],
  ]],
];

// 索引文件头部说明
const HEADER =
  "# 笔记索引\n\n" +
  "> 本文件由 `scripts/generate_index.js` 自动生成，请勿手动编辑。" +
  "如需新增主题或调整顺序，编辑 `scripts/generate_index.js` 中的 SECTIONS 后重新运行。\n\n";

/**
 * 返回某主题目录下笔记的 markdown 链接行，按文件名排序。
 * @param {string} topic - 主题目录名，如 "01-foundation-models"
 * @returns {string[]} markdown 链接行数组
 */
function collectNotes(topic) {
  const topicDir = path.join(NOTES_DIR, topic);

  // 如果目录不存在则返回空数组
  if (!fs.existsSync(topicDir) || !fs.statSync(topicDir).isDirectory()) {
    return [];
  }

  // 筛选 .md 文件（排除 README.md），按文件名排序
  const mdFiles = fs.readdirSync(topicDir)
    .filter((f) => f.endsWith(".md") && f.toLowerCase() !== "readme.md")
    .sort();

  const lines = [];

  for (const filename of mdFiles) {
    const filePath = path.join(topicDir, filename);
    const content = fs.readFileSync(filePath, "utf-8");

    // 默认标题为文件名（去掉扩展名）
    let title = path.basename(filename, ".md");

    // 从文件第一行 # 开头的内容提取标题
    for (const line of content.split(/\r?\n/)) {
      if (line.startsWith("# ")) {
        title = line.replace(/^#\s+/, "").trim();
        break;
      }
    }

    // 生成相对路径（统一使用正斜杠）
    const rel = path.relative(ROOT, filePath).replace(/\\/g, "/");

    lines.push(`- [${title}](${rel})`);
  }

  return lines;
}

/**
 * 构建完整的索引文本
 * @returns {string} 索引 markdown 内容
 */
function buildIndex() {
  const out = [HEADER];

  for (const [sectionName, topics] of SECTIONS) {
    out.push(`## ${sectionName}\n`);

    for (const [dirname, display] of topics) {
      // 从目录名提取编号后的名称，例如 "01-foundation-models" -> "foundation-models"
      const dirLabel = dirname.split("-").slice(1).join("-");
      out.push(`### ${dirLabel} · ${display}\n`);

      const notes = collectNotes(dirname);
      if (notes.length > 0) {
        out.push(notes.join("\n") + "\n");
      } else {
        out.push("_暂无笔记_\n");
      }

      out.push("\n");
    }
  }

  return out.join("").replace(/\n+$/, "") + "\n";
}

// 主函数：生成索引并写入文件
function main() {
  const newText = buildIndex();
  fs.writeFileSync(INDEX_FILE, newText, "utf-8");
  console.log(`已更新索引：${INDEX_FILE}`);
}

main();

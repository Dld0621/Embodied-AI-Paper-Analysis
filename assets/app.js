const I18N = {
  en: {
    skip: "Skip to research workbench", navWorkbench: "Workbench", navDirections: "Research map", navPolicy: "Method", readingList: "Reading list",
    eyebrow: "Systematic census · 2022–2026 · updated 2026-08-07", heroLineOne: "Research the field.", heroLineTwo: "Not the feed.",
    heroLead: "A bilingual, source-aware workbench for tracing the papers, pipelines, and research directions shaping embodied intelligence.",
    openWorkbench: "Open research workbench", browseMarkdown: "Browse Markdown index", heroNote: "Systematic census under an explicit, auditable boundary. Every record includes an online paper and provenance link.",
    scope: "Research corpus", audited: "AUDITED", papers: "papers", venues: "major venues", tracks: "research tracks", latest: "2026 records", linked: "source linked",
    workbenchKicker: "Research workbench", catalogTitle: "Move from discovery to a usable reading set.", catalogLead: "Search the full corpus, inspect provenance, save a local reading list, and export the exact view you are using.",
    allPapers: "All papers", savedPapers: "Reading list", shareView: "Share view", filters: "Filters", reset: "Reset",
    searchPlaceholder: "Search title, topic, venue", sort: "Sort order", sortLatest: "Latest first", sortOldest: "Oldest first", sortTitle: "Title A–Z",
    year: "Year", venue: "Venue", track: "Research track", sourceTier: "Source tier", all: "All", results: "matching papers", showing: "showing", loadMore: "Load 120 more",
    official: "Official", publisher: "Publisher", index: "Index", paper: "Paper", source: "Source", code: "Code", save: "Save paper", remove: "Remove from reading list",
    emptyTitle: "No papers match this view.", emptyLead: "Broaden the filters or return to the complete catalog.", exportNote: "Exports contain only verified catalog fields; unavailable author metadata is never inferred.",
    directionKicker: "Research map", directionTitle: "Seven directions, each expressed as a research pipeline.", directionLead: "Use the map to move from a scientific question to the relevant five-year literature, with coverage visible before you open the catalog.",
    pipeline: "Research pipeline", papersAcross: "papers across", venuePlural: "venues", browseDirection: "Open direction in workbench",
    policyKicker: "Census contract", policyTitle: "Transparent enough to inspect. Stable enough to reproduce.", policyLead: "Completeness is measured against a published operational boundary—not an undefined claim to every paper anyone might call Embodied AI.", readMethod: "Read the full methodology",
    policyOneTitle: "Rolling five-year window", policyOneBody: "Conference years 2022 through 2026, inclusive.",
    policyTwoTitle: "Reproducible discovery", policyTwoBody: "Ten fixed venues are searched through conference-indexed metadata with the query “robot”.",
    policyThreeTitle: "Deterministic admission", policyThreeBody: "Title taxonomy, medical exclusions, normalized-title deduplication, and one primary direction per paper.",
    policyFourTitle: "Tiered provenance", policyFourBody: "Every row links a paper plus an official, publisher, or bibliographic source whose tier is shown honestly.",
    footerLine: "Open infrastructure for rigorous literature work.", contribute: "Contribute", copied: "Shareable view copied", saved: "Added to reading list", removed: "Removed from reading list",
    markdownExported: "Markdown exported", csvExported: "CSV exported", columnPaper: "Paper", columnYear: "Year", columnVenue: "Venue", columnSource: "Provenance", columnActions: "Links"
  },
  zh: {
    skip: "跳转到科研工作台", navWorkbench: "科研工作台", navDirections: "研究地图", navPolicy: "方法", readingList: "阅读清单",
    eyebrow: "系统性论文普查 · 2022–2026 · 更新于 2026-08-07", heroLineOne: "研究整个领域。", heroLineTwo: "不被信息流裹挟。",
    heroLead: "面向科研工作者的双语、来源透明的具身智能论文工作台，连接论文、研究流程与领域方向。",
    openWorkbench: "进入科研工作台", browseMarkdown: "浏览 Markdown 索引", heroNote: "Systematic census：在明确、可审计的边界下进行系统性普查；每条记录均提供论文与来源链接。",
    scope: "科研语料库", audited: "已审计", papers: "篇论文", venues: "个主要顶会", tracks: "条研究主线", latest: "篇 2026 记录", linked: "来源已链接",
    workbenchKicker: "科研工作台", catalogTitle: "从发现论文，到形成可用的阅读集合。", catalogLead: "检索完整语料、核对来源、保存本地阅读清单，并导出当前使用的精确视图。",
    allPapers: "全部论文", savedPapers: "阅读清单", shareView: "分享视图", filters: "筛选条件", reset: "重置",
    searchPlaceholder: "搜索标题、主题或会议", sort: "排序方式", sortLatest: "最新优先", sortOldest: "最早优先", sortTitle: "标题 A–Z",
    year: "年份", venue: "会议", track: "研究主线", sourceTier: "来源层级", all: "全部", results: "篇匹配论文", showing: "当前显示", loadMore: "再加载 120 篇",
    official: "官方", publisher: "出版社", index: "文献索引", paper: "论文", source: "来源", code: "代码", save: "加入阅读清单", remove: "从阅读清单移除",
    emptyTitle: "当前视图没有匹配论文。", emptyLead: "请放宽筛选条件，或返回完整目录。", exportNote: "导出只包含已核验的目录字段；缺失的作者信息不会被推测或补造。",
    directionKicker: "研究地图", directionTitle: "七个研究方向，每个方向都有明确的研究流程。", directionLead: "从科学问题进入近五年相关文献；在打开目录前即可查看年份、顶会与流程覆盖。",
    pipeline: "研究流程", papersAcross: "篇论文，覆盖", venuePlural: "个顶会", browseDirection: "在工作台打开此方向",
    policyKicker: "普查契约", policyTitle: "足够透明以供审查，足够稳定以便复现。", policyLead: "完整性以公开的操作性边界衡量，而不是声称覆盖所有人可能称为具身智能的论文。", readMethod: "阅读完整方法",
    policyOneTitle: "滚动五年窗口", policyOneBody: "会议年份限定为 2022 至 2026。",
    policyTwoTitle: "可复现发现", policyTwoBody: "通过会议索引元数据，以 robot 为查询词检索固定十个顶会。",
    policyThreeTitle: "确定性纳入", policyThreeBody: "采用标题分类、医学排除、归一化标题去重，并为每篇论文分配一个主方向。",
    policyFourTitle: "分层来源", policyFourBody: "每条记录同时链接论文和官方、出版社或文献索引来源，并如实显示来源层级。",
    footerLine: "服务严谨文献研究的开放基础设施。", contribute: "参与贡献", copied: "可分享视图已复制", saved: "已加入阅读清单", removed: "已从阅读清单移除",
    markdownExported: "Markdown 已导出", csvExported: "CSV 已导出", columnPaper: "论文", columnYear: "年份", columnVenue: "会议", columnSource: "来源", columnActions: "链接"
  }
};

const PAGE_SIZE = 120;
const STORAGE_KEY = "embodied-ai-reading-list-v1";
const $ = (selector) => document.querySelector(selector);
const escapeHtml = (value) => String(value).replace(/[&<>\"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char]));
const label = (key) => I18N[state.language][key] || key;
const paperKey = (paper) => `${paper.year}::${paper.venue}::${paper.title}`;

function loadSaved() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    return new Set(Array.isArray(stored) ? stored : []);
  } catch (_) {
    return new Set();
  }
}

const state = {
  papers: [], catalog: null, language: localStorage.getItem("language") || "en",
  year: "all", venue: "all", track: "all", source: "all", query: "", sort: "latest",
  view: "all", visible: PAGE_SIZE, saved: loadSaved()
};

function number(value) {
  return new Intl.NumberFormat(state.language === "zh" ? "zh-CN" : "en-US").format(value);
}

function trackName(track) {
  if (state.language === "zh" && state.catalog?.track_meta?.[track]) return state.catalog.track_meta[track].name_zh;
  return track;
}

function sourceName(sourceType) {
  if (sourceType === "publisher") return label("publisher");
  if (sourceType === "bibliographic") return label("index");
  return label("official");
}

function counts(items, field) {
  return items.reduce((map, item) => map.set(item[field], (map.get(item[field]) || 0) + 1), new Map());
}

function applyLanguage() {
  document.documentElement.lang = state.language === "zh" ? "zh-CN" : "en";
  document.title = state.language === "zh" ? "具身智能 · 科研工作台" : "Embodied AI · Research Workbench";
  document.querySelectorAll("[data-i18n]").forEach((node) => { node.textContent = label(node.dataset.i18n); });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((node) => { node.placeholder = label(node.dataset.i18nPlaceholder); });
  $("#language-toggle").textContent = state.language === "en" ? "中文" : "EN";
  renderAll();
  updateUrl();
}

function renderStats() {
  const sourceCounts = counts(state.papers, "source_type");
  $("#paper-count").textContent = number(state.papers.length);
  $("#venue-count").textContent = number(state.catalog.venues.length);
  $("#track-count").textContent = number(state.catalog.tracks.length);
  $("#latest-count").textContent = number(state.papers.filter((paper) => paper.year === state.catalog.window.end).length);
  $("#scope-provenance").innerHTML = ["official", "publisher", "bibliographic"].map((type) => {
    const count = sourceCounts.get(type) || 0;
    const width = Math.max(2, count / state.papers.length * 100);
    return `<div><span><i class="tier-dot ${type}"></i>${sourceName(type)}</span><strong>${number(count)}</strong><b><i class="${type}" style="width:${width}%"></i></b></div>`;
  }).join("");

  const trackCounts = counts(state.papers, "track");
  $("#track-ticker").innerHTML = state.catalog.tracks.map((track) => `<button type="button" data-direction="${escapeHtml(track)}"><strong title="${escapeHtml(trackName(track))}">${escapeHtml(trackName(track))}</strong><span>${number(trackCounts.get(track) || 0)} ${label("papers")}</span></button>`).join("");
}

function renderDirections() {
  const years = Array.from({ length: state.catalog.window.end - state.catalog.window.start + 1 }, (_, index) => state.catalog.window.start + index);
  $("#direction-grid").innerHTML = state.catalog.tracks.map((track, index) => {
    const meta = state.catalog.track_meta[track];
    const papers = state.papers.filter((paper) => paper.track === track);
    const paperYears = new Set(papers.map((paper) => paper.year));
    const venues = new Set(papers.map((paper) => paper.venue));
    const stages = state.language === "zh" ? meta.pipeline_zh : meta.pipeline;
    const question = state.language === "zh" ? meta.question_zh : meta.question;
    return `<article class="direction-card">
      <div class="direction-card-top"><span>0${index + 1}</span><div class="year-coverage">${years.map((year) => `<i class="${paperYears.has(year) ? "covered" : ""}">${year}</i>`).join("")}</div></div>
      <h3>${escapeHtml(trackName(track))}</h3>
      <p>${escapeHtml(question)}</p>
      <div class="direction-stats"><strong>${number(papers.length)}</strong> ${label("papersAcross")} <strong>${number(venues.size)}</strong> ${label("venuePlural")}</div>
      <div class="pipeline"><span>${label("pipeline")}</span><ol>${stages.map((stage) => `<li>${escapeHtml(stage)}</li>`).join("")}</ol></div>
      <button type="button" data-direction="${escapeHtml(track)}">${label("browseDirection")} <span aria-hidden="true">→</span></button>
    </article>`;
  }).join("");
}

function chip(value, text, active, type, count) {
  const suffix = Number.isFinite(count) ? `<small>${number(count)}</small>` : "";
  return `<button class="filter-chip" type="button" data-filter="${type}" data-value="${escapeHtml(value)}" aria-pressed="${active}"><span>${escapeHtml(text)}</span>${suffix}</button>`;
}

function renderFilters() {
  const years = Array.from(new Set(state.papers.map((paper) => paper.year))).sort((a, b) => b - a);
  const yearCounts = counts(state.papers, "year");
  const venueCounts = counts(state.papers, "venue");
  const trackCounts = counts(state.papers, "track");
  const sourceCounts = counts(state.papers, "source_type");
  $("#year-filters").innerHTML = chip("all", label("all"), state.year === "all", "year", state.papers.length) + years.map((year) => chip(year, year, String(state.year) === String(year), "year", yearCounts.get(year))).join("");
  $("#venue-filters").innerHTML = chip("all", label("all"), state.venue === "all", "venue", state.papers.length) + state.catalog.venues.map((venue) => chip(venue, venue, state.venue === venue, "venue", venueCounts.get(venue))).join("");
  $("#track-filters").innerHTML = chip("all", label("all"), state.track === "all", "track", state.papers.length) + state.catalog.tracks.map((track) => chip(track, trackName(track), state.track === track, "track", trackCounts.get(track))).join("");
  $("#source-type-filters").innerHTML = chip("all", label("all"), state.source === "all", "source", state.papers.length) + ["official", "publisher", "bibliographic"].map((type) => chip(type, sourceName(type), state.source === type, "source", sourceCounts.get(type))).join("");
  document.querySelectorAll("[data-view]").forEach((button) => { button.setAttribute("aria-pressed", String(button.dataset.view === state.view)); });
  $("#sort-select").value = state.sort;
}

function filteredPapers() {
  const query = state.query.trim().toLocaleLowerCase();
  const items = state.papers.filter((paper) => {
    const haystack = `${paper.title} ${paper.topic} ${paper.track} ${paper.venue}`.toLocaleLowerCase();
    return (state.view === "all" || state.saved.has(paperKey(paper))) &&
      (state.year === "all" || String(paper.year) === String(state.year)) &&
      (state.venue === "all" || paper.venue === state.venue) &&
      (state.track === "all" || paper.track === state.track) &&
      (state.source === "all" || paper.source_type === state.source) &&
      (!query || haystack.includes(query));
  });
  return items.sort((a, b) => {
    if (state.sort === "oldest") return a.year - b.year || a.title.localeCompare(b.title);
    if (state.sort === "title") return a.title.localeCompare(b.title);
    return b.year - a.year || a.title.localeCompare(b.title);
  });
}

function renderSavedCounts() {
  const savedCount = state.saved.size;
  $("#saved-count").textContent = number(savedCount);
  $("#toolbar-saved-count").textContent = number(savedCount);
}

function renderPapers() {
  const items = filteredPapers();
  const visibleItems = items.slice(0, state.visible);
  $("#result-count").textContent = number(items.length);
  $("#showing-count").textContent = number(visibleItems.length);
  $("#load-more").hidden = visibleItems.length >= items.length;
  $("#load-more").textContent = label("loadMore");
  $("#empty-state").hidden = items.length !== 0;
  const header = `<div class="paper-table-head" role="row">
    <span role="columnheader" aria-label="Reading list"></span><span role="columnheader">${label("columnPaper")}</span><span role="columnheader">${label("columnYear")}</span><span role="columnheader">${label("columnVenue")}</span><span role="columnheader">${label("columnSource")}</span><span role="columnheader">${label("columnActions")}</span>
  </div>`;
  const rows = visibleItems.map((paper) => {
    const key = paperKey(paper);
    const saved = state.saved.has(key);
    const code = paper.code_url ? `<a href="${escapeHtml(paper.code_url)}" target="_blank" rel="noopener">${label("code")} ↗</a>` : "";
    return `<article class="paper-row" role="row">
      <div role="cell"><button class="save-button" type="button" data-save-key="${escapeHtml(key)}" aria-pressed="${saved}" aria-label="${escapeHtml(saved ? label("remove") : label("save"))}" title="${escapeHtml(saved ? label("remove") : label("save"))}"><span aria-hidden="true">${saved ? "●" : "○"}</span></button></div>
      <div class="paper-identity" role="cell"><a href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener"><strong>${escapeHtml(paper.title)}</strong></a><span>${escapeHtml(trackName(paper.track))}<i>·</i>${escapeHtml(paper.topic)}</span></div>
      <div class="paper-year" role="cell"><span class="mobile-label">${label("year")}</span>${paper.year}</div>
      <div class="paper-venue" role="cell"><span class="mobile-label">${label("venue")}</span><strong>${escapeHtml(paper.venue)}</strong></div>
      <div class="paper-source" role="cell"><span class="mobile-label">${label("sourceTier")}</span><a href="${escapeHtml(paper.official_url)}" target="_blank" rel="noopener"><i class="tier-dot ${escapeHtml(paper.source_type)}"></i>${sourceName(paper.source_type)}</a></div>
      <div class="paper-links" role="cell"><a class="primary-link" href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener">${label("paper")} ↗</a><a href="${escapeHtml(paper.official_url)}" target="_blank" rel="noopener">${label("source")} ↗</a>${code}</div>
    </article>`;
  }).join("");
  $("#paper-grid").innerHTML = header + rows;
  renderSavedCounts();
}

function renderAll() {
  if (!state.catalog) return;
  renderStats();
  renderDirections();
  renderFilters();
  renderPapers();
}

function updateUrl() {
  if (!state.catalog) return;
  const params = new URLSearchParams();
  if (state.query) params.set("q", state.query);
  if (state.year !== "all") params.set("year", state.year);
  if (state.venue !== "all") params.set("venue", state.venue);
  if (state.track !== "all") params.set("track", state.track);
  if (state.source !== "all") params.set("source", state.source);
  if (state.sort !== "latest") params.set("sort", state.sort);
  if (state.view !== "all") params.set("view", state.view);
  if (state.language !== "en") params.set("lang", state.language);
  const query = params.toString();
  history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
}

function readUrlState() {
  const params = new URLSearchParams(location.search);
  const validYears = new Set(state.papers.map((paper) => String(paper.year)));
  const year = params.get("year");
  const venue = params.get("venue");
  const track = params.get("track");
  const source = params.get("source");
  const sort = params.get("sort");
  const view = params.get("view");
  if (year && validYears.has(year)) state.year = year;
  if (venue && state.catalog.venues.includes(venue)) state.venue = venue;
  if (track && state.catalog.tracks.includes(track)) state.track = track;
  if (["official", "publisher", "bibliographic"].includes(source)) state.source = source;
  if (["latest", "oldest", "title"].includes(sort)) state.sort = sort;
  if (["all", "saved"].includes(view)) state.view = view;
  if (["en", "zh"].includes(params.get("lang"))) state.language = params.get("lang");
  state.query = params.get("q") || "";
  $("#paper-search").value = state.query;
}

function setView(view) {
  state.view = view;
  state.visible = PAGE_SIZE;
  renderFilters();
  renderPapers();
  updateUrl();
}

function clearFilters() {
  Object.assign(state, { year: "all", venue: "all", track: "all", source: "all", query: "", sort: "latest", view: "all", visible: PAGE_SIZE });
  $("#paper-search").value = "";
  renderFilters();
  renderPapers();
  updateUrl();
}

function showToast(message) {
  const toast = $("#toast");
  toast.textContent = message;
  toast.hidden = false;
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => { toast.hidden = true; }, 2200);
}

function toggleSaved(key) {
  if (state.saved.has(key)) {
    state.saved.delete(key);
    showToast(label("removed"));
  } else {
    state.saved.add(key);
    showToast(label("saved"));
  }
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...state.saved]));
  renderPapers();
}

function downloadFile(filename, content, type) {
  const url = URL.createObjectURL(new Blob([content], { type }));
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
}

function exportMarkdown() {
  const items = filteredPapers();
  const escapeCell = (value) => String(value || "").replace(/\|/g, "\\|").replace(/\r?\n/g, " ");
  const lines = [
    "# Embodied AI Research View", "", `> ${items.length} papers · exported ${new Date().toISOString().slice(0, 10)}`, "",
    "| Year | Venue | Paper | Track | Topic | Provenance |", "|---:|---|---|---|---|---|",
    ...items.map((paper) => `| ${paper.year} | ${escapeCell(paper.venue)} | [${escapeCell(paper.title)}](${paper.paper_url}) | ${escapeCell(paper.track)} | ${escapeCell(paper.topic)} | [${paper.source_type}](${paper.official_url}) |`),
    "", "_Exported from Embodied AI Paper Analysis. Author metadata is not inferred._", ""
  ];
  downloadFile("embodied-ai-research-view.md", lines.join("\n"), "text/markdown;charset=utf-8");
  showToast(label("markdownExported"));
}

function exportCsv() {
  const quote = (value) => `"${String(value || "").replace(/"/g, '""')}"`;
  const header = ["Title", "Year", "Venue", "Track", "Topic", "Paper URL", "Source URL", "Source Type", "Code URL"];
  const rows = filteredPapers().map((paper) => [paper.title, paper.year, paper.venue, paper.track, paper.topic, paper.paper_url, paper.official_url, paper.source_type, paper.code_url || ""]);
  downloadFile("embodied-ai-research-view.csv", `\ufeff${[header, ...rows].map((row) => row.map(quote).join(",")).join("\r\n")}`, "text/csv;charset=utf-8");
  showToast(label("csvExported"));
}

async function shareView() {
  updateUrl();
  const url = location.href;
  try {
    await navigator.clipboard.writeText(url);
  } catch (_) {
    const input = document.createElement("textarea");
    input.value = url;
    input.style.position = "fixed";
    input.style.opacity = "0";
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    input.remove();
  }
  showToast(label("copied"));
}

async function initialize() {
  const storedTheme = localStorage.getItem("theme");
  const preferredDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.dataset.theme = storedTheme || (preferredDark ? "dark" : "light");
  try {
    const response = await fetch("data/papers.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.catalog = await response.json();
    state.papers = state.catalog.papers;
    readUrlState();
    applyLanguage();
  } catch (error) {
    $("#paper-grid").innerHTML = `<div class="empty-state"><strong>Catalog unavailable</strong><p>${escapeHtml(error.message)}</p></div>`;
  }
}

document.addEventListener("click", (event) => {
  const directionButton = event.target.closest("[data-direction]");
  if (directionButton) {
    Object.assign(state, { track: directionButton.dataset.direction, year: "all", venue: "all", source: "all", query: "", view: "all", visible: PAGE_SIZE });
    $("#paper-search").value = "";
    renderFilters();
    renderPapers();
    updateUrl();
    $("#research-workbench").scrollIntoView({ behavior: "smooth", block: "start" });
    return;
  }
  const chipButton = event.target.closest("[data-filter]");
  if (chipButton) {
    state[chipButton.dataset.filter] = chipButton.dataset.value;
    state.visible = PAGE_SIZE;
    renderFilters();
    renderPapers();
    updateUrl();
    return;
  }
  const saveButton = event.target.closest("[data-save-key]");
  if (saveButton) {
    toggleSaved(saveButton.dataset.saveKey);
    return;
  }
  const viewButton = event.target.closest("[data-view]");
  if (viewButton) setView(viewButton.dataset.view);
});

$("#paper-search").addEventListener("input", (event) => { state.query = event.target.value; state.visible = PAGE_SIZE; renderPapers(); updateUrl(); });
$("#sort-select").addEventListener("change", (event) => { state.sort = event.target.value; state.visible = PAGE_SIZE; renderPapers(); updateUrl(); });
$("#clear-filters").addEventListener("click", clearFilters);
$("#load-more").addEventListener("click", () => { state.visible += PAGE_SIZE; renderPapers(); });
$("#header-saved").addEventListener("click", () => { setView("saved"); $("#research-workbench").scrollIntoView({ behavior: "smooth", block: "start" }); });
$("#share-view").addEventListener("click", shareView);
$("#export-markdown").addEventListener("click", exportMarkdown);
$("#export-csv").addEventListener("click", exportCsv);
$("#language-toggle").addEventListener("click", () => { state.language = state.language === "en" ? "zh" : "en"; localStorage.setItem("language", state.language); applyLanguage(); });
$("#theme-toggle").addEventListener("click", () => { const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark"; document.documentElement.dataset.theme = next; localStorage.setItem("theme", next); });
document.addEventListener("keydown", (event) => {
  const isTyping = ["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName);
  if (((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") || (event.key === "/" && !isTyping)) {
    event.preventDefault();
    $("#paper-search").focus();
  }
  if (event.key === "Escape" && document.activeElement === $("#paper-search")) {
    state.query = "";
    $("#paper-search").value = "";
    renderPapers();
    updateUrl();
  }
});

initialize();

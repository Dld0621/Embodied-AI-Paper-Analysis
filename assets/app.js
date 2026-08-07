const I18N = {
  en: {
    navPolicy: "Policy", eyebrow: "Curated research index · updated 2026-08-07",
    heroLineOne: "Five years.", heroLineTwo: "One research map.",
    heroLead: "A precise, source-backed path through the papers shaping embodied perception, reasoning, action, and physical systems.",
    acceptedOnly: "Accepted papers only", selective: "Selective, not exhaustive", explore: "Explore catalog", readMarkdown: "Read on GitHub",
    scope: "Research scope", verified: "VERIFIED", curatedPapers: "curated papers", venues: "Major venues", tracks: "Research tracks",
    latest: "2026 accepted", sourceRule: "Official source", seePolicy: "See selection policy",
    latestKicker: "Latest verified layer", spotlightTitle: "2026 conference papers", spotlightLead: "Only decisions already visible on official conference or proceedings pages as of August 7.",
    catalogKicker: "Five-year index", catalogTitle: "Find the paper that moves your work forward.", catalogLead: "Search complete titles, then narrow by conference year, venue, or research track.",
    searchPlaceholder: "Search papers or topics", sort: "Sort", sortLatest: "Latest first", sortOldest: "Oldest first", sortTitle: "Title A–Z",
    year: "Year", venue: "Venue", track: "Track", all: "All", results: "papers in view", clear: "Clear filters",
    emptyTitle: "No papers match this view.", emptyLead: "Try a broader year, venue, track, or search term.",
    policyKicker: "Selection contract", policyTitle: "Small enough to trust. Broad enough to navigate.", policyLead: "A paper enters the core map only when its year, venue, embodied relevance, and official acceptance source are explicit.",
    policyOneTitle: "Rolling five-year window", policyOneBody: "Conference years 2022 through 2026, inclusive.",
    policyTwoTitle: "Formal acceptance", policyTwoBody: "Main conference or official conference track—not workshop, withdrawn, under review, or arXiv-only.",
    policyThreeTitle: "One paper, one venue", policyThreeBody: "No ambiguous labels such as RSS/CoRL/ICRA and no duplicate title variants.",
    policyFourTitle: "Official provenance", policyFourBody: "Every row carries a proceedings, conference, publisher, or accepted OpenReview source.",
    footerLine: "Curated for research, not for vanity metrics.", contribute: "Contribute", paper: "Paper", official: "Official", code: "Code", open: "Open paper"
  },
  zh: {
    navPolicy: "规则", eyebrow: "精选研究索引 · 更新于 2026-08-07",
    heroLineOne: "五年论文。", heroLineTwo: "一张研究地图。",
    heroLead: "用可核验来源连接塑造具身感知、推理、行动与物理系统的关键论文。",
    acceptedOnly: "仅正式录用论文", selective: "精选而非穷举", explore: "浏览论文目录", readMarkdown: "在 GitHub 阅读",
    scope: "研究范围", verified: "已核验", curatedPapers: "篇精选论文", venues: "主要顶会", tracks: "研究主线",
    latest: "2026 已录用", sourceRule: "官方来源", seePolicy: "查看收录规则",
    latestKicker: "最新核验层", spotlightTitle: "2026 顶会论文", spotlightLead: "只包含截至 8 月 7 日已在官方会议或论文集页面确认的录用结果。",
    catalogKicker: "近五年索引", catalogTitle: "找到真正推动研究的论文。", catalogLead: "搜索完整标题，再按会议年份、顶会或研究主线收敛。",
    searchPlaceholder: "搜索论文或主题", sort: "排序", sortLatest: "最新优先", sortOldest: "最早优先", sortTitle: "标题 A–Z",
    year: "年份", venue: "会议", track: "主线", all: "全部", results: "篇论文", clear: "清除筛选",
    emptyTitle: "当前条件下没有论文。", emptyLead: "尝试放宽年份、会议、主线或搜索词。",
    policyKicker: "收录契约", policyTitle: "足够精简，才能可信；覆盖主线，才能导航。", policyLead: "只有年份、会议、具身相关性和正式录用来源都明确，论文才进入核心目录。",
    policyOneTitle: "滚动五年窗口", policyOneBody: "会议年份限定为 2022 至 2026。",
    policyTwoTitle: "正式录用", policyTwoBody: "仅主会或官方会议赛道；不含 workshop、撤稿、在审或纯 arXiv。",
    policyThreeTitle: "一篇论文，一个会议", policyThreeBody: "不使用 RSS/CoRL/ICRA 等模糊标签，也不保留标题变体重复项。",
    policyFourTitle: "官方来源", policyFourBody: "每条记录都包含论文集、会议、出版社或已录用 OpenReview 页面。",
    footerLine: "为研究判断而精选，不为数量指标堆积。", contribute: "参与贡献", paper: "论文", official: "录用来源", code: "代码", open: "打开论文"
  }
};

const state = { papers: [], catalog: null, language: localStorage.getItem("language") || "en", year: "all", venue: "all", track: "all", query: "", sort: "latest" };
const $ = (selector) => document.querySelector(selector);
const escapeHtml = (value) => String(value).replace(/[&<>"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char]));
const label = (key) => I18N[state.language][key] || key;

function applyLanguage() {
  document.documentElement.lang = state.language === "zh" ? "zh-CN" : "en";
  document.querySelectorAll("[data-i18n]").forEach((node) => { node.textContent = label(node.dataset.i18n); });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((node) => { node.placeholder = label(node.dataset.i18nPlaceholder); });
  $("#language-toggle").textContent = state.language === "en" ? "中文" : "EN";
  renderAll();
}

function counts(items, field) {
  return items.reduce((map, item) => map.set(item[field], (map.get(item[field]) || 0) + 1), new Map());
}

function renderStats() {
  $("#paper-count").textContent = state.papers.length;
  $("#venue-count").textContent = state.catalog.venues.length;
  $("#track-count").textContent = state.catalog.tracks.length;
  $("#latest-count").textContent = state.papers.filter((paper) => paper.year === state.catalog.window.end).length;
  const trackCounts = counts(state.papers, "track");
  $("#track-ticker").innerHTML = state.catalog.tracks.map((track) => `<div class="ticker-item"><strong title="${escapeHtml(track)}">${escapeHtml(track)}</strong><span>${trackCounts.get(track) || 0} ${state.language === "zh" ? "篇" : "papers"}</span></div>`).join("");
}

function renderSpotlight() {
  const latest = state.papers.filter((paper) => paper.year === state.catalog.window.end).slice(0, 6);
  $("#spotlight-grid").innerHTML = latest.map((paper) => `<a class="spotlight-card" href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener"><div><div class="spotlight-meta"><span class="venue-badge">${escapeHtml(paper.venue)}</span><span>${paper.year}</span><span>·</span><span>${escapeHtml(paper.topic)}</span></div><h3>${escapeHtml(paper.title)}</h3></div><span>${label("open")} ↗</span></a>`).join("");
}

function chip(value, text, active, type) {
  return `<button class="filter-chip" type="button" data-filter="${type}" data-value="${escapeHtml(value)}" aria-pressed="${active}">${escapeHtml(text)}</button>`;
}

function renderFilters() {
  const years = Array.from(new Set(state.papers.map((paper) => paper.year))).sort((a, b) => b - a);
  $("#year-filters").innerHTML = chip("all", label("all"), state.year === "all", "year") + years.map((year) => chip(year, year, String(state.year) === String(year), "year")).join("");
  $("#venue-filters").innerHTML = chip("all", label("all"), state.venue === "all", "venue") + state.catalog.venues.map((venue) => chip(venue, venue, state.venue === venue, "venue")).join("");
  $("#track-filters").innerHTML = chip("all", label("all"), state.track === "all", "track") + state.catalog.tracks.map((track) => chip(track, track, state.track === track, "track")).join("");
}

function filteredPapers() {
  const query = state.query.trim().toLocaleLowerCase();
  const items = state.papers.filter((paper) => {
    const haystack = `${paper.title} ${paper.topic} ${paper.track} ${paper.venue}`.toLocaleLowerCase();
    return (state.year === "all" || String(paper.year) === String(state.year)) &&
      (state.venue === "all" || paper.venue === state.venue) &&
      (state.track === "all" || paper.track === state.track) &&
      (!query || haystack.includes(query));
  });
  return items.sort((a, b) => {
    if (state.sort === "oldest") return a.year - b.year || a.title.localeCompare(b.title);
    if (state.sort === "title") return a.title.localeCompare(b.title);
    return b.year - a.year || a.title.localeCompare(b.title);
  });
}

function renderPapers() {
  const items = filteredPapers();
  $("#result-count").textContent = items.length;
  $("#empty-state").hidden = items.length !== 0;
  $("#paper-grid").innerHTML = items.map((paper) => {
    const code = paper.code_url ? `<a href="${escapeHtml(paper.code_url)}" target="_blank" rel="noopener">${label("code")} ↗</a>` : "";
    return `<article class="paper-card"><div class="paper-meta"><span class="venue-badge">${escapeHtml(paper.venue)}</span><span class="year-badge">${paper.year}</span><span class="paper-topic">${escapeHtml(paper.track)} · ${escapeHtml(paper.topic)}</span></div><h3>${escapeHtml(paper.title)}</h3><div class="paper-links"><a href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener">${label("paper")} ↗</a><a href="${escapeHtml(paper.official_url)}" target="_blank" rel="noopener">${label("official")} ↗</a>${code}</div></article>`;
  }).join("");
}

function renderAll() {
  if (!state.catalog) return;
  renderStats();
  renderSpotlight();
  renderFilters();
  renderPapers();
}

function clearFilters() {
  Object.assign(state, { year: "all", venue: "all", track: "all", query: "" });
  $("#paper-search").value = "";
  renderAll();
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
    applyLanguage();
  } catch (error) {
    $("#paper-grid").innerHTML = `<div class="empty-state"><strong>Catalog unavailable</strong><p>${escapeHtml(error.message)}</p></div>`;
  }
}

document.addEventListener("click", (event) => {
  const chipButton = event.target.closest("[data-filter]");
  if (chipButton) {
    state[chipButton.dataset.filter] = chipButton.dataset.value;
    renderFilters();
    renderPapers();
  }
});
$("#paper-search").addEventListener("input", (event) => { state.query = event.target.value; renderPapers(); });
$("#sort-select").addEventListener("change", (event) => { state.sort = event.target.value; renderPapers(); });
$("#clear-filters").addEventListener("click", clearFilters);
$("#language-toggle").addEventListener("click", () => { state.language = state.language === "en" ? "zh" : "en"; localStorage.setItem("language", state.language); applyLanguage(); });
$("#theme-toggle").addEventListener("click", () => { const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark"; document.documentElement.dataset.theme = next; localStorage.setItem("theme", next); });
document.addEventListener("keydown", (event) => { if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") { event.preventDefault(); $("#paper-search").focus(); } });
initialize();

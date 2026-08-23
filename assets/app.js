const I18N = {
  en: {
    skip: "Skip to research workbench", navWorkbench: "Workbench", navDirections: "Research map", navPolicy: "Method", readingList: "Reading list",
    eyebrow: "Conference + arXiv census · updated 2026-08-23", heroLineOne: "Research the field.", heroLineTwo: "Not the feed.",
    heroLead: "A bilingual, source-aware workbench connecting a five-year top-conference census with a systematic three-year arXiv layer and an auditable three-level research taxonomy.",
    openWorkbench: "Open research workbench", browseMarkdown: "Browse Markdown index", heroNote: "Two explicit layers: formal conference provenance and recent arXiv preprints. Duplicate titles are resolved in the combined view, never used to imply acceptance.",
    scope: "Research corpus", audited: "AUDITED", papers: "papers", researchRecords: "unique research records", conferencePapers: "conference papers", arxivPapers: "arXiv 2023–2026", arxivCandidates: "arXiv candidates audited", venues: "major venues", tracks: "research tracks", subfields: "level-2 subfields", specialties: "level-3 specialties", linked: "source linked",
    workbenchKicker: "Research workbench", catalogTitle: "Move from a direction to its complete research layer.", catalogLead: "Enter any direction directly, switch between conference and arXiv evidence, save a reading list, and export the exact view you are using.",
    allPapers: "All papers", savedPapers: "Reading list", shareView: "Share view", filters: "Filters", reset: "Reset",
    corpus: "Research layer", combined: "Combined unique", conference: "Conference census", recentArxiv: "Recent arXiv", unique: "unique",
    searchPlaceholder: "Search title, author, field, specialty, topic, venue", sort: "Sort order", sortLatest: "Latest first", sortOldest: "Oldest first", sortTitle: "Title A–Z",
    year: "Year", venue: "Venue", track: "Research track", subcategory: "Subfield · Level 2", specialty: "Specialty · Level 3", chooseTrack: "Select a research track to reveal its subfields.", chooseSubcategory: "Select a subfield to reveal its specialties.", sourceTier: "Source tier", all: "All", results: "matching papers", showing: "showing", loadMore: "Load 120 more",
    official: "Official", publisher: "Publisher", index: "Index", arxiv: "arXiv", paper: "Paper", abstract: "Abstract", source: "Source", pdf: "PDF", code: "Code", leafCatalog: "Leaf catalog", save: "Save paper", remove: "Remove from reading list",
    emptyTitle: "No papers match this view.", emptyLead: "Broaden the filters or return to the complete catalog.", exportNote: "Exports include authors when supplied by arXiv; unavailable conference-author metadata is never inferred.",
    directionKicker: "Research map", directionTitle: "Seven directions. Forty subfields. Two hundred paper destinations.", directionLead: "Expand any level-2 subfield to inspect its level-3 specialties, then open the papers assigned to that exact taxonomy path.",
    pipeline: "Research pipeline", subfieldMap: "Level-2 → level-3 map", specialtyCount: "leaf catalogs", conferenceLayer: "Conference", arxivLayer: "arXiv 3 years", openConference: "Open conference papers", openArxiv: "Open recent arXiv",
    policyKicker: "Census contract", policyTitle: "Transparent enough to inspect. Stable enough to reproduce.", policyLead: "Completeness is measured against published operational boundaries—not an undefined claim to every paper anyone might call Embodied AI.", readMethod: "Read the full methodology",
    policyOneTitle: "Two explicit windows", policyOneBody: "Conference years 2022–2026; arXiv submissions from 2023-08-23 through 2026-08-23.",
    policyTwoTitle: "Reproducible discovery", policyTwoBody: "Ten conference indexes are paired with a complete arXiv cs.RO candidate harvest.",
    policyThreeTitle: "Deterministic classification", policyThreeBody: "Published rules assign one auditable direction → subfield → specialty path; unsupported fine-grained claims remain General / Cross-cutting.",
    policyFourTitle: "Separated provenance", policyFourBody: "Official, publisher, index, and arXiv records remain visibly distinct; preprints are never presented as acceptances.",
    footerLine: "Open infrastructure for rigorous literature work.", contribute: "Contribute", copied: "Shareable view copied", saved: "Added to reading list", removed: "Removed from reading list",
    markdownExported: "Markdown exported", csvExported: "CSV exported", columnPaper: "Paper", columnYear: "Year", columnVenue: "Venue", columnSource: "Provenance", columnActions: "Links"
  },
  zh: {
    skip: "跳转到科研工作台", navWorkbench: "科研工作台", navDirections: "研究地图", navPolicy: "方法", readingList: "阅读清单",
    eyebrow: "顶会 + arXiv 系统普查 · 更新于 2026-08-23", heroLineOne: "研究整个领域。", heroLineTwo: "不被信息流裹挟。",
    heroLead: "面向科研工作者的双语、来源透明工作台，连接近五年顶会普查、近三年 arXiv 论文层与可审计的三级研究分类。",
    openWorkbench: "进入科研工作台", browseMarkdown: "浏览 Markdown 索引", heroNote: "顶会录用来源与 arXiv 预印本严格分层；合并视图按标题去重，不会把预印本重复误写成录用证据。",
    scope: "科研语料库", audited: "已审计", papers: "篇论文", researchRecords: "条去重研究记录", conferencePapers: "篇顶会论文", arxivPapers: "篇 arXiv 近三年论文", arxivCandidates: "条 arXiv 候选已审计", venues: "个主要顶会", tracks: "条一级方向", subfields: "个二级子领域", specialties: "个三级专题", linked: "来源已链接",
    workbenchKicker: "科研工作台", catalogTitle: "从研究方向，直接进入完整论文层。", catalogLead: "直接打开任一方向，在顶会与 arXiv 证据间切换，保存阅读清单，并导出正在使用的精确视图。",
    allPapers: "全部论文", savedPapers: "阅读清单", shareView: "分享视图", filters: "筛选条件", reset: "重置",
    corpus: "研究层", combined: "合并去重", conference: "顶会普查", recentArxiv: "近三年 arXiv", unique: "条去重",
    searchPlaceholder: "搜索标题、作者、方向、专题、主题或会议", sort: "排序方式", sortLatest: "最新优先", sortOldest: "最早优先", sortTitle: "标题 A–Z",
    year: "年份", venue: "会议", track: "一级研究方向", subcategory: "二级子领域", specialty: "三级研究专题", chooseTrack: "请先选择一级研究方向，再查看二级子领域。", chooseSubcategory: "请选择二级子领域，再查看三级专题。", sourceTier: "来源层级", all: "全部", results: "篇匹配论文", showing: "当前显示", loadMore: "再加载 120 篇",
    official: "官方", publisher: "出版社", index: "文献索引", arxiv: "arXiv", paper: "论文", abstract: "摘要页", source: "来源", pdf: "PDF", code: "代码", leafCatalog: "最细目录", save: "加入阅读清单", remove: "从阅读清单移除",
    emptyTitle: "当前视图没有匹配论文。", emptyLead: "请放宽筛选条件，或返回完整目录。", exportNote: "arXiv 提供作者时会随结果导出；顶会层缺失的作者信息不会被推测或补造。",
    directionKicker: "研究地图", directionTitle: "七个一级方向，四十个二级子领域，两百个论文落点。", directionLead: "展开任一二级子领域即可查看三级专题，并直接打开精确归入该路径的论文。",
    pipeline: "研究流程", subfieldMap: "二级 → 三级分类图", specialtyCount: "个最细目录", conferenceLayer: "顶会", arxivLayer: "arXiv 近三年", openConference: "打开顶会论文", openArxiv: "打开近三年 arXiv",
    policyKicker: "普查契约", policyTitle: "足够透明以供审查，足够稳定以便复现。", policyLead: "完整性以公开的操作性边界衡量，而不是声称覆盖所有人可能称为具身智能的论文。", readMethod: "阅读完整方法",
    policyOneTitle: "两个明确窗口", policyOneBody: "顶会年份为 2022–2026；arXiv 原始提交日期为 2023-08-23 至 2026-08-23。",
    policyTwoTitle: "可复现发现", policyTwoBody: "十个固定顶会索引与 arXiv cs.RO 全部候选收集并行维护。",
    policyThreeTitle: "确定性分类", policyThreeBody: "公开规则为每篇论文分配“方向 → 子领域 → 专题”路径；证据不足时诚实保留为“综合与交叉研究”。",
    policyFourTitle: "来源严格分层", policyFourBody: "官方、出版社、文献索引与 arXiv 始终分别显示；预印本不会被包装成顶会录用。",
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
const normalizedTitle = (title) => String(title).toLocaleLowerCase().replaceAll("π", "pi").replace(/[^a-z0-9]+/g, " ").trim();
const slugify = (value) => String(value).toLocaleLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

function loadSaved() {
  try {
    const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    return new Set(Array.isArray(stored) ? stored : []);
  } catch (_) {
    return new Set();
  }
}

const state = {
  conferencePapers: [], arxivPapers: [], papers: [], catalog: null, arxivCatalog: null,
  language: localStorage.getItem("language") || "en", corpus: "all",
  year: "all", venue: "all", track: "all", subcategory: "all", specialty: "all", source: "all", query: "", sort: "latest",
  view: "all", visible: PAGE_SIZE, saved: loadSaved()
};

function number(value) {
  return new Intl.NumberFormat(state.language === "zh" ? "zh-CN" : "en-US").format(value);
}

function trackName(track) {
  if (state.language === "zh" && state.catalog?.track_meta?.[track]) return state.catalog.track_meta[track].name_zh;
  return track;
}

function trackTaxonomy(track) {
  return state.catalog?.taxonomy?.tracks?.[track]?.subcategories || {};
}

function subcategoryName(track, subcategory) {
  const meta = trackTaxonomy(track)[subcategory];
  return state.language === "zh" && meta?.name_zh ? meta.name_zh : subcategory;
}

function specialtyName(track, subcategory, specialty) {
  const meta = trackTaxonomy(track)[subcategory]?.specialties?.[specialty];
  return state.language === "zh" && meta?.name_zh ? meta.name_zh : specialty;
}

function sourceName(sourceType) {
  if (sourceType === "publisher") return label("publisher");
  if (sourceType === "bibliographic") return label("index");
  if (sourceType === "arxiv") return label("arxiv");
  return label("official");
}

function taxonomyHref(paper, depth = 3) {
  const params = new URLSearchParams({ corpus: paper.corpus, track: paper.track, lang: state.language });
  if (depth >= 2) params.set("subcategory", paper.subcategory);
  if (depth >= 3) params.set("specialty", paper.specialty);
  return `?${params.toString()}#research-workbench`;
}

function leafCatalogHref(paper) {
  return `papers/taxonomy/${slugify(paper.track)}/${slugify(paper.subcategory)}/${slugify(paper.specialty)}/`;
}

function counts(items, field) {
  return items.reduce((map, item) => map.set(item[field], (map.get(item[field]) || 0) + 1), new Map());
}

function combinedUniquePapers() {
  const seen = new Set();
  const combined = [];
  for (const paper of [...state.conferencePapers, ...state.arxivPapers]) {
    const key = normalizedTitle(paper.title);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    combined.push(paper);
  }
  return combined;
}

function basePapers() {
  if (state.corpus === "conference") return state.conferencePapers;
  if (state.corpus === "arxiv") return state.arxivPapers;
  return state.papers;
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
  const totalLayerRecords = state.conferencePapers.length + state.arxivPapers.length;
  const sourceCounts = counts([...state.conferencePapers, ...state.arxivPapers], "source_type");
  $("#paper-count").textContent = number(state.papers.length);
  $("#conference-count").textContent = number(state.conferencePapers.length);
  $("#arxiv-count").textContent = number(state.arxivPapers.length);
  $("#venue-count").textContent = number(state.catalog.venues.length);
  $("#track-count").textContent = number(state.catalog.tracks.length);
  $("#subcategory-count").textContent = number(state.catalog.taxonomy.subcategory_count);
  $("#specialty-count").textContent = number(state.catalog.taxonomy.specialty_count);
  $("#scope-provenance").innerHTML = ["official", "publisher", "bibliographic", "arxiv"].map((type) => {
    const count = sourceCounts.get(type) || 0;
    const width = Math.max(2, count / totalLayerRecords * 100);
    return `<div><span><i class="tier-dot ${type}"></i>${sourceName(type)}</span><strong>${number(count)}</strong><b><i class="${type}" style="width:${width}%"></i></b></div>`;
  }).join("");

  const conferenceCounts = counts(state.conferencePapers, "track");
  const arxivCounts = counts(state.arxivPapers, "track");
  $("#track-ticker").innerHTML = state.catalog.tracks.map((track) => `<button type="button" data-direction="${escapeHtml(track)}" data-corpus="all"><strong title="${escapeHtml(trackName(track))}">${escapeHtml(trackName(track))}</strong><span>${number(conferenceCounts.get(track) || 0)} ${label("conferenceLayer")} · ${number(arxivCounts.get(track) || 0)} arXiv</span></button>`).join("");
}

function renderDirections() {
  const years = Array.from({ length: state.catalog.window.end - state.catalog.window.start + 1 }, (_, index) => state.catalog.window.start + index);
  $("#direction-grid").innerHTML = state.catalog.tracks.map((track, index) => {
    const meta = state.catalog.track_meta[track];
    const conferencePapers = state.conferencePapers.filter((paper) => paper.track === track);
    const arxivPapers = state.arxivPapers.filter((paper) => paper.track === track);
    const paperYears = new Set(conferencePapers.map((paper) => paper.year));
    const stages = state.language === "zh" ? meta.pipeline_zh : meta.pipeline;
    const question = state.language === "zh" ? meta.question_zh : meta.question;
    const taxonomy = trackTaxonomy(track);
    const subcategories = Object.keys(taxonomy);
    const combined = [...conferencePapers, ...arxivPapers];
    const subcategoryCounts = counts(combined, "subcategory");
    return `<article class="direction-card">
      <div class="direction-card-top"><span>0${index + 1}</span><div class="year-coverage">${years.map((year) => `<i class="${paperYears.has(year) ? "covered" : ""}">${year}</i>`).join("")}</div></div>
      <h3>${escapeHtml(trackName(track))}</h3>
      <p>${escapeHtml(question)}</p>
      <div class="direction-layer-stats"><span>${label("conferenceLayer")}<strong>${number(conferencePapers.length)}</strong><small>2022–2026</small></span><span>${label("arxivLayer")}<strong>${number(arxivPapers.length)}</strong><small>2023–2026</small></span></div>
      <div class="pipeline"><span>${label("pipeline")}</span><ol>${stages.map((stage) => `<li>${escapeHtml(stage)}</li>`).join("")}</ol></div>
      <div class="direction-subfields"><span>${label("subfieldMap")}</span><div>${subcategories.map((subcategory) => {
        const subfieldPapers = combined.filter((paper) => paper.subcategory === subcategory);
        const specialtyCounts = counts(subfieldPapers, "specialty");
        const specialties = Object.keys(taxonomy[subcategory].specialties);
        return `<details class="direction-subfield">
          <summary><b>${escapeHtml(subcategoryName(track, subcategory))}</b><small>${number(subcategoryCounts.get(subcategory) || 0)} · ${specialties.length} ${label("specialtyCount")}</small></summary>
          <div class="direction-specialties">${specialties.map((specialty) => `<button type="button" data-direction="${escapeHtml(track)}" data-subcategory="${escapeHtml(subcategory)}" data-specialty="${escapeHtml(specialty)}" data-corpus="all"><b>${escapeHtml(specialtyName(track, subcategory, specialty))}</b><small>${number(specialtyCounts.get(specialty) || 0)}</small></button>`).join("")}</div>
        </details>`;
      }).join("")}</div></div>
      <div class="direction-actions"><button type="button" data-direction="${escapeHtml(track)}" data-corpus="conference">${label("openConference")} <span aria-hidden="true">→</span></button><button type="button" data-direction="${escapeHtml(track)}" data-corpus="arxiv">${label("openArxiv")} <span aria-hidden="true">→</span></button></div>
    </article>`;
  }).join("");
}

function chip(value, text, active, type, count) {
  const suffix = Number.isFinite(count) ? `<small>${number(count)}</small>` : "";
  return `<button class="filter-chip" type="button" data-filter="${type}" data-value="${escapeHtml(value)}" aria-pressed="${active}"><span>${escapeHtml(text)}</span>${suffix}</button>`;
}

function renderFilters() {
  const universe = basePapers();
  const years = Array.from(new Set(universe.map((paper) => paper.year))).sort((a, b) => b - a);
  const venues = Array.from(new Set(universe.map((paper) => paper.venue))).sort((a, b) => {
    const left = state.catalog.venues.indexOf(a);
    const right = state.catalog.venues.indexOf(b);
    return (left < 0 ? 99 : left) - (right < 0 ? 99 : right);
  });
  const yearCounts = counts(universe, "year");
  const venueCounts = counts(universe, "venue");
  const trackCounts = counts(universe, "track");
  const sourceCounts = counts(universe, "source_type");
  const subcategories = state.track === "all" ? [] : Object.keys(trackTaxonomy(state.track));
  if (state.subcategory !== "all" && !subcategories.includes(state.subcategory)) {
    state.subcategory = "all";
    state.specialty = "all";
  }
  const subcategoryUniverse = state.track === "all" ? [] : universe.filter((paper) => paper.track === state.track);
  const subcategoryCounts = counts(subcategoryUniverse, "subcategory");
  const specialties = state.subcategory === "all"
    ? []
    : Object.keys(trackTaxonomy(state.track)[state.subcategory]?.specialties || {});
  if (state.specialty !== "all" && !specialties.includes(state.specialty)) state.specialty = "all";
  const specialtyUniverse = state.subcategory === "all"
    ? []
    : subcategoryUniverse.filter((paper) => paper.subcategory === state.subcategory);
  const specialtyCounts = counts(specialtyUniverse, "specialty");
  $("#corpus-filters").innerHTML = [
    chip("all", label("combined"), state.corpus === "all", "corpus", state.papers.length),
    chip("conference", label("conference"), state.corpus === "conference", "corpus", state.conferencePapers.length),
    chip("arxiv", label("recentArxiv"), state.corpus === "arxiv", "corpus", state.arxivPapers.length)
  ].join("");
  $("#year-filters").innerHTML = chip("all", label("all"), state.year === "all", "year", universe.length) + years.map((year) => chip(year, year, String(state.year) === String(year), "year", yearCounts.get(year))).join("");
  $("#venue-filters").innerHTML = chip("all", label("all"), state.venue === "all", "venue", universe.length) + venues.map((venue) => chip(venue, venue, state.venue === venue, "venue", venueCounts.get(venue))).join("");
  $("#track-filters").innerHTML = chip("all", label("all"), state.track === "all", "track", universe.length) + state.catalog.tracks.map((track) => chip(track, trackName(track), state.track === track, "track", trackCounts.get(track) || 0)).join("");
  $("#subcategory-filters").innerHTML = state.track === "all"
    ? `<p class="filter-hint">${label("chooseTrack")}</p>`
    : chip("all", label("all"), state.subcategory === "all", "subcategory", subcategoryUniverse.length) + subcategories.map((subcategory) => chip(subcategory, subcategoryName(state.track, subcategory), state.subcategory === subcategory, "subcategory", subcategoryCounts.get(subcategory) || 0)).join("");
  $("#specialty-filters").innerHTML = state.subcategory === "all"
    ? `<p class="filter-hint">${label("chooseSubcategory")}</p>`
    : chip("all", label("all"), state.specialty === "all", "specialty", specialtyUniverse.length) + specialties.map((specialty) => chip(specialty, specialtyName(state.track, state.subcategory, specialty), state.specialty === specialty, "specialty", specialtyCounts.get(specialty) || 0)).join("");
  const sourceTypes = ["official", "publisher", "bibliographic", "arxiv"].filter((type) => sourceCounts.has(type));
  $("#source-type-filters").innerHTML = chip("all", label("all"), state.source === "all", "source", universe.length) + sourceTypes.map((type) => chip(type, sourceName(type), state.source === type, "source", sourceCounts.get(type))).join("");
  document.querySelectorAll("[data-view]").forEach((button) => { button.setAttribute("aria-pressed", String(button.dataset.view === state.view)); });
  $("#sort-select").value = state.sort;
}

function filteredPapers() {
  const query = state.query.trim().toLocaleLowerCase();
  const items = basePapers().filter((paper) => {
    const authors = (paper.authors || []).join(" ");
    const haystack = `${paper.title} ${authors} ${paper.topic} ${paper.track} ${paper.subcategory} ${paper.specialty} ${paper.venue}`.toLocaleLowerCase();
    return (state.view === "all" || state.saved.has(paperKey(paper))) &&
      (state.year === "all" || String(paper.year) === String(state.year)) &&
      (state.venue === "all" || paper.venue === state.venue) &&
      (state.track === "all" || paper.track === state.track) &&
      (state.subcategory === "all" || paper.subcategory === state.subcategory) &&
      (state.specialty === "all" || paper.specialty === state.specialty) &&
      (state.source === "all" || paper.source_type === state.source) &&
      (!query || haystack.includes(query));
  });
  return items.sort((a, b) => {
    if (state.sort === "oldest") return a.year - b.year || a.title.localeCompare(b.title);
    if (state.sort === "title") return a.title.localeCompare(b.title);
    const dateA = a.published || `${a.year}-12-31`;
    const dateB = b.published || `${b.year}-12-31`;
    return dateB.localeCompare(dateA) || a.title.localeCompare(b.title);
  });
}

function renderSavedCounts() {
  $("#saved-count").textContent = number(state.saved.size);
  $("#toolbar-saved-count").textContent = number(state.saved.size);
}

function renderPapers() {
  const items = filteredPapers();
  const visibleItems = items.slice(0, state.visible);
  $("#result-count").textContent = number(items.length);
  $("#showing-count").textContent = number(visibleItems.length);
  $("#load-more").hidden = visibleItems.length >= items.length;
  $("#load-more").textContent = label("loadMore");
  $("#empty-state").hidden = items.length !== 0;
  const header = `<div class="paper-table-head" role="row"><span role="columnheader" aria-label="Reading list"></span><span role="columnheader">${label("columnPaper")}</span><span role="columnheader">${label("columnYear")}</span><span role="columnheader">${label("columnVenue")}</span><span role="columnheader">${label("columnSource")}</span><span role="columnheader">${label("columnActions")}</span></div>`;
  const rows = visibleItems.map((paper) => {
    const key = paperKey(paper);
    const saved = state.saved.has(key);
    const authors = paper.authors?.length ? `<i>·</i><span class="paper-authors">${escapeHtml(paper.authors.slice(0, 5).join(", "))}${paper.authors.length > 5 ? " et al." : ""}</span>` : "";
    const taxonomy = `<a href="${escapeHtml(taxonomyHref(paper, 1))}">${escapeHtml(trackName(paper.track))}</a><i>›</i><a href="${escapeHtml(taxonomyHref(paper, 2))}">${escapeHtml(subcategoryName(paper.track, paper.subcategory))}</a><i>›</i><a href="${escapeHtml(taxonomyHref(paper, 3))}">${escapeHtml(specialtyName(paper.track, paper.subcategory, paper.specialty))}</a>`;
    const code = paper.code_url ? `<a href="${escapeHtml(paper.code_url)}" target="_blank" rel="noopener">${label("code")} ↗</a>` : "";
    const links = paper.source_type === "arxiv"
      ? `<a class="primary-link" href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener">${label("abstract")} ↗</a><a href="${escapeHtml(paper.pdf_url)}" target="_blank" rel="noopener">${label("pdf")} ↗</a>`
      : `<a class="primary-link" href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener">${label("paper")} ↗</a><a href="${escapeHtml(paper.official_url)}" target="_blank" rel="noopener">${label("source")} ↗</a>${code}`;
    return `<article class="paper-row" role="row">
      <div role="cell"><button class="save-button" type="button" data-save-key="${escapeHtml(key)}" aria-pressed="${saved}" aria-label="${escapeHtml(saved ? label("remove") : label("save"))}" title="${escapeHtml(saved ? label("remove") : label("save"))}"><span aria-hidden="true">${saved ? "●" : "○"}</span></button></div>
      <div class="paper-identity" role="cell"><a href="${escapeHtml(paper.paper_url)}" target="_blank" rel="noopener"><strong>${escapeHtml(paper.title)}</strong></a><span class="paper-taxonomy">${taxonomy}</span><span class="paper-detail">${escapeHtml(paper.topic)}${authors}</span></div>
      <div class="paper-year" role="cell"><span class="mobile-label">${label("year")}</span>${paper.published || paper.year}</div>
      <div class="paper-venue" role="cell"><span class="mobile-label">${label("venue")}</span><strong>${escapeHtml(paper.venue)}</strong></div>
      <div class="paper-source" role="cell"><span class="mobile-label">${label("sourceTier")}</span><a href="${escapeHtml(paper.official_url)}" target="_blank" rel="noopener"><i class="tier-dot ${escapeHtml(paper.source_type)}"></i>${sourceName(paper.source_type)}</a></div>
      <div class="paper-links" role="cell"><a href="${escapeHtml(leafCatalogHref(paper))}">${label("leafCatalog")} ↗</a>${links}</div>
    </article>`;
  }).join("");
  $("#paper-grid").innerHTML = header + rows;
  renderSavedCounts();
}

function renderAll() {
  if (!state.catalog || !state.arxivCatalog) return;
  renderStats();
  renderDirections();
  renderFilters();
  renderPapers();
}

function updateUrl() {
  if (!state.catalog) return;
  const params = new URLSearchParams();
  if (state.corpus !== "all") params.set("corpus", state.corpus);
  if (state.query) params.set("q", state.query);
  if (state.year !== "all") params.set("year", state.year);
  if (state.venue !== "all") params.set("venue", state.venue);
  if (state.track !== "all") params.set("track", state.track);
  if (state.subcategory !== "all") params.set("subcategory", state.subcategory);
  if (state.specialty !== "all") params.set("specialty", state.specialty);
  if (state.source !== "all") params.set("source", state.source);
  if (state.sort !== "latest") params.set("sort", state.sort);
  if (state.view !== "all") params.set("view", state.view);
  if (state.language !== "en") params.set("lang", state.language);
  const query = params.toString();
  history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
}

function readUrlState() {
  const params = new URLSearchParams(location.search);
  const validYears = new Set([...state.conferencePapers, ...state.arxivPapers].map((paper) => String(paper.year)));
  const corpus = params.get("corpus");
  const year = params.get("year");
  const venue = params.get("venue");
  const track = params.get("track");
  const subcategory = params.get("subcategory");
  const specialty = params.get("specialty");
  const source = params.get("source");
  if (["all", "conference", "arxiv"].includes(corpus)) state.corpus = corpus;
  if (year && validYears.has(year)) state.year = year;
  if (venue && [...state.catalog.venues, "arXiv"].includes(venue)) state.venue = venue;
  if (track && state.catalog.tracks.includes(track)) state.track = track;
  if (subcategory && Object.hasOwn(trackTaxonomy(state.track), subcategory)) state.subcategory = subcategory;
  if (specialty && Object.hasOwn(trackTaxonomy(state.track)[state.subcategory]?.specialties || {}, specialty)) state.specialty = specialty;
  if (["official", "publisher", "bibliographic", "arxiv"].includes(source)) state.source = source;
  if (["latest", "oldest", "title"].includes(params.get("sort"))) state.sort = params.get("sort");
  if (["all", "saved"].includes(params.get("view"))) state.view = params.get("view");
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
  Object.assign(state, { corpus: "all", year: "all", venue: "all", track: "all", subcategory: "all", specialty: "all", source: "all", query: "", sort: "latest", view: "all", visible: PAGE_SIZE });
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
    "| Date | Venue | Paper | Authors | Direction | Subfield | Specialty | Topic | Provenance |", "|---|---|---|---|---|---|---|---|---|",
    ...items.map((paper) => `| ${paper.published || paper.year} | ${escapeCell(paper.venue)} | [${escapeCell(paper.title)}](${paper.paper_url}) | ${escapeCell((paper.authors || []).join(", "))} | ${escapeCell(paper.track)} | ${escapeCell(paper.subcategory)} | ${escapeCell(paper.specialty)} | ${escapeCell(paper.topic)} | [${paper.source_type}](${paper.official_url}) |`),
    "", "_Authors are included when supplied by the source; missing metadata is not inferred._", ""
  ];
  downloadFile("embodied-ai-research-view.md", lines.join("\n"), "text/markdown;charset=utf-8");
  showToast(label("markdownExported"));
}

function exportCsv() {
  const quote = (value) => `"${String(value || "").replace(/"/g, '""')}"`;
  const header = ["Title", "Authors", "Date", "Year", "Venue", "Corpus", "Track", "Subfield", "Specialty", "Topic", "Taxonomy Evidence", "Paper URL", "Source URL", "Source Type", "Code URL"];
  const rows = filteredPapers().map((paper) => [paper.title, (paper.authors || []).join("; "), paper.published || "", paper.year, paper.venue, paper.corpus, paper.track, paper.subcategory, paper.specialty, paper.topic, paper.taxonomy_evidence, paper.paper_url, paper.official_url, paper.source_type, paper.code_url || ""]);
  downloadFile("embodied-ai-research-view.csv", `\ufeff${[header, ...rows].map((row) => row.map(quote).join(",")).join("\r\n")}`, "text/csv;charset=utf-8");
  showToast(label("csvExported"));
}

async function shareView() {
  updateUrl();
  try {
    await navigator.clipboard.writeText(location.href);
  } catch (_) {
    const input = document.createElement("textarea");
    input.value = location.href;
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
    const [conferenceResponse, arxivResponse] = await Promise.all([fetch("data/papers.json"), fetch("data/arxiv_recent.json")]);
    if (!conferenceResponse.ok || !arxivResponse.ok) throw new Error(`HTTP ${conferenceResponse.status}/${arxivResponse.status}`);
    state.catalog = await conferenceResponse.json();
    state.arxivCatalog = await arxivResponse.json();
    state.conferencePapers = state.catalog.papers.map((paper) => ({ ...paper, corpus: "conference" }));
    state.arxivPapers = state.arxivCatalog.papers.map((paper) => ({ ...paper, corpus: "arxiv" }));
    state.papers = combinedUniquePapers();
    readUrlState();
    applyLanguage();
  } catch (error) {
    $("#paper-grid").innerHTML = `<div class="empty-state"><strong>Catalog unavailable</strong><p>${escapeHtml(error.message)}</p></div>`;
  }
}

document.addEventListener("click", (event) => {
  const directionButton = event.target.closest("[data-direction]");
  if (directionButton) {
    Object.assign(state, { corpus: directionButton.dataset.corpus || "all", track: directionButton.dataset.direction, subcategory: directionButton.dataset.subcategory || "all", specialty: directionButton.dataset.specialty || "all", year: "all", venue: "all", source: "all", query: "", view: "all", visible: PAGE_SIZE });
    $("#paper-search").value = "";
    renderFilters();
    renderPapers();
    updateUrl();
    $("#research-workbench").scrollIntoView({ behavior: "smooth", block: "start" });
    return;
  }
  const chipButton = event.target.closest("[data-filter]");
  if (chipButton) {
    const filter = chipButton.dataset.filter;
    state[filter] = chipButton.dataset.value;
    if (filter === "corpus") Object.assign(state, { year: "all", venue: "all", source: "all" });
    if (filter === "track") Object.assign(state, { subcategory: "all", specialty: "all" });
    if (filter === "subcategory") state.specialty = "all";
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

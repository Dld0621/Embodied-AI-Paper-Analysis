const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const root = path.resolve(__dirname, "..");
const catalog = JSON.parse(fs.readFileSync(path.join(root, "data/papers.json"), "utf8"));
const arxiv = JSON.parse(fs.readFileSync(path.join(root, "data/arxiv_recent.json"), "utf8"));
test("entry HTML loads the facet helper before the app and provides facet containers", () => {
  const html = fs.readFileSync(path.join(root, "index.html"), "utf8");
  const helper = html.indexOf('<script src="assets/taxonomy-filters.js" defer>');
  const app = html.indexOf('<script src="assets/app.js" defer>');
  assert(helper >= 0 && helper < app);
  assert(html.includes('id="facet-filters"'));
  assert(html.includes('id="track-count">9'));
  assert(html.includes('id="specialty-count">126'));
});

async function workbench(search = "") {
  const nodes = new Map();
  const node = (selector) => {
    if (!nodes.has(selector)) nodes.set(selector, { textContent: "", innerHTML: "", value: "", hidden: false, dataset: {},
      addEventListener() {}, setAttribute() {}, scrollIntoView() {}, click() {}, remove() {} });
    return nodes.get(selector);
  };
  const context = vm.createContext({
    URLSearchParams, Intl, Set, Map, Object, Array, String, Number, Promise, Date,
    setTimeout, clearTimeout,
    localStorage: { getItem() { return null; }, setItem() {} },
    location: { search, pathname: "/", hash: "" },
    history: { replaceState(_a, _b, url) { context.lastUrl = url; } },
    window: { matchMedia() { return { matches: false }; } },
    document: { documentElement: { dataset: {} }, querySelector: node, querySelectorAll() { return []; },
      addEventListener() {}, activeElement: { tagName: "BODY" } },
    fetch: async (url) => ({ ok: true, json: async () => url.includes("arxiv") ? arxiv : catalog }),
  });
  vm.runInContext(fs.readFileSync(path.join(root, "assets/taxonomy-filters.js"), "utf8"), context);
  vm.runInContext(fs.readFileSync(path.join(root, "assets/app.js"), "utf8"), context);
  await new Promise(setImmediate);
  assert(!node("#paper-grid").innerHTML.includes("Catalog unavailable"));
  return { context, node, run: (code) => vm.runInContext(code, context) };
}

test("real catalog initializes and resolves bilingual nine-direction navigation", async () => {
  const app = await workbench("?lang=zh");
  assert.equal(app.run("state.papers.length"), 27637);
  assert.equal(app.node("#track-count").textContent, "9");
  assert(app.node("#direction-grid").innerHTML.includes("世界模型"));
  assert(app.node("#facet-filters").innerHTML.includes("关联主题（跨分类）"));
  assert(app.node("#paper-grid").innerHTML.includes("paper-annotations"));
});

test("shared cross-topic filter finds SPIDER with its unique hand primary path", async () => {
  const params = new URLSearchParams({ related_topics: "Hand Retargeting", q: "SPIDER" });
  const app = await workbench("?" + params);
  assert.equal(app.run("filteredPapers().length"), 1);
  assert.equal(app.run("filteredPapers()[0].subcategory"), "Dexterous Hand Retargeting");
  assert.equal(app.run("filteredPapers()[0].specialty"), "Physics & Dynamics Retargeting");
  assert(app.context.lastUrl.includes("related_topics=Hand+Retargeting"));
  app.run('state.related_topics = "Whole-body Retargeting"; renderPapers(); updateUrl();');
  assert.equal(app.run("filteredPapers().length"), 1);
  assert(app.context.lastUrl.includes("Whole-body"));
  app.run("clearFilters()");
  assert.equal(app.run("state.related_topics"), "all");
  assert.equal(app.run("filteredPapers().length"), 27637);
});

test("invalid URL facets are ignored and review filter isolates pending records", async () => {
  const app = await workbench("?method_tags=not-a-real-tag&classification_status=needs-review&lang=zh");
  assert.equal(app.run("state.method_tags"), "all");
  assert(app.run("filteredPapers().length") > 0);
  assert(app.run('filteredPapers().every(p => p.classification_status === "needs-review")'));
  assert(!app.context.lastUrl.includes("not-a-real-tag"));
});

test("both exports preserve review evidence, tags and source provenance", async () => {
  const app = await workbench("?q=DexMachina");
  app.run("globalThis.exportsCaptured = []; downloadFile = (name, contents) => exportsCaptured.push({name, contents}); exportMarkdown(); exportCsv();");
  const outputs = app.run("exportsCaptured");
  assert.equal(outputs.length, 2);
  for (const output of outputs) {
    assert(output.contents.includes("DexMachina"));
    assert(output.contents.includes("Contact & Functional Retargeting"));
    assert(output.contents.includes("reviewed"));
    assert(output.contents.includes("related_topics"));
    assert(output.contents.includes("https://"));
  }
});

test("generic dexterity no longer appears in the retargeting view", async () => {
  const params = new URLSearchParams({ related_topics: "Hand Retargeting", q: "Quantized Hand State" });
  const app = await workbench("?" + params);
  assert.equal(app.run("filteredPapers().length"), 0);
  app.run('state.related_topics = "all"; renderPapers();');
  assert(app.run("filteredPapers().length") > 0);
  assert.equal(app.run("filteredPapers()[0].subcategory"), "Multifinger Grasping & Control");
});

test("provisional subfield is visibly labeled and preserved in exports", async () => {
  const app = await workbench("?q=Learning%20Dexterous%20Manipulation%20with%20Quantized%20Hand%20State&lang=zh");
  assert(app.node("#paper-grid").innerHTML.includes("二级归属暂定"));
  app.run("globalThis.exportsCaptured = []; downloadFile = (name, contents) => exportsCaptured.push({name, contents}); exportMarkdown(); exportCsv();");
  for (const output of app.run("exportsCaptured")) assert(output.contents.includes("provisional"));
});

const test = require("node:test");
const assert = require("node:assert/strict");
const { combine, matches } = require("../assets/taxonomy-filters.js");
test("conference primary is preserved while cross-source tags are merged", () => {
  const first = { title: "SPIDER: Motion", corpus: "conference", track: "Hand", related_topics: ["Hand Retargeting"] };
  const result = combine([first], [{ title: "SPIDER Motion", corpus: "arxiv", track: "Whole body", related_topics: ["Whole-body Retargeting"] }]);
  assert.equal(result.length, 1);
  assert.equal(result[0].track, "Hand");
  assert.equal(result[0].corpus, "conference");
  assert.deepEqual(result[0].related_topics, ["Hand Retargeting", "Whole-body Retargeting"]);
  assert.deepEqual(first.related_topics, ["Hand Retargeting"]);
});
test("cross-topic facets combine with AND and default to unrestricted", () => {
  const p = { method_tags: ["Reinforcement Learning"], related_topics: ["Hand Retargeting"], classification_status: "reviewed" };
  assert(matches(p, {}));
  assert(matches(p, { method_tags: "Reinforcement Learning", related_topics: "Hand Retargeting", classification_status: "reviewed" }));
  assert(!matches(p, { related_topics: "Whole-body Retargeting" }));
  assert(!matches(p, { classification_status: "needs-review" }));
  assert(!matches(p, { data_tags: "Human Video" }));
});

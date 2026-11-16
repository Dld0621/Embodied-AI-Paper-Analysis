/* Shared, testable cross-topic filtering. Primary classification is not duplicated. */
(function (root) {
  const fields = ["method_tags", "embodiment_tags", "data_tags", "related_topics"];
  const key = (title) => String(title).toLowerCase().replaceAll("π", "pi").replace(/[^a-z0-9]+/g, " ").trim();
  function combine(conference, arxiv) {
    const unique = new Map();
    for (const paper of [...conference, ...arxiv]) {
      const title = key(paper.title);
      if (!title) continue;
      if (!unique.has(title)) {
        unique.set(title, { ...paper, ...Object.fromEntries(fields.map((field) => [field, [...(paper[field] || [])]])) });
      } else {
        const existing = unique.get(title);
        for (const field of fields) existing[field] = [...new Set([...existing[field], ...(paper[field] || [])])].sort();
      }
    }
    return [...unique.values()];
  }
  function matches(paper, filters) {
    return fields.every((field) => !filters[field] || filters[field] === "all" || (paper[field] || []).includes(filters[field])) &&
      (!filters.classification_status || filters.classification_status === "all" || paper.classification_status === filters.classification_status);
  }
  const api = { fields, combine, matches };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.TaxonomyFilters = api;
})(typeof globalThis !== "undefined" ? globalThis : this);

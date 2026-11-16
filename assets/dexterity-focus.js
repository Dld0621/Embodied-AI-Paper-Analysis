/* Read-only focused catalog. The full source layers and their admission remain unchanged. */
(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const PAGE_SIZE = 60;
  const tierNames = {
    reviewed:'重点核查',
    'strong-candidate':'自动强匹配',
    'broad-candidate':'宽泛匹配待复核',
  };
  const tierOrder = {reviewed:0,'strong-candidate':1,'broad-candidate':2};
  const sourceNames = {official:'官方来源',publisher:'出版方来源',bibliographic:'文献索引',arxiv:'arXiv 预印本'};
  const state = {data:null, group:'all', tier:'all', source:'all', query:'', visible:PAGE_SIZE};
  const escape = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  const safeUrl = value => {
    try { const url = new URL(String(value)); return url.protocol === 'https:' ? url.href : ''; }
    catch { return ''; }
  };
  const format = value => Number(value || 0).toLocaleString('en-US');
  const normal = value => String(value || '').toLocaleLowerCase().replace(/[^a-z0-9\u3400-\u9fff]+/g, ' ').trim();
  const variants = paper => Array.isArray(paper.source_variants) ? paper.source_variants : [];
  const groupName = slug => state.data.groups.find(group => group.slug === slug)?.name_zh || slug;
  function reviewLabel(value) {
    const text = String(value || '');
    if (!text) return '';
    if (/automat|metadata|rule.derived/i.test(text)) return '自动检索与元数据匹配，待人工复核';
    if (/selected.*method|method.*section/i.test(text)) return '标题、摘要与部分方法章节核查，未独立复现实验';
    if (/title.*abstract/i.test(text)) return '标题与摘要核查；部分所列官方材料辅助核对，未复现实验';
    return /[\u3400-\u9fff]/.test(text) ? text : '所列来源与核查记录，详细范围见完整目录；未复现实验';
  }
  function residualLabel(paper) {
    if (!paper.groups.includes('residual') || !paper.residual_role) return '';
    if (/action\/control phrase/i.test(paper.residual_role)) return '命中动作或控制残差相关词；实际修正接口仍需核对原文。';
    if (/representation.or.model/i.test(paper.residual_role)) return '涉及表征或模型残差，不能据此视为动作残差控制。';
    return /not established|not assessed|unknown/i.test(paper.residual_role)
      ? '尚未确认具体作用位置；需核对原文，不能据检索词推断为动作残差。'
      : paper.residual_role;
  }
  function readTheme() {
    try { return localStorage.getItem('theme'); } catch { return null; }
  }
  function setTheme(theme) {
    document.documentElement.dataset.theme = theme;
    $('#focus-theme').setAttribute('aria-pressed', String(theme === 'dark'));
    try { localStorage.setItem('theme', theme); } catch {}
  }
  setTheme(readTheme() || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  $('#focus-theme').addEventListener('click', () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'));
  function chosen(paper) {
    if (state.group !== 'all' && !paper.groups.includes(state.group)) return false;
    if (state.tier === 'direct' && paper.tier === 'broad-candidate') return false;
    if (!['all','direct'].includes(state.tier) && paper.tier !== state.tier) return false;
    if (state.source !== 'all' && !variants(paper).some(source => source.source_layer === state.source)) return false;
    if (state.query) {
      const fields = [paper.title, paper.why_zh, paper.track, paper.subcategory, paper.specialty,
        paper.residual_role, ...paper.groups.map(groupName), ...variants(paper).flatMap(source => [source.title,source.arxiv_id,source.venue,source.year]),
        ...(paper.evidence || []).map(evidence => evidence.term)];
      const haystack = normal(fields.join(' '));
      if (!normal(state.query).split(/\s+/).filter(Boolean).every(term => haystack.includes(term))) return false;
    }
    return true;
  }
  function sourceLinks(source) {
    const paper = safeUrl(source.paper_url), official = safeUrl(source.official_url);
    return [paper ? `<a href="${escape(paper)}" target="_blank" rel="noopener">论文 ↗</a>` : '',
      official && official !== paper ? `<a href="${escape(official)}" target="_blank" rel="noopener">来源 ↗</a>` : ''].join('');
  }
  function paperHtml(paper) {
    const sources = variants(paper), url = safeUrl(paper.paper_url) || safeUrl(sources[0]?.paper_url);
    const title = url ? `<a href="${escape(url)}" target="_blank" rel="noopener">${escape(paper.title)}</a>` : escape(paper.title);
    const layers = [...new Set(sources.map(source => source.source_layer))];
    const layerLabel = layers.includes('conference') && layers.includes('arxiv') ? '含会议与预印本来源' : layers.includes('conference') ? '会议来源' : '预印本来源';
    const evidence = (paper.evidence || []).slice(0, 8).map(item => `<li><strong>${escape(({title:'标题',abstract:'摘要',taxonomy:'已有分类'})[item.field] || '依据')}</strong>${item.term ? ` · ${escape(item.term)}` : ''}${item.snippet ? `：${escape(item.snippet)}` : ''}</li>`).join('');
    const sourcesHtml = sources.map(source => `<p>${escape(source.venue || (source.source_layer === 'arxiv' ? 'arXiv' : 'Conference'))} ${escape(source.year || '')} · ${escape(sourceNames[source.source_type] || source.source_type || '来源层级未标注')}${source.published ? ` · ${source.source_layer === 'arxiv' ? '原始提交' : '来源日期'} ${escape(source.published)}` : ''}<br>${sourceLinks(source)}</p>`).join('');
    const reviewLinks = [...new Set((paper.review_urls || []).map(safeUrl).filter(Boolean))].slice(0,6).map((url,index) => `<a href="${escape(url)}" target="_blank" rel="noopener">核查材料 ${index+1} ↗</a>`).join('');
    return `<article class="df-paper" data-paper-id="${escape(paper.id)}" data-tier="${escape(paper.tier)}">
      <div class="df-paper-head"><h3>${title}</h3><span class="df-tier df-tier-${escape(paper.tier)}">${escape(tierNames[paper.tier] || paper.tier)}</span></div>
      <p class="df-paper-meta">${escape(paper.year || '')} · ${escape(layerLabel)} · ${escape([paper.track,paper.subcategory,paper.specialty].filter(Boolean).join(' → '))}</p>
      <div class="df-groups">${paper.groups.map(slug => `<span>${escape(groupName(slug))}</span>`).join('')}</div>
      ${paper.why_zh ? `<p class="df-paper-why">${escape(paper.why_zh)}</p>` : ''}
      ${residualLabel(paper) ? `<p class="df-paper-boundary"><strong>残差位置：</strong>${escape(residualLabel(paper))}</p>` : ''}
      ${paper.boundary_zh ? `<p class="df-paper-boundary">${escape(paper.boundary_zh)}</p>` : ''}
      <details><summary>查看筛选依据与来源（${sources.length} 条来源记录）</summary>
        ${paper.review_basis ? `<p class="df-paper-boundary">核查范围：${escape(reviewLabel(paper.review_basis))}。重点核查不等于实验复现或对全部结论背书。</p>` : ''}
        ${evidence ? `<ul class="df-evidence">${evidence}</ul>` : ''}
        <div class="df-source">${sourcesHtml}</div>
        ${reviewLinks ? `<div class="df-source"><p>${reviewLinks}</p></div>` : ''}
      </details>
    </article>`;
  }
  function render() {
    if (!state.data) return;
    const matched = state.data.papers.filter(chosen).sort((a,b) => (tierOrder[a.tier] ?? 9) - (tierOrder[b.tier] ?? 9) || Number(b.year) - Number(a.year) || a.title.localeCompare(b.title));
    const shown = matched.slice(0, state.visible);
    $('#focus-results').innerHTML = shown.length ? shown.map(paperHtml).join('') : '<p class="df-empty">当前条件没有匹配论文。可切换“全部候选”或清除搜索。</p>';
    const tierLabel = $('#focus-tier').selectedOptions[0].textContent;
    $('#focus-result-status').textContent = `${format(matched.length)} 个去重标题符合当前条件 · 已显示 ${format(shown.length)} · 当前为“${tierLabel}” · 全部候选 ${format(state.data.papers.length)} 个`;
    $('#focus-more').hidden = shown.length >= matched.length;
    $('#focus-more').textContent = `继续显示 ${Math.min(PAGE_SIZE, matched.length - shown.length)} 篇`;
    $('#focus-results').dataset.resultCount = String(matched.length);
  }
  function updateUrl() {
    const url = new URL(location.href);
    for (const [key,value] of Object.entries({group:state.group,tier:state.tier,source:state.source,q:state.query})) {
      if (((key === 'group' || key === 'source') && value === 'all') || (key === 'tier' && value === 'all') || !value) url.searchParams.delete(key);
      else url.searchParams.set(key,value);
    }
    history.replaceState(null, '', url);
  }
  function changed() { state.visible = PAGE_SIZE; render(); updateUrl(); }
  function initialFilters() {
    const params = new URLSearchParams(location.search);
    for (const [key,selector] of [['group','#focus-group'],['tier','#focus-tier'],['source','#focus-source']]) {
      const value = params.get(key);
      if (value && [...$(selector).options].some(option => option.value === value)) { state[key] = value; $(selector).value = value; }
    }
    state.query = params.get('q') || ''; $('#focus-search').value = state.query;
  }
  function renderFoundations() {
    const papers = state.data.external_foundations || [];
    $('#focus-foundations-summary').textContent = `展开 ${format(papers.length)} 条库外补充参考（不计入专题候选）`;
    $('#focus-foundations').innerHTML = papers.length ? papers.map(paper => {
      const url = (paper.urls || []).map(safeUrl).find(Boolean), title = url ? `<a href="${escape(url)}" target="_blank" rel="noopener">${escape(paper.title)} ↗</a>` : escape(paper.title);
      return `<article class="df-foundation"><h3>${escape(paper.year || '')} · ${title}</h3><p>${escape(paper.why_zh || '')}</p>${paper.boundary_zh ? `<p>${escape(paper.boundary_zh)}</p>` : ''}${paper.review_basis ? `<p>核查范围：${escape(reviewLabel(paper.review_basis))}</p>` : ''}</article>`;
    }).join('') : '<p class="df-paper-boundary">当前没有库外补充参考。</p>';
  }
  async function initialize() {
    try {
      const response = await fetch('data/dexterous-retargeting-contact.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = await response.json();
      if (!Array.isArray(data.papers) || !Array.isArray(data.groups) || data.papers.some(p => !p.title || !Array.isArray(p.groups) || !tierNames[p.tier])) throw new Error('专题数据结构不完整');
      state.data = data;
      const counts = data.counts || {}, tiers = counts.tier_counts || {};
      const conferenceSources = data.papers.reduce((sum,paper) => sum + variants(paper).filter(v => v.source_layer === 'conference').length,0);
      const arxivSources = data.papers.reduce((sum,paper) => sum + variants(paper).filter(v => v.source_layer === 'arxiv').length,0);
      const overlapTitles = data.papers.filter(paper => ['conference','arxiv'].every(layer => variants(paper).some(v => v.source_layer === layer))).length;
      const groupOptions = data.groups.map(group => `<option value="${escape(group.slug)}">${escape(group.name_zh)} · ${format(counts.group_counts?.[group.slug])}</option>`).join('');
      $('#focus-group').insertAdjacentHTML('beforeend', groupOptions);
      $('#focus-summary').innerHTML = [
        [data.papers.length,'当前库候选 · 标题去重'],[conferenceSources,'会议来源记录'],[arxivSources,'arXiv 来源记录'],[overlapTitles,'同时含两层来源的标题'],[tiers.reviewed,'重点核查'],[tiers['strong-candidate'],'自动强匹配'],[tiers['broad-candidate'],'宽泛匹配待复核'],
      ].map(([value,label]) => `<span><strong>${format(value)}</strong>${escape(label)}</span>`).join('');
      $('#focus-snapshots').textContent = `专题生成：${data.generated_on || '未提供'} · 会议快照：${data.source_snapshots?.conference || '未提供'} · arXiv 快照：${data.source_snapshots?.arxiv || '未提供'} · 标题去重保留全部来源变体`;
      renderFoundations(); initialFilters(); render();
      document.documentElement.dataset.focusReady = 'true';
    } catch (error) {
      $('#focus-snapshots').textContent = '专题数据暂不可用，请稍后重新加载，或打开 GitHub 完整目录。';
      $('#focus-result-status').textContent = '未读取到可核对的专题数据。';
      $('#focus-results').innerHTML = `<p class="df-error">载入失败：${escape(error.message)}。<a href="https://github.com/Dld0621/Embodied-AI-Paper-Analysis/tree/main/papers/focus/dexterous-retargeting-contact">打开 GitHub 目录 ↗</a></p>`;
    }
  }
  $('#focus-controls').addEventListener('submit', event => event.preventDefault());
  $('#focus-search').addEventListener('input', event => { state.query = event.target.value; changed(); });
  for (const [key,selector] of [['group','#focus-group'],['tier','#focus-tier'],['source','#focus-source']]) $(selector).addEventListener('change', event => { state[key] = event.target.value; changed(); });
  $('#focus-reset').addEventListener('click', () => {
    Object.assign(state,{group:'all',tier:'all',source:'all',query:'',visible:PAGE_SIZE});
    $('#focus-search').value = ''; $('#focus-group').value = 'all'; $('#focus-tier').value = 'all'; $('#focus-source').value = 'all'; changed();
  });
  $('#focus-more').addEventListener('click', () => { state.visible += PAGE_SIZE; render(); });
  initialize();
})();

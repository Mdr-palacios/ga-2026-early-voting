/* Georgia 2026 Primary — Early Voting Map (bilingual EN/ES) */
(async function () {
  const svg = d3.select('#ga-map');
  const tooltip = document.getElementById('tooltip');
  const detail = document.getElementById('detail');
  const searchEl = document.getElementById('search');
  const toggleBtn = document.getElementById('lang-toggle');
  const toggleLabel = document.getElementById('lang-toggle-label');

  let selectedName = null;
  let dataByCounty = {};
  let features = null;

  // ---------- Language ----------
  const STORAGE_KEY = 'ga2026_lang';
  function detectInitialLang() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'en' || saved === 'es') return saved;
    const nav = (navigator.language || 'en').toLowerCase();
    return nav.startsWith('es') ? 'es' : 'en';
  }
  let lang = detectInitialLang();
  function t() { return window.I18N[lang]; }

  function applyStaticI18n() {
    const s = t();
    document.documentElement.lang = s.htmlLang;
    document.getElementById('page-title').textContent = s.page_title;
    document.getElementById('h1').textContent = s.h1;
    document.getElementById('subtitle').textContent = s.subtitle;
    document.getElementById('m-election-day').textContent = s.meta_election_day;
    document.getElementById('m-election-day-value').textContent = s.meta_election_day_value;
    document.getElementById('m-early-voting').textContent = s.meta_early_voting;
    document.getElementById('m-early-voting-value').textContent = s.meta_early_voting_value;
    document.getElementById('m-polls-open').textContent = s.meta_polls_open;
    document.getElementById('m-polls-open-value').textContent = s.meta_polls_open_value;
    document.getElementById('m-help-line').textContent = s.meta_help_line;
    document.getElementById('m-help-line-value').textContent = s.meta_help_line_value;

    searchEl.placeholder = s.search_placeholder;
    document.getElementById('lg-has').textContent = s.legend_has_data;
    document.getElementById('lg-no').textContent = s.legend_no_data;
    document.getElementById('lg-sel').textContent = s.legend_selected;
    document.getElementById('ga-map').setAttribute('aria-label', s.map_aria);

    // Footer
    document.getElementById('footer').innerHTML =
      escape(s.footer_text) +
      `<a href="https://mvp.sos.ga.gov" target="_blank" rel="noopener">${escape(s.footer_mvp)}</a>` +
      escape(s.footer_dot) +
      `<a href="https://georgia.gov/vote-early-person" target="_blank" rel="noopener">${escape(s.footer_ga)}</a>`;

    // Toggle button label
    toggleLabel.textContent = s.button_label;
    toggleBtn.setAttribute('aria-label', s.button_aria);
  }

  function setLang(newLang) {
    lang = newLang;
    localStorage.setItem(STORAGE_KEY, lang);
    applyStaticI18n();
    if (selectedName) {
      renderDetail(selectedName, false);
    } else {
      detail.classList.add('empty');
      detail.innerHTML = emptyStateHTML();
    }
  }

  toggleBtn.addEventListener('click', () => {
    setLang(lang === 'en' ? 'es' : 'en');
  });

  // ---------- Load data ----------
  const [topo, voting] = await Promise.all([
    fetch('ga-counties.json').then(r => r.json()),
    fetch('voting-locations.json').then(r => r.json()),
  ]);
  dataByCounty = voting.counties;
  features = topojson.feature(topo, topo.objects['georgia-counties']);

  const path = d3.geoPath().projection(
    d3.geoMercator().fitSize([600, 720], features)
  );

  // ---------- Tooltip ----------
  function showTip(evt, name) {
    const c = dataByCounty[name];
    const s = t();
    const hint = c && !c.placeholder
      ? s.tip_sites(c.locations.length)
      : s.tip_lookup;
    tooltip.querySelector('.name').textContent = name + s.suffix_county;
    tooltip.querySelector('.hint').textContent = hint;
    tooltip.style.left = evt.clientX + 'px';
    tooltip.style.top = evt.clientY + 'px';
    tooltip.classList.add('show');
  }
  function moveTip(evt) {
    tooltip.style.left = evt.clientX + 'px';
    tooltip.style.top = evt.clientY + 'px';
  }
  function hideTip() { tooltip.classList.remove('show'); }

  // ---------- Map ----------
  const g = svg.append('g');
  g.selectAll('path.county')
    .data(features.features)
    .enter()
    .append('path')
    .attr('class', d => {
      const c = dataByCounty[d.properties.NAME];
      return 'county' + (c && !c.placeholder ? ' has-data' : '');
    })
    .attr('d', path)
    .attr('data-name', d => d.properties.NAME)
    .on('mouseenter', function (evt, d) {
      const name = d.properties.NAME;
      showTip(evt, name);
      if (!selectedName) renderDetail(name, true);
    })
    .on('mousemove', moveTip)
    .on('mouseleave', function () {
      hideTip();
      if (!selectedName) {
        detail.classList.add('empty');
        detail.innerHTML = emptyStateHTML();
      }
    })
    .on('click', function (evt, d) {
      selectCounty(d.properties.NAME);
    })
    .append('title')
    .text(d => d.properties.NAME);

  function selectCounty(name) {
    selectedName = name;
    g.selectAll('path.county').classed('selected', d => d.properties.NAME === name);
    renderDetail(name, false);
    detail.scrollTop = 0;
  }

  // ---------- Search ----------
  searchEl.addEventListener('input', () => {
    const q = searchEl.value.trim().toLowerCase();
    if (!q) return;
    const match = features.features.find(f => f.properties.NAME.toLowerCase().startsWith(q));
    if (match) selectCounty(match.properties.NAME);
  });
  searchEl.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      const q = searchEl.value.trim().toLowerCase();
      const match =
        features.features.find(f => f.properties.NAME.toLowerCase() === q) ||
        features.features.find(f => f.properties.NAME.toLowerCase().startsWith(q));
      if (match) selectCounty(match.properties.NAME);
    }
  });

  // ---------- Detail rendering ----------
  function emptyStateHTML() {
    const s = t();
    return `<div class="empty-state">
        <div class="big">${escape(s.empty_title)}</div>
        ${escape(s.empty_body)}
      </div>`;
  }

  function mapsLink(query) {
    return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(query);
  }

  function ballotExplainerHTML() {
    const s = t();
    const offices = (s.ballot_offices || []).map(o => `
      <li>
        <div class="office-name">${escape(o.name)}</div>
        <div class="office-what">${escape(o.what)}</div>
        <div class="office-why">${escape(o.why)}</div>
      </li>`).join('');
    return `
      <details class="ballot-explainer">
        <summary>
          <span class="title">${escape(s.ballot_section)}</span>
          <span class="toggle"><span class="show-text">${escape(s.ballot_show)} ▾</span><span class="hide-text">${escape(s.ballot_hide)} ▴</span></span>
        </summary>
        <div class="body">
          <p class="intro">${escape(s.ballot_intro)}</p>
          <ul class="offices">${offices}</ul>
          <div class="county-note">${escape(s.ballot_county_note)} <a href="https://mvp.sos.ga.gov" target="_blank" rel="noopener">${escape(s.ballot_mvp_link)}</a>.</div>
        </div>
      </details>`;
  }

  function renderDetail(name, ephemeral) {
    const c = dataByCounty[name];
    if (!c) return;
    const s = t();
    detail.classList.remove('empty');

    const tag = c.placeholder
      ? `<span class="county-tag placeholder">${escape(s.tag_county_lookup)}</span>`
      : `<span class="county-tag">${escape(s.tag_sites_listed(c.locations.length))}</span>`;

    let locationsHTML = '';
    if (!c.placeholder && c.locations.length) {
      locationsHTML =
        `<h3 class="section">${escape(s.section_locations)}</h3>` +
        '<ul class="locations">' +
        c.locations.map(([siteName, addr]) => `
          <li>
            <div>
              <div class="name">${escape(siteName)}</div>
              <div class="addr">${escape(addr)}</div>
            </div>
            <a class="map-link" target="_blank" rel="noopener"
               href="${mapsLink(siteName + ', ' + addr)}">${escape(s.directions)}</a>
          </li>
        `).join('') +
        '</ul>';
    }

    let placeholderHTML = '';
    if (c.placeholder) {
      placeholderHTML = `
        <div class="placeholder-note">
          <div class="lead">${escape(s.placeholder_lead(name))}</div>
          ${escape(s.placeholder_body_pre)}${escape(name)}${escape(s.placeholder_body_mid)}<a href="https://mvp.sos.ga.gov/s/advanced-voting-location-information" target="_blank" rel="noopener">${escape(s.placeholder_mvp_link)}</a>${escape(s.placeholder_or)}<a href="https://www.google.com/search?q=${encodeURIComponent(name + ' County GA elections office early voting')}" target="_blank" rel="noopener">${escape(name)}${escape(s.placeholder_search_link_suffix)}</a>.
        </div>`;
    }

    const sourcesHTML = c.sources && c.sources.length
      ? `<div class="sources">${escape(s.sources_label)}` +
        c.sources.map(([n, u]) => `<a href="${escape(u)}" target="_blank" rel="noopener">${escape(n)}</a>`).join(', ') +
        '</div>'
      : '';

    const notesHTML = c.notes ? `<div class="notes">${escape(c.notes)}</div>` : '';

    detail.innerHTML = `
      <div class="county-header">
        <h2>${escape(name)}${escape(s.suffix_county)}</h2>
        ${tag}
      </div>

      <div class="info-row">
        <div class="label">${escape(s.label_hours)}</div>
        <div class="value">${escape(c.hours_summary)}</div>
      </div>
      <div class="info-row">
        <div class="label">${escape(s.label_dates)}</div>
        <div class="value">${escape(c.dates)}</div>
      </div>
      <div class="info-row">
        <div class="label">${escape(s.label_election_day)}</div>
        <div class="value"><b>${escape(s.election_day_full)}</b> ${escape(s.election_day_suffix)}</div>
      </div>

      ${notesHTML}
      ${placeholderHTML}
      ${locationsHTML}

      ${ballotExplainerHTML()}

      <div class="help-banner">
        <b>${escape(s.help_lead)}</b>${escape(s.help_body_pre)}<b>${escape(s.help_phone)}</b>${escape(s.help_phone_suffix)}
        ${escape(s.help_find_polling)}<a href="https://mvp.sos.ga.gov" target="_blank" rel="noopener" style="color:#fff">mvp.sos.ga.gov</a>.
      </div>

      ${sourcesHTML}
    `;
  }

  function escape(s) {
    return String(s).replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
  }

  // ---------- Init ----------
  applyStaticI18n();
  selectCounty('Fulton');
})();

/* Georgia 2026 Primary — Early Voting Map */
(async function () {
  const svg = d3.select('#ga-map');
  const tooltip = document.getElementById('tooltip');
  const detail = document.getElementById('detail');
  const searchEl = document.getElementById('search');

  let selectedName = null;
  let dataByCounty = {};

  // Load topology + voting data in parallel
  const [topo, voting] = await Promise.all([
    fetch('ga-counties.json').then(r => r.json()),
    fetch('voting-locations.json').then(r => r.json()),
  ]);

  dataByCounty = voting.counties;

  const features = topojson.feature(topo, topo.objects['georgia-counties']);

  // Project state into the 600x720 viewBox
  const path = d3.geoPath().projection(
    d3.geoMercator().fitSize([600, 720], features)
  );

  // Tooltip helpers
  function showTip(evt, name) {
    const c = dataByCounty[name];
    const hint = c && !c.placeholder
      ? `${c.locations.length} early voting sites`
      : 'Click for county lookup';
    tooltip.querySelector('.name').textContent = name + ' County';
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

  // Render counties
  const g = svg.append('g');
  g.selectAll('path.county')
    .data(features.features)
    .enter()
    .append('path')
    .attr('class', d => {
      const name = d.properties.NAME;
      const c = dataByCounty[name];
      const hasData = c && !c.placeholder;
      return 'county' + (hasData ? ' has-data' : '');
    })
    .attr('d', path)
    .attr('data-name', d => d.properties.NAME)
    .on('mouseenter', function (evt, d) {
      const name = d.properties.NAME;
      // Hover-driven preview (without persisting selection)
      showTip(evt, name);
      if (!selectedName) renderDetail(name, /*ephemeral*/ true);
    })
    .on('mousemove', moveTip)
    .on('mouseleave', function (evt, d) {
      hideTip();
      if (!selectedName) {
        detail.classList.add('empty');
        detail.innerHTML = emptyStateHTML();
      }
    })
    .on('click', function (evt, d) {
      const name = d.properties.NAME;
      selectCounty(name);
    })
    .append('title')
    .text(d => d.properties.NAME + ' County');

  // Selection
  function selectCounty(name) {
    selectedName = name;
    g.selectAll('path.county').classed('selected', d => d.properties.NAME === name);
    renderDetail(name, false);
    // Keep selected county visible on the small screen
    detail.scrollTop = 0;
  }

  // Search
  searchEl.addEventListener('input', () => {
    const q = searchEl.value.trim().toLowerCase();
    if (!q) return;
    const match = features.features.find(f =>
      f.properties.NAME.toLowerCase().startsWith(q)
    );
    if (match) {
      const name = match.properties.NAME;
      selectCounty(name);
    }
  });
  searchEl.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      const q = searchEl.value.trim().toLowerCase();
      const match = features.features.find(f =>
        f.properties.NAME.toLowerCase() === q
      ) || features.features.find(f =>
        f.properties.NAME.toLowerCase().startsWith(q)
      );
      if (match) selectCounty(match.properties.NAME);
    }
  });

  // ---------- Detail rendering ----------

  function emptyStateHTML() {
    return `
      <div class="empty-state">
        <div class="big">Pick a county</div>
        Hover any county on the map for a quick peek, or click to see full early-voting locations and hours. Six metro Atlanta counties have detailed site lists; all 159 counties link to the official lookup.
      </div>`;
  }

  function mapsLink(query) {
    return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(query);
  }

  function renderDetail(name, ephemeral) {
    const c = dataByCounty[name];
    if (!c) return;

    detail.classList.remove('empty');

    const tag = c.placeholder
      ? '<span class="county-tag placeholder">County lookup</span>'
      : '<span class="county-tag">' + c.locations.length + ' sites listed</span>';

    let locationsHTML = '';
    if (!c.placeholder && c.locations.length) {
      locationsHTML =
        '<h3 class="section">Early voting locations</h3>' +
        '<ul class="locations">' +
        c.locations.map(([siteName, addr]) => `
          <li>
            <div>
              <div class="name">${escape(siteName)}</div>
              <div class="addr">${escape(addr)}</div>
            </div>
            <a class="map-link" target="_blank" rel="noopener"
               href="${mapsLink(siteName + ', ' + addr)}">Directions</a>
          </li>
        `).join('') +
        '</ul>';
    }

    let placeholderHTML = '';
    if (c.placeholder) {
      placeholderHTML = `
        <div class="placeholder-note">
          <div class="lead">No site list available in this dashboard for ${escape(name)} County.</div>
          Detailed site lists are included for the 6 largest metro Atlanta counties.
          For ${escape(name)}, use the official Georgia <a href="https://mvp.sos.ga.gov/s/advanced-voting-location-information" target="_blank" rel="noopener">My Voter Page early-voting lookup</a>
          or search <a href="https://www.google.com/search?q=${encodeURIComponent(name + ' County GA elections office early voting')}" target="_blank" rel="noopener">${escape(name)} County Elections</a>.
        </div>`;
    }

    const sourcesHTML = c.sources && c.sources.length
      ? '<div class="sources">Sources: ' +
        c.sources.map(([n, u]) => `<a href="${escape(u)}" target="_blank" rel="noopener">${escape(n)}</a>`).join(', ') +
        '</div>'
      : '';

    const notesHTML = c.notes ? `<div class="notes">${escape(c.notes)}</div>` : '';

    detail.innerHTML = `
      <div class="county-header">
        <h2>${escape(name)} County</h2>
        ${tag}
      </div>

      <div class="info-row">
        <div class="label">Hours</div>
        <div class="value">${escape(c.hours_summary)}</div>
      </div>
      <div class="info-row">
        <div class="label">Dates</div>
        <div class="value">${escape(c.dates)}</div>
      </div>
      <div class="info-row">
        <div class="label">Election Day</div>
        <div class="value"><b>Tuesday, May 19, 2026</b> · Polls 7a–7p · Vote at your assigned precinct only</div>
      </div>

      ${notesHTML}
      ${placeholderHTML}
      ${locationsHTML}

      <div class="help-banner">
        <b>Need help?</b> Call <b>866-OUR-VOTE</b> (866-687-8683) — free nonpartisan voter help line, English &amp; Spanish.
        Find your assigned polling place at <a href="https://mvp.sos.ga.gov" target="_blank" rel="noopener" style="color:#fff">mvp.sos.ga.gov</a>.
      </div>

      ${sourcesHTML}
    `;
  }

  function escape(s) {
    return String(s).replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[ch]));
  }

  // Default: surface a featured county on first load
  selectCounty('Fulton');
})();

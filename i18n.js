/* Bilingual strings for the GA 2026 early voting dashboard. */
window.I18N = {
  en: {
    htmlLang: 'en',
    page_title: 'Georgia 2026 Primary — Early Voting Locations',
    h1: 'Georgia 2026 Primary — Early Voting Locations',
    subtitle: 'Hover or click any county to see early voting sites, hours, and addresses.',
    meta_election_day: 'Election day:',
    meta_election_day_value: 'Tuesday, May 19, 2026',
    meta_early_voting: 'Early voting:',
    meta_early_voting_value: 'April 27 – May 15',
    meta_polls_open: 'Polls open Election Day:',
    meta_polls_open_value: '7am – 7pm',
    meta_help_line: 'Help line:',
    meta_help_line_value: '866-OUR-VOTE (866-687-8683)',
    search_placeholder: 'Search counties (e.g., Fulton, Bibb, Chatham)…',
    legend_has_data: 'Detailed sites listed',
    legend_no_data: 'Use county lookup',
    legend_selected: 'Selected',
    map_aria: 'Map of Georgia counties',
    empty_title: 'Pick a county',
    empty_body: 'Hover any county on the map for a quick peek, or click to see full early-voting locations and hours. Detailed site lists are included for 54 counties; all 159 counties link to the official lookup.',
    tag_county_lookup: 'County lookup',
    tag_sites_listed: (n) => n + ' sites listed',
    tip_sites: (n) => n + ' early voting sites',
    tip_lookup: 'Click for county lookup',
    label_hours: 'Hours',
    label_dates: 'Dates',
    label_election_day: 'Election Day',
    election_day_full: 'Tuesday, May 19, 2026',
    election_day_suffix: '· Polls 7a–7p · Vote at your assigned precinct only',
    section_locations: 'Early voting locations',
    directions: 'Directions',
    placeholder_lead: (n) => 'No site list available in this dashboard for ' + n + ' County.',
    placeholder_body_pre: 'Detailed site lists are included for 54 Georgia counties in this dashboard. For ',
    placeholder_body_mid: ', use the official Georgia ',
    placeholder_mvp_link: 'My Voter Page early-voting lookup',
    placeholder_or: ' or search ',
    placeholder_search_link_suffix: ' County Elections',
    help_lead: 'Need help?',
    help_body_pre: ' Call ',
    help_phone: '866-OUR-VOTE',
    help_phone_suffix: ' (866-687-8683) — free nonpartisan voter help line, English & Spanish.',
    help_find_polling: 'Find your assigned polling place at ',
    sources_label: 'Sources: ',
    footer_text: 'Nonpartisan voter information · Built with public data from county elections offices and the Georgia Secretary of State · ',
    footer_mvp: 'My Voter Page',
    footer_dot: ' · ',
    footer_ga: 'Georgia.gov early voting',
    suffix_county: ' County',
    button_label: 'Español',
    button_aria: 'Cambiar a español',

    /* What's on your ballot — office explainer */
    ballot_section: "What's on your ballot",
    ballot_intro: 'In this primary, voters across Georgia will help decide who advances to the November general election for many of the offices below. Some races (like the Supreme Court) are nonpartisan and are decided in May.',
    ballot_show: 'Show details',
    ballot_hide: 'Hide details',
    ballot_county_note: 'County and local races on your ballot vary — your sample ballot at My Voter Page shows exactly what you will see.',
    ballot_mvp_link: 'See your sample ballot',
    ballot_offices: [
      {
        name: 'Governor',
        what: 'Leads the state executive branch — signs or vetoes laws, sets the budget proposal, appoints judges to vacancies, and directs state agencies.',
        why: "Open seat. Gov. Brian Kemp is term-limited, so for the first time since 2018 there is no incumbent. Both parties are holding contested primaries."
      },
      {
        name: 'Lieutenant Governor',
        what: 'Presides over the State Senate, breaks tie votes, and steps in if the governor cannot serve.',
        why: 'Shapes which bills get heard in the Senate and how committee assignments are made.'
      },
      {
        name: 'Secretary of State',
        what: 'Runs Georgia elections, oversees voter registration and the official voter rolls, and licenses many businesses and professions.',
        why: 'Decides how elections are administered statewide, including rules for absentee ballots, drop boxes, and voter list maintenance.'
      },
      {
        name: 'Attorney General',
        what: "Georgia's chief lawyer — prosecutes some state cases, defends state laws in court, and issues legal opinions for state agencies.",
        why: 'Decides which lawsuits Georgia joins or files, and how aggressively to enforce consumer protection, civil rights, and antitrust laws.'
      },
      {
        name: 'Other statewide offices',
        what: 'Insurance Commissioner (regulates insurance and fire safety), Agriculture Commissioner (food safety and farms), Labor Commissioner (unemployment claims and workforce), and State School Superintendent (K–12 public schools).',
        why: 'These officials directly affect your insurance rates, the safety of your food, how unemployment claims are handled, and what your kids learn in public schools.'
      },
      {
        name: 'U.S. Senate',
        what: 'One of two senators representing Georgia in Washington for a six-year term — confirms federal judges, votes on treaties, and shapes federal law.',
        why: "Sen. Jon Ossoff's seat is on the ballot. The Senate is closely divided, so this race has national implications."
      },
      {
        name: 'Georgia Supreme Court (3 seats — nonpartisan)',
        what: "Georgia's highest court. Decides appeals on abortion, election laws, criminal sentences, business disputes, and the meaning of the state constitution. Justices serve six-year terms.",
        why: 'Three of the nine seats are up at once — a rare chance to shape the court for years. These races are officially nonpartisan and are decided in May (no November runoff unless no one wins outright). The last sitting Georgia Supreme Court justice to lose reelection was in 1922, so when challengers run seriously, every vote counts.'
      },
      {
        name: 'Public Service Commission (Districts 2 & 5)',
        what: 'Five elected commissioners regulate Georgia Power, Atlanta Gas Light, and most telecom utilities — they set the rates on your monthly power and gas bills.',
        why: 'Recent PSC decisions have driven multiple rate hikes. Districts 2 and 5 hold primaries May 19 and a general election November 3.'
      },
      {
        name: 'U.S. House of Representatives',
        what: 'Your district\'s member of Congress — a two-year term in Washington that votes on federal laws, the federal budget, and oversight of the executive branch.',
        why: 'House control is closely divided. Your district\'s race may be one of a small number that determines the national majority.'
      },
      {
        name: 'Georgia State Senate & House',
        what: 'Your state legislators write Georgia laws on schools, taxes, healthcare, criminal justice, and elections, and approve the state budget every year.',
        why: "State law often affects daily life more directly than federal law — and primaries frequently decide who wins, since many districts aren't competitive in November."
      },
      {
        name: 'County offices (vary by county)',
        what: 'Sheriff (county law enforcement and jail), Probate Judge (wills, marriage licenses, often elections), Tax Commissioner (property tax bills and car tags), Coroner, County Commission, and others.',
        why: 'These offices are the closest level of government to daily life and many are decided entirely in the primary.'
      },
      {
        name: 'Local nonpartisan races & referendums',
        what: 'Some counties and cities hold nonpartisan judicial races, school board races, or ballot questions like SPLOST (a 1% local sales tax for roads, schools, or other projects).',
        why: 'Referendums are decided by majority vote on the day — there is no November runoff for most of them.'
      }
    ],
  },
  es: {
    htmlLang: 'es',
    page_title: 'Primarias de Georgia 2026 — Centros de votación anticipada',
    h1: 'Primarias de Georgia 2026 — Centros de votación anticipada',
    subtitle: 'Pase el cursor o haga clic en cualquier condado para ver los centros de votación anticipada, los horarios y las direcciones.',
    meta_election_day: 'Día de elección:',
    meta_election_day_value: 'martes, 19 de mayo de 2026',
    meta_early_voting: 'Votación anticipada:',
    meta_early_voting_value: '27 de abril – 15 de mayo',
    meta_polls_open: 'Centros abiertos el día de elección:',
    meta_polls_open_value: '7 a.m. – 7 p.m.',
    meta_help_line: 'Línea de ayuda:',
    meta_help_line_value: '866-OUR-VOTE (866-687-8683)',
    search_placeholder: 'Buscar condado (p. ej., Fulton, Bibb, Chatham)…',
    legend_has_data: 'Centros detallados',
    legend_no_data: 'Búsqueda por condado',
    legend_selected: 'Seleccionado',
    map_aria: 'Mapa de los condados de Georgia',
    empty_title: 'Elija un condado',
    empty_body: 'Pase el cursor sobre cualquier condado para ver un resumen, o haga clic para ver todos los centros de votación anticipada y horarios. 54 condados tienen listas detalladas en este panel; los 159 condados enlazan a la búsqueda oficial.',
    tag_county_lookup: 'Búsqueda por condado',
    tag_sites_listed: (n) => n + ' centros listados',
    tip_sites: (n) => n + ' centros de votación anticipada',
    tip_lookup: 'Haga clic para buscar el condado',
    label_hours: 'Horario',
    label_dates: 'Fechas',
    label_election_day: 'Día de elección',
    election_day_full: 'martes, 19 de mayo de 2026',
    election_day_suffix: '· Centros abiertos 7 a.m.–7 p.m. · Vote solo en su centro asignado',
    section_locations: 'Centros de votación anticipada',
    directions: 'Cómo llegar',
    placeholder_lead: (n) => 'No hay lista de centros disponible en este panel para el condado de ' + n + '.',
    placeholder_body_pre: 'Las listas detalladas están incluidas para 54 condados de Georgia en este panel. Para ',
    placeholder_body_mid: ', use la herramienta oficial de Georgia ',
    placeholder_mvp_link: 'Búsqueda de centros de votación anticipada (My Voter Page)',
    placeholder_or: ' o busque ',
    placeholder_search_link_suffix: ' County Elections',
    help_lead: '¿Necesita ayuda?',
    help_body_pre: ' Llame al ',
    help_phone: '866-OUR-VOTE',
    help_phone_suffix: ' (866-687-8683) — línea gratuita y no partidista de ayuda al votante, en inglés y español.',
    help_find_polling: 'Encuentre su centro de votación asignado en ',
    sources_label: 'Fuentes: ',
    footer_text: 'Información no partidista para votantes · Creado con datos públicos de las oficinas electorales de los condados y de la Secretaría de Estado de Georgia · ',
    footer_mvp: 'My Voter Page',
    footer_dot: ' · ',
    footer_ga: 'Georgia.gov votación anticipada',
    suffix_county: ' (condado)',
    button_label: 'English',
    button_aria: 'Switch to English',

    /* What's on your ballot — office explainer */
    ballot_section: 'Qué hay en su boleta',
    ballot_intro: 'En estas primarias, los votantes de Georgia ayudan a decidir quién pasa a la elección general de noviembre para muchos de los cargos de abajo. Algunas contiendas (como la Corte Suprema) son no partidistas y se deciden en mayo.',
    ballot_show: 'Ver detalles',
    ballot_hide: 'Ocultar detalles',
    ballot_county_note: 'Las contiendas locales y del condado en su boleta varían — su boleta de muestra en My Voter Page le muestra exactamente lo que verá.',
    ballot_mvp_link: 'Ver su boleta de muestra',
    ballot_offices: [
      {
        name: 'Gobernador',
        what: 'Dirige la rama ejecutiva del estado — firma o veta leyes, propone el presupuesto, nombra jueces para vacantes y dirige las agencias estatales.',
        why: 'Cargo abierto. El gobernador Brian Kemp no puede reelegirse, así que por primera vez desde 2018 no hay un titular. Ambos partidos tienen primarias disputadas.'
      },
      {
        name: 'Vicegobernador',
        what: 'Preside el Senado estatal, rompe los empates en las votaciones y asume el cargo si el gobernador no puede ejercer.',
        why: 'Decide qué proyectos de ley se discuten en el Senado y cómo se asignan los comités.'
      },
      {
        name: 'Secretario de Estado',
        what: 'Dirige las elecciones de Georgia, supervisa el registro de votantes y los padrones electorales oficiales, y otorga licencias a muchas empresas y profesiones.',
        why: 'Decide cómo se administran las elecciones en todo el estado, incluyendo las reglas para boletas por correo, urnas de depósito y mantenimiento del padrón.'
      },
      {
        name: 'Procurador General (Attorney General)',
        what: 'Es el principal abogado del estado — procesa ciertos casos, defiende las leyes estatales en los tribunales y emite opiniones legales para las agencias estatales.',
        why: 'Decide a qué demandas se une o presenta Georgia, y con qué fuerza se aplican las leyes de protección al consumidor, derechos civiles y antimonopolio.'
      },
      {
        name: 'Otros cargos estatales',
        what: 'Comisionado de Seguros (regula seguros y seguridad contra incendios), Comisionado de Agricultura (seguridad alimentaria y granjas), Comisionado de Trabajo (reclamos de desempleo y fuerza laboral) y Superintendente Escolar Estatal (escuelas públicas K–12).',
        why: 'Estos funcionarios afectan directamente sus tarifas de seguros, la seguridad de los alimentos, cómo se manejan los reclamos de desempleo y lo que sus hijos aprenden en las escuelas públicas.'
      },
      {
        name: 'Senado de los EE. UU.',
        what: 'Uno de los dos senadores que representan a Georgia en Washington por seis años — confirma jueces federales, vota tratados y crea leyes federales.',
        why: 'El escaño del senador Jon Ossoff está en la boleta. El Senado está muy dividido, así que esta contienda tiene implicaciones nacionales.'
      },
      {
        name: 'Corte Suprema de Georgia (3 escaños — no partidista)',
        what: 'El tribunal más alto de Georgia. Decide apelaciones sobre el aborto, leyes electorales, sentencias penales, disputas comerciales y el sentido de la constitución estatal. Los jueces sirven seis años.',
        why: 'Tres de los nueve escaños se eligen al mismo tiempo — una oportunidad poco común de moldear el tribunal por años. Estas contiendas son oficialmente no partidistas y se deciden en mayo (sin segunda vuelta en noviembre, salvo que nadie gane por mayoría). El último juez en ejercicio de la Corte Suprema de Georgia que perdió la reelección fue en 1922, así que cuando hay retadores serios, cada voto cuenta.'
      },
      {
        name: 'Comisión de Servicios Públicos (Distritos 2 y 5)',
        what: 'Cinco comisionados electos regulan Georgia Power, Atlanta Gas Light y la mayoría de las empresas de telecomunicaciones — fijan las tarifas de su factura mensual de electricidad y gas.',
        why: 'Las decisiones recientes de la PSC han causado varios aumentos de tarifas. Los distritos 2 y 5 tienen primarias el 19 de mayo y elección general el 3 de noviembre.'
      },
      {
        name: 'Cámara de Representantes de los EE. UU.',
        what: 'El miembro del Congreso de su distrito — un mandato de dos años en Washington que vota leyes federales, el presupuesto federal y supervisa al ejecutivo.',
        why: 'El control de la Cámara está muy ajustado. La contienda de su distrito puede ser una de las pocas que decida la mayoría nacional.'
      },
      {
        name: 'Senado y Cámara estatales de Georgia',
        what: 'Sus legisladores estatales escriben las leyes de Georgia sobre escuelas, impuestos, salud, justicia penal y elecciones, y aprueban cada año el presupuesto del estado.',
        why: 'Las leyes estatales suelen afectar la vida diaria más directamente que las federales — y la primaria suele decidir el ganador, ya que muchos distritos no son competitivos en noviembre.'
      },
      {
        name: 'Cargos del condado (varían según el condado)',
        what: 'Sheriff (orden público y cárcel del condado), Juez de Sucesiones (testamentos, licencias de matrimonio, a menudo elecciones), Comisionado de Impuestos (impuestos de propiedad y placas de carro), Forense, Comisión del Condado y otros.',
        why: 'Estos cargos son el nivel de gobierno más cercano a la vida diaria, y muchos se deciden completamente en la primaria.'
      },
      {
        name: 'Contiendas locales no partidistas y referendos',
        what: 'Algunos condados y ciudades realizan elecciones judiciales no partidistas, elecciones de juntas escolares o consultas de boleta como SPLOST (un impuesto local de 1% sobre las ventas para carreteras, escuelas u otros proyectos).',
        why: 'Los referendos se deciden por mayoría el día de la elección — la mayoría no tiene segunda vuelta en noviembre.'
      }
    ],
  },
};

# Georgia 2026 Primary — Early Voting Locations Map

Interactive nonpartisan dashboard showing early voting locations and hours for the
**May 19, 2026 Georgia Primary Election**. Hover or click any of Georgia's 159
counties for site details.

**Live site:** https://mdr-palacios.github.io/ga-2026-early-voting/

![Screenshot of the dashboard](screenshot.png)

## What's in it

- **Interactive map** of all 159 Georgia counties (D3 + TopoJSON)
- **Detailed site lists** for the 16 largest Georgia counties — names, addresses,
  hours, special notes (Sunday voting, weekend-only sites), and directions links:
  - **Metro Atlanta:** Fulton, DeKalb, Gwinnett, Cobb, Clayton, Cherokee, Henry,
    Forsyth, Paulding, Coweta
  - **Outside metro Atlanta:** Chatham (Savannah), Richmond (Augusta),
    Muscogee (Columbus), Hall (Gainesville), Houston (Warner Robins), Columbia
- **Statewide fallback** — the remaining 143 counties link to Georgia's official
  My Voter Page early-voting lookup
- **Hours, dates, Election-Day reminders** built into every county view
- **Voter help line** (866-OUR-VOTE) on every panel

## Election facts

| | |
|---|---|
| **Primary date** | Tuesday, May 19, 2026 |
| **Early voting** | April 27 – May 15, 2026 |
| **Polls open** | 7am – 7pm on Election Day |
| **Help line** | 866-OUR-VOTE (866-687-8683) |

## Tech

- Pure static site — `index.html` + `app.js` + two JSON files
- [D3.js v7](https://d3js.org/) and [topojson-client v3](https://github.com/topojson/topojson-client) loaded from jsDelivr
- TopoJSON of GA counties from [kthotav/TopoJSON-Maps](https://github.com/kthotav/TopoJSON-Maps)
- No build step. Hosted on GitHub Pages.

## Files

- `index.html` — markup + styles
- `app.js` — map rendering, hover/click, search, detail panel
- `voting-locations.json` — generated from `build_data.py` (location data per county)
- `ga-counties.json` — TopoJSON of Georgia's 159 counties
- `build_data.py` — regenerates `voting-locations.json` (run with `python3 build_data.py`)

## Data sources

Metro Atlanta:
- [Fulton County Elections](https://www.fultoncountyga.gov/inside-fulton-county/fulton-county-departments/registration-and-elections/early-voting-locations)
- [DeKalb Voter Registration & Elections](https://www.dekalbvotes.com/)
- [Gwinnett County Elections](https://www.gwinnettcounty.com/government/departments/elections/voting/advance)
- [Cobb County Elections](https://www.cobbcounty.org/elections)
- [Clayton County Elections](https://www.claytoncountyga.gov/government/elections-and-registration/)
- [Cherokee County Elections](https://cherokeegavotes.com/advance-voting-2/)
- [Henry County Elections](https://www.henrycountyga.gov/35/Services)
- [Forsyth County Elections](https://www.forsythco.com/Departments-Offices/Voter-Registrations-Elections)
- [Paulding County Elections](https://www.paulding.gov/1501/Advanced-Voting)
- [Coweta County Elections](https://www.coweta.ga.us/departments-services/departments-a-e/elections-and-voter-registration-7700)

Outside metro Atlanta:
- [Chatham County Board of Registrars](https://voter.chathamcountyga.gov/)
- [Augusta-Richmond County Elections](https://www.augustaga.gov/2836/Advance-Voting-Location-Information)
- [Muscogee County Elections](https://columbusga.gov/elections/)
- [Hall County Elections](https://www.hallcounty.org/249/Elections)
- [Houston County Board of Elections](https://www.houstoncountyga.gov/residents/early-voting.cms)
- [Columbia County Elections](https://www.columbiacountyga.gov/government/elections-board-of)

Statewide:
- [Georgia Secretary of State — My Voter Page](https://mvp.sos.ga.gov)
- [Georgia.gov — Vote Early in Person](https://georgia.gov/vote-early-person)

## Local preview

```bash
cd ga-2026-early-voting
python3 -m http.server 8000
# open http://localhost:8000
```

## License

This is nonpartisan public-interest information. Data is compiled from public
county and state sources. Map tiles and code released under the MIT license.

---

Made for Georgia voters — not affiliated with any party, candidate, or campaign.

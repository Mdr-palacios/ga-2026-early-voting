#!/usr/bin/env python3
"""Merge 10 Black Belt counties into voting-locations.json with EN+ES notes."""
import json, ast, re

PATH = '/home/user/workspace/ga_voting_map/voting-locations.json'

# Hand-crafted county records (from wide_browse + manual cleanup of dashes/sources/etc.)
# Notes are in English; notes_es is the Spanish translation.
NEW = {
    "Stewart": {
        "hours_summary": "Mon-Fri 8a-5p (closed for lunch 12-1p) \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Stewart County Board of Elections Office (Courthouse)",
             "1764 Broad St, Lumpkin, GA 31815"],
        ],
        "notes": "The Elections Office is inside the Stewart County Courthouse. The office is closed daily for lunch from 12:00 PM to 1:00 PM.",
        "notes_es": "La Oficina de Elecciones est\u00e1 dentro del Tribunal del Condado de Stewart. La oficina cierra todos los d\u00edas para el almuerzo de 12:00 PM a 1:00 PM.",
        "source_url": "https://stewartcountyga.gov/elections/index.html",
        "source_name": "Stewart County Board of Elections, Georgia My Voter Page",
    },
    "Quitman": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Quitman County Elections Office",
             "37 Old School Road, Georgetown, GA 39854"],
        ],
        "notes": "The early voting site recently moved from the Courthouse to Old School Road. A drop box is located at the Courthouse (111 Main Street).",
        "notes_es": "El sitio de votaci\u00f3n anticipada se traslad\u00f3 recientemente del Tribunal a Old School Road. Hay un buz\u00f3n para boletas en el Tribunal (111 Main Street).",
        "source_url": "https://www.gqc-ga.org/Default.asp?ID=121&pg=Elections",
        "source_name": "Quitman County Board of Elections and Voter Registration, Georgia My Voter Page",
    },
    "Marion": {
        "hours_summary": "Mon-Fri 8a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Marion County Board of Elections and Registration Office",
             "100 E Burkhalter Ave, Buena Vista, GA 31803"],
        ],
        "notes": "Advance voting is held at the Board of Elections office. A ballot dropbox is available at this location.",
        "notes_es": "La votaci\u00f3n anticipada se realiza en la oficina de la Junta de Elecciones. Hay un buz\u00f3n para boletas disponible en este lugar.",
        "source_url": "https://www.marioncountyga.org/by-department/elections-and-registration/",
        "source_name": "Georgia My Voter Page, Marion County Elections & Registration",
    },
    "Crisp": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Crisp County Government Center (Board of Elections Office)",
             "210 S 7th St, Room 103, Cordele, GA 31015"],
        ],
        "notes": "A ballot dropbox is available inside the early voting location during voting hours. Voting is held in Room 103.",
        "notes_es": "Hay un buz\u00f3n para boletas dentro del centro de votaci\u00f3n anticipada durante el horario de votaci\u00f3n. La votaci\u00f3n se realiza en la Sala 103.",
        "source_url": "https://crispcounty.com/elections-voter-registration",
        "source_name": "Crisp County Board of Elections, Georgia My Voter Page",
    },
    "Twiggs": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Twiggs County Board of Elections & Registrations Office",
             "425 Railroad Street North, Rm 123, Jeffersonville, GA 31044"],
        ],
        "notes": "Voting is held in the courthouse, Room 123. The dropbox is at the front entrance with the security guard during early voting dates.",
        "notes_es": "La votaci\u00f3n se realiza en el tribunal, Sala 123. El buz\u00f3n est\u00e1 en la entrada principal con el guardia de seguridad durante las fechas de votaci\u00f3n anticipada.",
        "source_url": "https://www.twiggscounty.us/notice-l-a-testing-computation-canvassing-and-absentee-voting-may-192026-general-primary-election-nonpartisan-election/",
        "source_name": "Twiggs County Board of Elections & Registrations",
    },
    "Wilkinson": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Wilkinson County Courthouse (Elections and Registrar Office, Rm 133)",
             "100 Bacon Street, Irwinton, GA 31042"],
        ],
        "notes": "Advance voting is held in the Elections and Registrar Office (Room 133) of the courthouse. Dropbox is available during voting hours. No Sunday voting.",
        "notes_es": "La votaci\u00f3n anticipada se realiza en la Oficina de Elecciones y Registro (Sala 133) del tribunal. El buz\u00f3n est\u00e1 disponible durante el horario de votaci\u00f3n. No hay votaci\u00f3n los domingos.",
        "source_url": "https://mvp.sos.ga.gov/s/advanced-voting-location-information?election=a0pcs00000J6e6HAAR&countyName=WILKINSON&page=advpollingplace",
        "source_name": "Georgia My Voter Page, Wilkinson County Board of Elections",
    },
    "Warren": {
        "hours_summary": "Mon-Fri 8a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Warren County Board of Elections Office (Community Service Building)",
             "48 Warren Street, Warrenton, GA 30828"],
        ],
        "notes": "Early voting is held at the Board of Elections office. No official drop box is available in the county: voters may bring ballots into the office.",
        "notes_es": "La votaci\u00f3n anticipada se realiza en la oficina de la Junta de Elecciones. No hay buz\u00f3n oficial en el condado: los votantes pueden entregar las boletas dentro de la oficina.",
        "source_url": "https://www.warrencountyga.com/elections.html",
        "source_name": "Warren County Board of Elections, Georgia My Voter Page",
    },
    "Greene": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Greene County Annex Early Voting",
             "1180 C Weldon Smith Drive, Suite 109, Greensboro, GA 30642"],
        ],
        "notes": "Ballot dropbox is available inside the polling location during early voting hours. The site is open both Saturdays (May 2 and May 9).",
        "notes_es": "Hay un buz\u00f3n para boletas dentro del centro de votaci\u00f3n durante el horario de votaci\u00f3n anticipada. El sitio est\u00e1 abierto los dos s\u00e1bados (2 y 9 de mayo).",
        "source_url": "https://www.greenecountyga.gov/984/Vote-Early-In-Person",
        "source_name": "Georgia My Voter Page, Greene County Board of Elections",
    },
    "Jenkins": {
        "hours_summary": "Mon-Fri 9a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["James Henry Administrative Building (Election and Registration Office)",
             "833 East Winthrope Avenue, Millen, GA 30442"],
        ],
        "notes": "Drop box located inside the early voting site. No Sunday voting. Contact Election Supervisor Patricia Rich at 478-982-3985 for questions.",
        "notes_es": "El buz\u00f3n est\u00e1 dentro del centro de votaci\u00f3n anticipada. No hay votaci\u00f3n los domingos. Para preguntas, llame a la Supervisora de Elecciones Patricia Rich al 478-982-3985.",
        "source_url": "https://www.jenkinscounty.net/notices",
        "source_name": "Jenkins County Board of Elections and Registration",
    },
    "Emanuel": {
        "hours_summary": "Mon-Fri 8:30a-5p \u00b7 Sat May 2: 9a-5p \u00b7 Sat May 9: 9a-5p",
        "dates": "Apr 27 \u2013 May 15, 2026",
        "locations": [
            ["Emanuel County Elections Office",
             "223 W Moring St, Suite 102, Swainsboro, GA 30401"],
        ],
        "notes": "Early voting is held at the county elections office. A ballot dropbox is available inside the building during early voting hours and closes May 15.",
        "notes_es": "La votaci\u00f3n anticipada se realiza en la oficina de elecciones del condado. Hay un buz\u00f3n para boletas dentro del edificio durante el horario de votaci\u00f3n anticipada y cierra el 15 de mayo.",
        "source_url": "https://mvp.sos.ga.gov/s/advanced-voting-location-information?election=a0pcs00000J6e6HAAR&countyName=EMANUEL&page=advpollingplace",
        "source_name": "Georgia My Voter Page, Emanuel County Board of Elections",
    },
}


def main():
    with open(PATH) as f:
        d = json.load(f)
    counties = d['counties']

    # Sanity: verify NO em dashes anywhere we're inserting
    em_dash = '\u2014'
    for k, v in NEW.items():
        for field in ('hours_summary', 'notes', 'notes_es', 'source_name'):
            val = v.get(field, '')
            if em_dash in val:
                raise SystemExit(f"em dash found in {k}.{field}: {val!r}")

    added = 0
    for name, payload in NEW.items():
        if name not in counties:
            print(f"  WARN: {name} not in counties dict; skipping")
            continue
        # Replace placeholder with full record
        counties[name] = payload
        added += 1
        print(f"  + {name}: {len(payload['locations'])} location(s)")

    with open(PATH, 'w') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print(f"\nUpdated {added}/{len(NEW)} counties.")
    print(f"Total counties with locations now:",
          sum(1 for v in counties.values() if v.get('locations')))


if __name__ == '__main__':
    main()

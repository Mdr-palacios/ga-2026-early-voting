#!/usr/bin/env python3
"""Merge the next 10 most populous counties into voting-locations.json."""
import csv, ast, json, re
from pathlib import Path

CSV_PATH = '/home/user/workspace/wide/browse_results_mor5exw1.csv'
JSON_PATH = Path(__file__).parent / 'voting-locations.json'


def clean_url(s: str) -> str:
    """Source URL cells sometimes come as markdown like '[Label](url)' or comma-separated.
    Pull the first http(s) URL we find."""
    if not s:
        return ''
    m = re.search(r'https?://[^\s)\],]+', s)
    return m.group(0) if m else s.strip()


def main():
    with open(CSV_PATH) as f:
        rows = list(csv.DictReader(f))

    with open(JSON_PATH) as f:
        data = json.load(f)
    counties = data['counties']

    added = []
    for r in rows:
        county = r['County'].strip()
        if not county:
            continue

        try:
            locs_parsed = ast.literal_eval(r['Locations'])
        except (ValueError, SyntaxError):
            try:
                locs_parsed = json.loads(r['Locations'])
            except Exception as e:
                print(f'SKIP {county}: cannot parse locations ({e})')
                continue

        # Convert each location dict {name, address} -> [name, address]
        loc_pairs = []
        for L in locs_parsed:
            if isinstance(L, dict):
                name = (L.get('name') or '').strip()
                addr = (L.get('address') or '').strip()
                if name and addr:
                    loc_pairs.append([name, addr])
            elif isinstance(L, (list, tuple)) and len(L) >= 2:
                loc_pairs.append([str(L[0]).strip(), str(L[1]).strip()])

        if not loc_pairs:
            print(f'SKIP {county}: no valid locations')
            continue

        entry = {
            'hours_summary': r['Hours Summary'].strip(),
            'dates': r['Dates'].strip() or 'Apr 27 – May 15, 2026',
            'locations': loc_pairs,
        }
        notes = (r.get('Notes') or '').strip()
        if notes:
            entry['notes'] = notes
        src_url = clean_url(r.get('Source URL', ''))
        if src_url:
            entry['source_url'] = src_url
        src_name = (r.get('Source Name') or '').strip()
        if src_name:
            entry['source_name'] = src_name

        counties[county] = entry
        added.append((county, len(loc_pairs)))

    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'\nAdded {len(added)} counties:')
    for c, n in added:
        print(f'  {c}: {n} locations')

    detailed = [c for c, v in counties.items() if isinstance(v, dict) and v.get('locations')]
    print(f'\nTotal detailed counties: {len(detailed)}')


if __name__ == '__main__':
    main()

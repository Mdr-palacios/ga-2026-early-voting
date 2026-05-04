#!/usr/bin/env python3
"""
Merge PeachVote.com early-voting location data into voting-locations.json.

Strategy:
- Parse /tmp/peachvote_locations.json (already harvested).
- For each GA county:
    * If existing entry has placeholder=true OR no locations: REPLACE locations with PeachVote data.
    * If existing entry already has detailed locations: PRESERVE them
      (we already hand-curated those; don't clobber human-vetted Spanish notes).
- Compute hours_summary from the PeachVote per-location hours strings.
- Add notes (and notes_es) and a sources entry pointing to PeachVote.
- Keep election-day metadata as-is.
"""

import json, re, sys
from collections import OrderedDict

PEACH = json.load(open('/tmp/peachvote_locations.json'))
DATA = json.load(open('/home/user/workspace/ga_voting_map/voting-locations.json'))

# Group PeachVote In-Person locations by county
in_person = {}
for L in PEACH['locations']:
    if L['type'] != 'In-Person':
        continue
    county = (L['county'] or '').strip()
    if not county:
        continue
    in_person.setdefault(county, []).append(L)

phones = PEACH['phones']

def humanize_hours(hours_text):
    """Compress per-day hours text into a short summary."""
    if not hours_text:
        return None
    lines = [ln.strip() for ln in hours_text.split('\n') if ln.strip()]
    # Detect Saturday and Sunday lines for summary
    has_sat = any(re.search(r'^Sat', ln) for ln in lines)
    has_sun = any(re.search(r'^Sun', ln) for ln in lines)
    # Find a representative weekday range (most common time block)
    weekday_lines = [ln for ln in lines if re.match(r'^Mon', ln)]
    # Most common opening time across weekday lines
    times = []
    for ln in weekday_lines:
        m = re.search(r':\s*([0-9:]+\s*[AP]M)\s*-\s*([0-9:]+\s*[AP]M)', ln)
        if m: times.append((m.group(1), m.group(2)))
    if times:
        # pick the modal one
        from collections import Counter
        most = Counter(times).most_common(1)[0][0]
        weekday_summary = f"Mon–Fri {most[0]}–{most[1]}".replace(':00 ', '')
    else:
        weekday_summary = "Mon–Fri (hours vary)"
    extras = []
    if has_sat: extras.append('Sat hours available')
    if has_sun: extras.append('Sun hours available')
    return weekday_summary + (' · ' + ' · '.join(extras) if extras else '')


updated_count = 0
preserved_count = 0
no_data_count = 0
new_with_pv = 0

for county, info in DATA['counties'].items():
    pv_locs = in_person.get(county, [])
    has_existing_detail = (
        not info.get('placeholder', False)
        and isinstance(info.get('locations'), list)
        and len(info['locations']) > 0
    )

    if has_existing_detail:
        # Preserve hand-curated entry but optionally enrich with phone if missing
        preserved_count += 1
        # Add PeachVote as an additional source for completeness
        sources = info.get('sources', [])
        if not any('peachvote' in (s[1] if isinstance(s, list) else '').lower() for s in sources):
            if isinstance(sources, list):
                sources.append(["PeachVote.com", "https://www.peachvote.com/location-lookup"])
                info['sources'] = sources
        if county in phones and 'phone' not in info:
            info['phone'] = phones[county]
        continue

    if not pv_locs:
        no_data_count += 1
        continue

    # Replace with PeachVote data
    locations_list = []
    all_hours = []
    for L in pv_locs:
        nm = L.get('name') or 'Early Voting Location'
        addr = L.get('address') or ''
        locations_list.append([nm, addr])
        if L.get('hours'):
            all_hours.append(L['hours'])

    # Use the first location's hours for summary (most counties have one schedule)
    summary_source = all_hours[0] if all_hours else ''
    hours_summary = humanize_hours(summary_source) or info.get('hours_summary', '')

    # Build per-location hours map for the notes field
    notes_lines = []
    notes_es_lines = []
    for L in pv_locs:
        if L.get('hours'):
            notes_lines.append(f"{L['name']}: {L['hours']}")
            notes_es_lines.append(f"{L['name']}: {L['hours']}")  # hours are date/time, language-neutral

    notes = "Detailed hours per location:\n" + "\n\n".join(notes_lines) if notes_lines else None
    notes_es = "Horarios detallados por sede:\n" + "\n\n".join(notes_es_lines) if notes_es_lines else None

    new_entry = OrderedDict()
    new_entry['hours_summary'] = hours_summary
    new_entry['dates'] = info.get('dates', 'Apr 27 – May 15, 2026')
    new_entry['locations'] = locations_list
    if notes: new_entry['notes'] = notes
    if notes_es: new_entry['notes_es'] = notes_es
    if county in phones:
        new_entry['phone'] = phones[county]
    new_entry['placeholder'] = False
    new_entry['sources'] = [
        ["PeachVote.com", "https://www.peachvote.com/location-lookup"],
        ["My Voter Page", "https://mvp.sos.ga.gov/s/advanced-voting-location-information"],
    ]
    DATA['counties'][county] = new_entry

    if info.get('placeholder', False):
        updated_count += 1
    else:
        new_with_pv += 1

# Sort counties alphabetically
DATA['counties'] = OrderedDict(sorted(DATA['counties'].items()))

with open('/home/user/workspace/ga_voting_map/voting-locations.json', 'w') as f:
    json.dump(DATA, f, indent=2, ensure_ascii=False)

# Final stats
total = len(DATA['counties'])
detailed = sum(1 for c in DATA['counties'].values() if not c.get('placeholder', False) and c.get('locations'))
placeholders = sum(1 for c in DATA['counties'].values() if c.get('placeholder', False))

print(f"Counties total: {total}")
print(f"Counties with detail (after merge): {detailed}")
print(f"Placeholders remaining: {placeholders}")
print(f"  - upgraded from placeholder via PeachVote: {updated_count}")
print(f"  - preserved hand-curated: {preserved_count}")
print(f"  - no PeachVote data found: {no_data_count}")

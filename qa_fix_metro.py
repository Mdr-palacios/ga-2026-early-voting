#!/usr/bin/env python3
"""
QA fix: Override 3 metro counties (Gwinnett, DeKalb, Clayton) with verified
official-source location lists. The original hand-curated data was outdated.
"""
import json
from collections import OrderedDict

DATA = json.load(open('/home/user/workspace/ga_voting_map/voting-locations.json'))

# ── GWINNETT (13 locations, official county source) ──
gwinnett = OrderedDict()
gwinnett['hours_summary'] = 'Mon–Fri 7a–7p · Sat May 9: 9a–5p'
gwinnett['dates'] = 'Apr 27 – May 15, 2026'
gwinnett['phone'] = '(678) 226-7210'
gwinnett['locations'] = [
    ['Voter Registration & Elections Office (Beauty P. Baldwin Bldg)', '455 Grayson Hwy, Suite 200, Lawrenceville, GA 30046'],
    ['Bogan Park Community Recreation Center', '2723 N Bogan Rd, Buford, GA 30519'],
    ['Collins Hill Library', '455 Camp Perrin Rd NE, Lawrenceville, GA 30043'],
    ['Dacula Park Activity Building', '2735 Auburn Ave, Dacula, GA 30019'],
    ['Five Forks Library', '2780 Five Forks Trickum Rd SW, Lawrenceville, GA 30044'],
    ['George Pierce Park Recreation Center', '55 Buford Hwy, Suwanee, GA 30024'],
    ['Gwinnett Community Resource Center (Bethany Church Rd)', '3025 Bethany Church Rd, Snellville, GA 30039'],
    ['Gwinnett Fire Station 30', '1052 Ozora Rd, Loganville, GA 30052'],
    ['Lucky Shoals Park Community Recreation Center', '4651 Britt Rd, Norcross, GA 30093'],
    ['Mountain Park Activity Building', '1063 Rockbridge Rd, Stone Mountain, GA 30087'],
    ['Pinckneyville Park Community Recreation Center', '4650 Peachtree Industrial Blvd, Berkeley Lake, GA 30071'],
    ['Rhodes Jordan Park Community Recreation Center', '100 E Crogan St, Lawrenceville, GA 30046'],
    ['Shorty Howell Park Activity Building', '2750 Pleasant Hill Rd, Duluth, GA 30096'],
]
gwinnett['notes'] = '13 advance voting sites. Drop boxes available at the Elections Office, George Pierce Park, Centerville, Gwinnett Fire Station 30, Mountain Park, and Pinckneyville during voting hours.'
gwinnett['notes_es'] = '13 sedes de votación anticipada. Buzones disponibles en la Oficina de Elecciones, George Pierce Park, Centerville, Estación de Bomberos 30, Mountain Park y Pinckneyville durante las horas de votación.'
gwinnett['placeholder'] = False
gwinnett['sources'] = [
    ['Gwinnett County Elections', 'https://www.gwinnettcounty.com/government/departments/elections/voting/advance'],
    ['PeachVote.com', 'https://www.peachvote.com/location-lookup'],
]

# ── DEKALB (20 locations, official PDF + WABE confirmation) ──
dekalb = OrderedDict()
dekalb['hours_summary'] = 'Mon–Fri 7a–7p · Sat 9a–6p (May 2 & 9) · Sun 12p–5p (May 3 & 10)'
dekalb['dates'] = 'Apr 27 – May 15, 2026'
dekalb['phone'] = '(404) 298-4020'
dekalb['locations'] = [
    ['DeKalb Voter Registration & Elections Office ★', '4380 Memorial Dr, Suite 500, Decatur, GA 30032'],
    ['Berean Christian Church ★', '2201 Young Rd, Stone Mountain, GA 30088'],
    ['Bessie Branham Recreation Center', '2051 Delano Dr NE, Atlanta, GA 30317'],
    ['Beulah Missionary Baptist Church ★', '2340 Clifton Springs Rd, Decatur, GA 30034'],
    ['Briarwood Recreation Center', '2235 Briarwood Way NE, Atlanta, GA 30329'],
    ['Clarkston Library', '951 N Indian Creek Dr, Clarkston, GA 30021'],
    ['County Line-Ellenwood Library', '4331 River Rd, Ellenwood, GA 30294'],
    ['Dunwoody Library ★', '5339 Chamblee Dunwoody Rd, Dunwoody, GA 30338'],
    ['Emory University', '1599 Clifton Rd NE, Atlanta, GA 30329'],
    ['Greater Piney Grove Church', '1879 Glenwood Ave SE, Atlanta, GA 30316'],
    ['Hairston Crossing Library', '4911 Redan Rd, Stone Mountain, GA 30088'],
    ['Living Grace Lutheran Church', '1812 Cooledge Rd, Tucker, GA 30084'],
    ['Neighborhood Church', '1561 McLendon Ave NE, Atlanta, GA 30307'],
    ['New Bethel A.M.E. Church', '8350 Rockbridge Rd, Lithonia, GA 30058'],
    ['North DeKalb Senior Center', '3393 Malone Dr, Chamblee, GA 30341'],
    ['Redan-Trotti Library', '1569 Wellborn Rd, Lithonia, GA 30058'],
    ['Salem-Panola Library ★', '5137 Salem Rd, Lithonia, GA 30038'],
    ['Stonecrest Library', '3123 Klondike Rd, Stonecrest, GA 30038'],
    ['Tucker Library ★', '5234 Lavista Rd, Tucker, GA 30084'],
    ['Wesley Chapel Library', '2861 Wesley Chapel Rd, Decatur, GA 30034'],
]
dekalb['notes'] = '20 advance voting sites. ★ = also a 24-hour ballot drop box location.'
dekalb['notes_es'] = '20 sedes de votación anticipada. ★ = también es un buzón de boletas las 24 horas.'
dekalb['placeholder'] = False
dekalb['sources'] = [
    ['DeKalb Voter Registration & Elections', 'https://www.dekalbvotes.com/'],
    ['DeKalb County Official Flyer (PDF)', 'https://www.dekalbcountyga.gov/sites/default/files/users/user3597/AIP%20May%20PEV5_1.pdf'],
    ['PeachVote.com', 'https://www.peachvote.com/location-lookup'],
]

# ── CLAYTON (11 locations, official county press release) ──
clayton = OrderedDict()
clayton['hours_summary'] = 'Mon–Fri 8a–7p · Sat 9a–5p · Sun 12p–5p'
clayton['dates'] = 'Apr 27 – May 15, 2026'
clayton['phone'] = '(770) 477-3372'
clayton['locations'] = [
    ['Election & Registration Office ★', '121 S McDonough St, Jonesboro, GA 30236'],
    ['Carl Rhodenizer Recreation Center ★', '3499 Rex Rd, Rex, GA 30273'],
    ['Forest Park Senior Center', '5087 Park Ave, Forest Park, GA 30297'],
    ['Lake Spivey Recreation Center', '2300 Walt Stephens Rd, Jonesboro, GA 30236'],
    ['Morrow City Hall', '1500 Morrow Rd, Morrow, GA 30260'],
    ['South Clayton Recreation Center ★', '1837 McDonough Rd, Hampton, GA 30228'],
    ['Virginia Gray Recreation Center', '1475 E Fayetteville Rd, Riverdale, GA 30296'],
    ['Flint River Community Center', '153 Flint River Rd, Riverdale, GA 30296'],
    ['Sonna Gregory Senior Center', '3215 Anvil Block Rd, Ellenwood, GA 30294'],
    ['Northwest Branch Library', '6131 Riverdale Rd, Riverdale, GA 30274'],
    ['Headquarters Library', '865 Battle Creek Rd, Jonesboro, GA 30236'],
]
clayton['notes'] = '11 advance voting sites. ★ = also a ballot drop box location.'
clayton['notes_es'] = '11 sedes de votación anticipada. ★ = también es buzón de boletas.'
clayton['placeholder'] = False
clayton['sources'] = [
    ['Clayton County Official Announcement', 'https://www.claytoncountyga.org/advance-voting-for-general-primary-election-begins/'],
    ['Clayton County Elections', 'https://www.claytonelections.com/'],
    ['PeachVote.com', 'https://www.peachvote.com/location-lookup'],
]

DATA['counties']['Gwinnett'] = gwinnett
DATA['counties']['DeKalb'] = dekalb
DATA['counties']['Clayton'] = clayton

# Re-sort
DATA['counties'] = OrderedDict(sorted(DATA['counties'].items()))

with open('/home/user/workspace/ga_voting_map/voting-locations.json', 'w') as f:
    json.dump(DATA, f, indent=2, ensure_ascii=False)

# Em-dash check
with open('/home/user/workspace/ga_voting_map/voting-locations.json') as f:
    text = f.read()
em = text.count('—')
print(f"Em-dashes: {em} (should be 0)")
print(f"Updated: Gwinnett ({len(gwinnett['locations'])}), DeKalb ({len(dekalb['locations'])}), Clayton ({len(clayton['locations'])})")

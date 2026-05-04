#!/usr/bin/env python3
"""Build voting-locations.json from sourced + placeholder county data.

NOTE: This script regenerates the file from scratch using the DETAILED dict
below. As of the latest update, additional counties (Chatham, Forsyth, Henry,
Hall, Richmond, Muscogee, Paulding, Houston, Columbia, Coweta) were merged
into voting-locations.json directly via a separate research pipeline.
Running this script will overwrite that data with only the 6 metros below.
If you re-run it, also re-merge the additional counties.
"""
import json

# Six counties with detailed data sourced for the 2026 primary
DETAILED = {
    "Fulton": {
        "hours_summary": "Mon–Fri 7a–7p · Sat 9a–5p · Sun 10a–4p (select sites)",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["Fulton County Govt Center", "130 Peachtree St SW, Atlanta, GA 30303"],
            ["C.T. Martin Natatorium", "3201 Martin L King Jr Dr SW, Atlanta, GA 30311"],
            ["Buckhead Library", "269 Buckhead Ave NE, Atlanta, GA 30305"],
            ["Adams Park Library", "2231 Campbellton Rd SW, Atlanta, GA 30311"],
            ["Wolf Creek Library", "3100 Enon Rd, South Fulton, GA 30331"],
            ["Sandy Springs Library", "395 Mt Vernon Hwy NE, Sandy Springs, GA 30328"],
            ["Roswell Library", "115 Norcross St, Roswell, GA 30075"],
            ["Alpharetta Library", "10 Park Plaza, Alpharetta, GA 30009"],
            ["Milton Library", "855 Mayfield Rd, Milton, GA 30009"],
            ["Johns Creek Environmental Campus", "8100 Holcomb Bridge Rd, Roswell, GA 30022"],
            ["Robert F. Fulton Ocee Library", "5090 Abbotts Bridge Rd, Johns Creek, GA 30005"],
            ["East Roswell Library", "2301 Holcomb Bridge Rd, Roswell, GA 30076"],
            ["Northeast Spruill Oaks Library", "9560 Spruill Rd, Johns Creek, GA 30022"],
            ["Welcome All Recreation Center", "4255 Will Lee Rd, Atlanta, GA 30349"],
            ["South Fulton Service Center", "5600 Stonewall Tell Rd, South Fulton, GA 30349"],
            ["Elections Hub and Operations Center", "5600 Campbellton Fairburn Rd, Union City, GA 30213"],
            ["Etris-Darnell Community Recreation Center", "5285 Lakeside Dr, Union City, GA 30291"],
            ["Evelyn G. Lowery Library at Cascade", "3665 Cascade Rd SW, South Fulton, GA 30331"],
            ["Fairburn Annex", "40 Washington St, Fairburn, GA 30213"],
            ["Flipper Temple AME Church", "580 Atlanta Student Movement Blvd, Atlanta, GA 30314"],
            ["Fulton County Health and Human Services - North", "4700 North Point Pkwy, Alpharetta, GA 30005"],
            ["Gladys S. Dennard Library at South Fulton", "4055 Flat Shoals Rd, South Fulton, GA 30291"],
            ["Grant Park Recreation Center", "537 Park Ave SE, Atlanta, GA 30312"],
            ["Hugh C. Conley Recreation Center", "3636 College St, College Park, GA 30337"],
            ["Joan P. Garner Library at Ponce De Leon", "980 Ponce De Leon Ave NE, Atlanta, GA 30306"],
            ["Mechanicsville Library", "400 Formwalt St SW, Atlanta, GA 30312"],
            ["Metropolitan Library", "1332 Metropolitan Pkwy SW, Atlanta, GA 30310"],
            ["North Fulton Service Center", "7741 Roswell Rd, Sandy Springs, GA 30350"],
            ["Northside Library", "3295 Northside Pkwy NW, Atlanta, GA 30327"],
            ["Northwest Library at Scotts Crossing", "2489 Perry Blvd NW, Atlanta, GA 30318"],
            ["Palmetto Library", "9111 Cascade Palmetto Hwy, Palmetto, GA 30268"],
            ["Southwest Arts Center", "915 New Hope Rd SW, South Fulton, GA 30331"],
        ],
        "sources": [
            ["Fulton County Elections", "https://www.fultoncountyga.gov/inside-fulton-county/fulton-county-departments/registration-and-elections/early-voting-locations"],
        ],
    },
    "DeKalb": {
        "hours_summary": "Mon–Fri 7a–7p · Sat 9a–5p · Sun 12p–5p (select sites)",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["Voter Registration & Elections Office", "4380 Memorial Dr, Decatur, GA 30032"],
            ["Bessie Branham Recreation Center", "2051 Delano Dr NE, Atlanta, GA 30317"],
            ["County Line / Ellenwood Library", "4331 River Rd, Ellenwood, GA 30294"],
            ["Berean Christian Church", "2201 Young Rd, Stone Mountain, GA 30088"],
            ["Brookhaven Library", "1242 N Druid Hills Rd NE, Brookhaven, GA 30319"],
            ["Chamblee Civic Center", "3540 Broad St, Chamblee, GA 30341"],
            ["Lithonia-Davidson Library", "6821 Church St, Lithonia, GA 30058"],
            ["Stonecrest Library", "3123 Klondike Rd, Stonecrest, GA 30038"],
            ["Tucker-Reid H. Cofer Library", "5234 LaVista Rd, Tucker, GA 30084"],
            ["Wesley Chapel-William C. Brown Library", "2861 Wesley Chapel Rd, Decatur, GA 30034"],
            ["Dunwoody Library", "5339 Chamblee Dunwoody Rd, Dunwoody, GA 30338"],
        ],
        "sources": [
            ["DeKalb Voter Registration & Elections", "https://www.dekalbvotes.com/"],
        ],
    },
    "Gwinnett": {
        "hours_summary": "Mon–Fri 7a–7p · Sat May 9: 9a–5p · Closed Sundays",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["Voter Registration & Elections Office", "455 Grayson Hwy, Suite 200, Lawrenceville, GA 30046"],
            ["Bogan Park Community Recreation Center", "2723 N Bogan Rd, Buford, GA 30519"],
            ["Centerville Community Center", "3025 Bethany Church Rd, Snellville, GA 30039"],
            ["George Pierce Park Community Recreation Center", "55 Buford Hwy, Suwanee, GA 30024"],
            ["Lenora Park Gym", "4515 Lenora Church Rd, Snellville, GA 30039"],
            ["Lucky Shoals Park Community Recreation Center", "4651 Britt Rd, Norcross, GA 30093"],
            ["Mountain Park Activity Building", "1063 Rockbridge Rd, Stone Mountain, GA 30087"],
            ["Shorty Howell Park Activity Building", "2750 Pleasant Hill Rd, Duluth, GA 30096"],
        ],
        "sources": [
            ["Gwinnett County Elections", "https://www.gwinnettcounty.com/government/departments/elections/voting/advance"],
        ],
    },
    "Cobb": {
        "hours_summary": "Mon–Fri 7a–7p · Sat 9a–5p · Sun 12p–5p (★ sites only)",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["★ Main Elections Office", "995 Roswell St NE, Marietta, GA 30060"],
            ["★ North Cobb Senior Center", "3900 S Main St, Acworth, GA 30101"],
            ["★ South Cobb Community Center", "620 Lions Club Dr, Mableton, GA 30126"],
            ["★ East Cobb Govt. Service Center", "4400 Lower Roswell Rd, Marietta, GA 30068"],
            ["★ Boots Ward Recreation Center", "4845 Dallas Hwy, Powder Springs, GA 30127"],
            ["Milford Recreation Center", "675 Smyrna Powder Springs Rd, Marietta, GA 30060"],
            ["Ron Anderson Recreation Center", "3820 Macedonia Rd, Powder Springs, GA 30127"],
            ["Tim D. Lee Senior Center", "3332 Sandy Plains Rd, Marietta, GA 30066"],
            ["West Cobb Regional Library", "1750 Dennis Kemp Ln, Kennesaw, GA 30152"],
            ["Collar Park Community Center", "2625 Joe Jerkins Blvd, Austell, GA 30106"],
            ["Ben Robertson Community Center", "2753 Watts Dr, Kennesaw, GA 30144"],
            ["Fair Oaks Recreation Center", "1465 W Booth Rd, Marietta, GA 30008"],
            ["First Baptist of Smyrna", "1275 Church St, Smyrna, GA 30080"],
        ],
        "notes": "★ = also open Sundays",
        "sources": [
            ["Cobb County Elections", "https://www.cobbcounty.org/elections"],
        ],
    },
    "Clayton": {
        "hours_summary": "Mon–Fri 8a–6p · Sat 9a–4p · Closed Sundays",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["Voter Registration & Elections Office (Annex 3)", "121 South McDonough St, Jonesboro, GA 30236"],
            ["Frank Bailey Senior Center", "6213 Riverdale Rd, Riverdale, GA 30274"],
            ["North Clayton Park & Recreation", "1346 Old Dixie Hwy, Hapeville, GA 30354"],
            ["Randy Poynter Library (Forest Park)", "696 Main St, Forest Park, GA 30297"],
            ["Morrow Center", "1180 Southlake Cir, Morrow, GA 30260"],
        ],
        "sources": [
            ["Clayton County Elections", "https://www.claytoncountyga.gov/government/elections-and-registration/"],
        ],
    },
    "Cherokee": {
        "hours_summary": "Apr 27 – May 9: 8:30a–5p · May 11–15: 8:30a–7p · Sun May 3 only at Elections Office, 1p–5p",
        "dates": "Apr 27 – May 15, 2026",
        "locations": [
            ["Elections & Voter Registration Office", "193 Lamar Haley Pkwy, Canton, GA 30114"],
            ["Ball Ground Public Library", "435 Old Canton Rd, Ball Ground, GA 30107"],
            ["Hickory Flat Public Library", "2740 E Cherokee Dr, Canton, GA 30115"],
            ["Rose Creek Public Library", "4476 Towne Lake Pkwy, Woodstock, GA 30189"],
            ["Oak Grove Fire Station Community Room", "100 Ridge Mill Ct, Acworth, GA 30102"],
            ["South Cherokee Annex / Rec Center", "7545 Main St, Woodstock, GA 30188"],
            ["Buzz Ahrens Recreation Center", "7345 Cumming Hwy, Canton, GA 30115"],
        ],
        "sources": [
            ["Cherokee County Elections", "https://cherokeegavotes.com/advance-voting-2/"],
        ],
    },
}

# Load TopoJSON to get all 159 county names
with open("ga-counties.json") as f:
    topo = json.load(f)

geoms = topo["objects"]["georgia-counties"]["geometries"]
all_counties = sorted({g["properties"]["NAME"] for g in geoms})
print(f"Counties in TopoJSON: {len(all_counties)}")

# Default state-wide hours (per O.C.G.A. § 21-2-385)
DEFAULT_HOURS = "Typically Mon–Fri 9a–5p · Sat May 9 (3rd Sat before): 9a–4p · Hours vary by county"

# Build the data dict
data = {}
for name in all_counties:
    if name in DETAILED:
        data[name] = DETAILED[name]
    else:
        data[name] = {
            "hours_summary": DEFAULT_HOURS,
            "dates": "Apr 27 – May 15, 2026",
            "locations": [],
            "placeholder": True,
            "sources": [
                ["My Voter Page", "https://mvp.sos.ga.gov/s/advanced-voting-location-information"],
                ["Georgia.gov early voting", "https://georgia.gov/vote-early-person"],
            ],
        }

with open("voting-locations.json", "w") as f:
    json.dump({
        "election": "Georgia 2026 Primary Election",
        "election_date": "May 19, 2026",
        "early_voting_period": "April 27 – May 15, 2026",
        "counties": data,
    }, f, indent=2, ensure_ascii=False)

print("voting-locations.json written")
print(f"Detailed: {len(DETAILED)} counties")
print(f"MVP fallback: {len(all_counties) - len(DETAILED)} counties")

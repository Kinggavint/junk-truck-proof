# The Junk Truck — Research Notes

## 1. Existing site: junktruck123.com

**What was on the existing page (fetched):**
- Page title: "Welcome To The Junk Truck!"
- Owner copy: Collin Grote (Kansas City native), emphasis on "not like big chains", "locally owned and operated", "you're part of our community"
- Service mentions: residential junk removal, commercial junk removal, storage unit cleanouts, same-day service, light moving, apartment relocation, courier/delivery
- Service area reference: Kansas City + surrounding suburbs, with call-outs to Union Station, The Legends Outlets, Power & Light District
- Differentiators: free estimates, upfront pricing, same-day, multiple payment options ("cash, credit cards, and checks"), full-service ("We Do The Heavy Lifting"), licensed and insured

**What was NOT on the existing page:**
- Phone number (none visible)
- Email (none visible)
- Business hours (none visible)
- Physical address (none visible)
- Real fleet photos (none visible)
- Logo image URL (none visible)
- Tagline text (none visible on home)

**Implication for the new site:** All phone/email/address info is placeholder in the new build. NOTES_FOR_CLIENT.md flags this for Collin to fill in at launch.

## 2. Competitive scan (KC junk removal market)

### 1-800-GOT-JUNK (national franchise)
- Pricing: volume-based (1/8 to full truckload), $129–$799+ range
- Structure: customer pays after job, on-site quote before work starts, "point and we'll make it disappear"
- CTA: "Schedule online" prominent
- Review count & brand recognition are their moat

### Junk King Kansas City (803 Woodswether Rd Ste B, KC MO 64105)
- Yelp rating: 4.2 (22 reviews)
- Pricing: volume-based (min / ½ / full tiers — "industry standard is single price, we do better")
- Dumpster rental option available for bigger projects
- Also a national franchise

### College HUNKS Hauling Junk
- National franchise with 200+ locations
- Service menu very broad: junk removal, donation pickup, moving, labor, packing, storage
- Eco pitch: "70% of everything we haul is recycled or donated"
- Brand positioning: "stress-free" + "college hunks" persona

### Takeaways for The Junk Truck's positioning
- All three major competitors are franchises with out-of-state parent companies.
- **Collin's biggest natural differentiator = "locally-owned, self-funded, not a franchise."** This should lead every page.
- Volume-based pricing ($125 single-item minimum up to $750+ full truck) is the industry standard — our blog pricing post mirrors this.
- "Same-day / next-day" is table stakes — included in copy.
- Recycling/donation is table stakes for modern brands — included.
- Upfront on-site pricing before work starts is table stakes — included.

## 3. KC metro SEO target keywords

### Primary (metro-wide)
- junk removal Kansas City
- junk removal near me
- KC junk hauling
- bulk pickup Kansas City
- local junk removal companies
- same-day junk removal Kansas City
- estate cleanout Kansas City

### Suburb-specific (high-intent local)
- junk removal Overland Park KS
- junk removal Olathe KS
- junk removal Lee's Summit MO
- junk removal Leawood KS
- junk removal Shawnee KS
- junk removal Independence MO
- junk removal Blue Springs MO
- junk removal Liberty MO
- bulk pickup Overland Park
- garage cleanout Olathe

### Service-specific
- house cleanout Kansas City
- apartment cleanout KC
- garage cleanout Kansas City
- yard waste removal KC
- construction debris pickup Kansas City
- estate cleanout services KC
- HOA bulk pickup Kansas City

These are woven into page titles, H1s, meta descriptions, and natural body copy throughout the site.

## 4. KC demographic snapshot for service targeting

- KC metro population: ~2.2M across MO + KS side
- Senior population (60+): notable concentration in Prairie Village, Leawood, and Lee's Summit — **good target for estate cleanout messaging**
- Fastest-growing suburbs (new construction): Lee's Summit, Olathe, Liberty — good target for construction cleanup and move-in/move-out services
- Rental-heavy zips: 64111 (Westport), 64108 (Crossroads), 66212 (OP) — good target for apartment cleanout messaging
- HOA density: Leawood, Overland Park, Lee's Summit, Liberty — perfect target for HOA bulk item days

## 5. Design direction — what I chose and why

### Palette chosen: **Deep Charcoal + Safety Orange + Off-White Cream**
- **--ink: #141820** (near-black charcoal): professional anchor, works for dark sections and copy
- **--orange: #ff6b1a** (safety orange): high-energy accent, nods to construction/industrial work trucks, high visibility, "hustle" feel
- **--cream: #f7f3ec** (off-white paper): warm, local, grounded, avoids the "AI-slop pure-white" aesthetic
- **--bone: #ede7db** for alternating section fills
- Yellow and green tokens defined but unused in v1 — reserved for future expansion

**Why this palette:**
- Collin wanted "funky/fun logo but presented professionally" + signed off "To the Moon, baby!" = energetic, not corporate.
- Orange is recognizable as blue-collar / construction / safety — reads as "guys who actually work" vs. "corporate franchise."
- Charcoal instead of navy keeps it more premium and flexible if Collin's eventual brand color is blue, green, or red — charcoal plays nicely with anything.
- Cream over white gives it a local, indie, editorial feel — the "Jeni's Ice Cream vs. Baskin-Robbins" distinction Erik specified.

**Alternative considered:** dark green + bright red-orange (Kellerbauer-style contractor aesthetic). Rejected because orange alone is more distinctive in a market saturated with blue (1-800-GOT-JUNK) and red (Junk King).

### Typography
- **Display:** Archivo Black (Google Fonts) — heavy, condensed-feel, all caps, aggressive. Reads like moving-company signage. Fallback to Anton and Arial Black.
- **Body:** Inter — neutral, highly legible, free from Google Fonts.
- Display is used in ALL CAPS for headlines. Sans is used normal-case for all body and utility text.

### Motion
- Intersection-observer `fadeUp` on sections (600ms ease).
- Button hover lifts (translateY -2px) with shadow bloom.
- Service card hover: flip to dark theme with orange icon.
- Subtle — not flashy. Keeps the professional credibility.

### Photography direction
- All AI-generated, all residential-driveway / suburban-Midwest vibe.
- No faces on talent (only backs/distance shots where workers appear).
- Warm golden-hour light across the set — consistent brand look.
- 6 hero/feature images total, all served as webp < 325KB.

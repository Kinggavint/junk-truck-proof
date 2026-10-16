#!/usr/bin/env python3
"""
Static site generator for The Junk Truck.
Produces 13 HTML files from templates + content dicts. No runtime build step needed
after this runs — the output is plain HTML served from GitHub Pages.
"""

import os
from textwrap import dedent

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = ROOT

SITE = {
    "name": "The Junk Truck",
    "tagline": "We Haul It All.",
    "city": "Kansas City",
    "region": "MO",
    "phone_display": "Call for a quote",   # real phone not provided — placeholder
    "phone_tel": "",                        # leave blank, falls back to button text
    "email": "hello@junktruck123.com",      # placeholder — noted in NOTES
    "url": "https://kinggavint.github.io/junk-truck-proof",
}

# ---------- SVG logo (inline wordmark placeholder) ----------
LOGO_SVG = '''<svg viewBox="0 0 44 44" aria-label="The Junk Truck" role="img" xmlns="http://www.w3.org/2000/svg">
  <rect x="1" y="1" width="42" height="42" rx="8" fill="#141820"/>
  <path d="M6 26 L6 18 L22 18 L26 14 L34 14 L38 18 L38 26 Z" fill="none" stroke="#ff6b1a" stroke-width="2.5" stroke-linejoin="round"/>
  <circle cx="13" cy="30" r="3" fill="none" stroke="#ff6b1a" stroke-width="2.5"/>
  <circle cx="31" cy="30" r="3" fill="none" stroke="#ff6b1a" stroke-width="2.5"/>
  <rect x="28" y="19" width="6" height="5" fill="#ff6b1a"/>
</svg>'''

# ---------- Nav (same across all pages) ----------
NAV_ITEMS = [
    ("Home", "index.html"),
    ("Services", "services.html"),
    ("Service Area", "locations.html"),
    ("About", "about.html"),
    ("Blog", "blog.html"),
    ("FAQ", "faq.html"),
]

SERVICES = [
    {
        "slug": "junk-removal",
        "title": "Junk Removal",
        "short": "Single items to full-home hauls — furniture, appliances, electronics, you name it.",
        "icon": "box",
        "scenarios": "Moving out, downsizing, clearing a basement, replacing furniture.",
        "included": [
            "All lifting, loading, and hauling",
            "Cleanup of the pickup area",
            "Responsible recycling and donation when possible",
            "Same-day service when available",
        ],
    },
    {
        "slug": "bulk-item-removal",
        "title": "Bulk Item Removal",
        "short": "Couches, mattresses, fridges, hot tubs — the big stuff municipal trash won't take.",
        "icon": "sofa",
        "scenarios": "Replacing a mattress or sofa, upgrading appliances, clearing out a workout room.",
        "included": [
            "Pickup direct from any room — we do the heavy lifting",
            "Proper disposal of mattresses and appliances",
            "Freon handling for refrigerators and freezers",
            "No stairs or doorway charge",
        ],
    },
    {
        "slug": "house-clean-outs",
        "title": "House Clean-Outs",
        "short": "Whole-home clears for move-outs, foreclosures, rentals, or downsizing.",
        "icon": "home",
        "scenarios": "Prepping a house for sale, post-move-out, landlord turnover, hoarding recovery.",
        "included": [
            "Room-by-room clearing from top to bottom",
            "Sorting items for donation, recycling, or disposal",
            "Sweeping up after the job is done",
            "Discreet, respectful service",
        ],
    },
    {
        "slug": "apartment-clean-outs",
        "title": "Apartment Clean-Outs",
        "short": "Fast, clean move-out hauls that meet your landlord's deadline.",
        "icon": "building",
        "scenarios": "Breaking a lease, moving cross-country, evictions, new tenant turnover.",
        "included": [
            "Stair and elevator-friendly crews",
            "Protection for floors, walls, and trim",
            "Complete unit clearing in a single visit",
            "Fast turnaround for deadline-sensitive jobs",
        ],
    },
    {
        "slug": "garage-clean-outs",
        "title": "Garage Clean-Outs",
        "short": "Reclaim your garage — old tools, bikes, paint cans, broken furniture, you name it.",
        "icon": "garage",
        "scenarios": "Making room for a car, selling a home, spring cleaning, post-project cleanup.",
        "included": [
            "Full-garage sweep, floor to rafters",
            "Hazardous item disposal guidance (paint, chemicals)",
            "Metals, scrap, and electronics handled separately",
            "Floor-swept clean when we're done",
        ],
    },
    {
        "slug": "construction-clean-ups",
        "title": "Construction Clean-Ups",
        "short": "Post-remodel, demo, and punch-list debris cleared so your crew can close out.",
        "icon": "tools",
        "scenarios": "End of a remodel, demo-day debris, roofing tear-offs, flooring replacements.",
        "included": [
            "Drywall, lumber, flooring, and general debris",
            "On-site bins available for bigger projects",
            "Coordination with your GC or project manager",
            "Jobsite left broom-clean",
        ],
    },
    {
        "slug": "yard-waste-removal",
        "title": "Yard Waste Removal",
        "short": "Branches, brush, bagged leaves, old mulch, dirt piles — gone.",
        "icon": "leaf",
        "scenarios": "Post-storm cleanup, tree trimming, landscape renovation, seasonal yard prep.",
        "included": [
            "Branches, brush, and tree limbs up to a truckload",
            "Bagged leaves, grass, and sod",
            "Old mulch, dirt, and landscape rock",
            "Curbside or back-yard pickup — your call",
        ],
    },
    {
        "slug": "estate-sale-clean-outs",
        "title": "Estate Sale Clean-Outs",
        "short": "Respectful, discreet clears after an estate sale or loss. We handle it so you don't have to.",
        "icon": "heart",
        "scenarios": "Post-estate-sale leftovers, downsizing a parent's home, probate clean-outs.",
        "included": [
            "Compassionate, no-pressure service",
            "Sorting items for donation vs. disposal",
            "Coordination with realtors and estate attorneys",
            "Everything hauled in one visit when possible",
        ],
    },
    {
        "slug": "hoa-bulk-item-days",
        "title": "HOA Bulk Item Days",
        "short": "Scheduled neighborhood clean-ups — one truck, one day, no hassle for your board.",
        "icon": "community",
        "scenarios": "HOA-scheduled pickup days, neighborhood beautification events, apartment community purges.",
        "included": [
            "Fixed-fee, fixed-day community service",
            "Multiple stops per block in one pass",
            "Flyers and resident communication support",
            "Board-friendly reporting after each run",
        ],
    },
]

LOCATIONS = [
    ("Kansas City", "MO", "The heart of the metro — from the Plaza to the Northland, we haul it all.", "64108, 64111, 64112, 64114, 64116, 64118, 64119, 64123, 64129, 64130, 64132, 64134, 64137, 64145, 64146, 64151, 64152, 64153, 64154, 64155, 64158"),
    ("Kansas City", "KS", "Wyandotte County pickups, from Rosedale to the Legends.", "66101, 66102, 66103, 66104, 66105, 66106, 66109, 66111, 66112"),
    ("Overland Park", "KS", "Johnson County's largest city — same-day service on most jobs.", "66204, 66207, 66210, 66212, 66213, 66214, 66221, 66223, 66224"),
    ("Olathe", "KS", "Fast pickup across Olathe neighborhoods and new builds.", "66061, 66062, 66063"),
    ("Lee's Summit", "MO", "One of KC's fastest-growing suburbs — we know the streets.", "64063, 64064, 64081, 64082, 64086"),
    ("Independence", "MO", "Historic Independence to eastern suburbs — reliable local service.", "64050, 64052, 64053, 64055, 64056, 64057, 64058"),
    ("Shawnee", "KS", "Quick response across Shawnee and Shawnee Mission neighborhoods.", "66203, 66216, 66217, 66218, 66226"),
    ("Blue Springs", "MO", "Eastern metro pickups — residential and light commercial.", "64014, 64015, 64029"),
    ("Liberty", "MO", "Clay County service for Liberty, Pleasant Valley, and surrounding areas.", "64068"),
    ("Gladstone", "MO", "Northland clean-outs and bulk pickup, fast.", "64118, 64119"),
    ("Raytown", "MO", "Community-focused service for Raytown homeowners.", "64133, 64138"),
    ("Belton", "MO", "Cass County pickups, including Belton, Peculiar, and Raymore.", "64012"),
    ("Grandview", "MO", "Grandview and Martin City residential and commercial hauls.", "64030"),
    ("Mission", "KS", "Mission, Mission Hills, and Mission Woods — on time, every time.", "66202, 66205"),
    ("Prairie Village", "KS", "Quiet residential pickups with zero hassle.", "66206, 66208"),
    ("Leawood", "KS", "Estate and large-home clean-outs done right.", "66206, 66209, 66211, 66224"),
]

FAQS = [
    ("How does junk removal pricing work?",
     "We price by volume — how much space your stuff takes up in the truck. We'll take a look, give you a firm quote before we start, and that's the price. No hidden fees, no surprises. Single-item pickups (like a mattress or a couch) have a flat rate. Bigger jobs are priced by quarter, half, and full truck loads."),
    ("What areas do you serve?",
     "The entire Kansas City metro — both sides of the state line. That includes Kansas City MO and KS, Overland Park, Olathe, Lee's Summit, Independence, Shawnee, Blue Springs, Liberty, Leawood, Prairie Village, and every suburb in between. If you're not sure, just ask."),
    ("What items can't you take?",
     "A few things local regulations don't let us haul: hazardous waste, wet paint (dry it out first and we'll grab it), automotive fluids, medical waste, and asbestos. Pretty much everything else is fair game."),
    ("Do I need to be home during pickup?",
     "Not always. If you can leave the items on the driveway, curb, or in an unlocked garage, we can handle it and send you a photo when we're done. For inside pickups we do need an adult on-site."),
    ("How far in advance do I need to book?",
     "Same-day and next-day slots are common. Weekends and the first of the month fill up faster, so if you've got a tight deadline (like a move-out date), book a few days ahead if you can."),
    ("Do you recycle?",
     "Whenever possible, yes. Metals, electronics, and donation-worthy furniture get a second life. We partner with local donation centers so usable items find new homes instead of the landfill."),
    ("Are you insured?",
     "Yes. The Junk Truck is fully licensed and insured for residential and commercial jobs. Proof of insurance available on request, especially helpful for HOA and property management jobs."),
    ("What makes The Junk Truck different?",
     "We're locally owned and operated — not a franchise, not a chain. This company was started from scratch and self-funded by Collin Grote, a Kansas City native. That means every dollar you spend stays local, and every decision is made by someone who actually lives here. We show up, we show up on time, and we show up looking professional. Backed by a 100% satisfaction guarantee."),
    ("Do you do estate cleanouts?",
     "Absolutely. Estate and downsizing clean-outs are one of our specialties. We work carefully and discreetly, coordinate with realtors and attorneys when needed, and can sort items for donation rather than disposal. No one should have to handle an estate clear-out alone."),
    ("What's your 100% satisfaction guarantee?",
     "Simple: if you're not happy with the job, we'll make it right. Whether that means coming back to finish, adjusting the bill, or something else — we stand behind the work. Your word goes."),
]

ICONS = {
    "box": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>''',
    "sofa": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 9V7a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M10 9V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v2"/><path d="M2 11v5a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-5a2 2 0 0 0-4 0v2H6v-2a2 2 0 0 0-4 0Z"/><line x1="6" y1="18" x2="6" y2="20"/><line x1="18" y1="18" x2="18" y2="20"/></svg>''',
    "home": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>''',
    "building": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M8 10h.01"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 14h.01"/><path d="M16 14h.01"/><path d="M12 14h.01"/></svg>''',
    "garage": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10 12 3l9 7"/><path d="M5 10v10h14V10"/><path d="M7 14h10"/><path d="M7 18h10"/></svg>''',
    "tools": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76Z"/></svg>''',
    "leaf": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19.2 2c1 1.5 2 5 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>''',
    "heart": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78Z"/></svg>''',
    "community": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>''',
    "phone": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>''',
    "check": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>''',
    "clock": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>''',
    "shield": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1Z"/></svg>''',
    "pin": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 7-8 13-8 13s-8-6-8-13a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>''',
    "arrow": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>''',
    "upload": '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>''',
}

def icon(name, cls=""):
    svg = ICONS.get(name, "")
    if cls:
        svg = svg.replace("<svg ", f'<svg class="{cls}" ')
    return svg


def build_nav(active_page):
    links = ""
    for label, href in NAV_ITEMS:
        cls = "active" if href == active_page else ""
        links += f'<li><a href="{href}" class="{cls}">{label}</a></li>\n'

    mobile_links = ""
    for label, href in NAV_ITEMS:
        mobile_links += f'<li><a href="{href}">{label}</a></li>\n'

    return f'''<a href="#main" class="skip-link">Skip to main content</a>
<header class="site-header">
  <div class="container">
    <div class="nav">
      <a href="index.html" class="brand" aria-label="The Junk Truck home">
        {LOGO_SVG}
        <span class="brand-text">The Junk Truck<small>Kansas City · We Haul It All</small></span>
      </a>
      <nav aria-label="Primary">
        <ul class="nav-links">
          {links}
        </ul>
      </nav>
      <div class="nav-cta">
        <a href="book.html" class="btn btn-primary">Book a Pickup</a>
      </div>
      <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-menu" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div id="mobile-menu" class="mobile-menu" role="navigation" aria-label="Mobile">
    <ul>
      {mobile_links}
      <li><a href="book.html" class="btn btn-primary">Book a Pickup</a></li>
    </ul>
  </div>
</header>
'''


def build_footer():
    service_links = ""
    for s in SERVICES[:6]:
        service_links += f'<li><a href="services.html#{s["slug"]}">{s["title"]}</a></li>\n'
    location_links = ""
    for loc in LOCATIONS[:6]:
        location_links += f'<li><a href="locations.html">{loc[0]}, {loc[1]}</a></li>\n'

    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="brand">
          {LOGO_SVG}
          <span class="brand-text">The Junk Truck<small>KC · We Haul It All</small></span>
        </div>
        <p>Locally owned and operated in Kansas City since day one. Not a franchise, not a chain — just a local crew that shows up on time and hauls it all away.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{service_links}</ul>
      </div>
      <div>
        <h4>Service Area</h4>
        <ul>{location_links}</ul>
      </div>
      <div>
        <h4>Get a Quote</h4>
        <ul>
          <li><a href="book.html">Book a Pickup</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="blog.html">Blog</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      <div>© 2026 The Junk Truck. All rights reserved.</div>
      <div>Kansas City, MO · Locally owned &amp; operated</div>
    </div>
  </div>
</footer>
<script src="js/main.js" defer></script>
'''


def build_head(title, description, active_page, extra_schema=""):
    canonical = f"{SITE['url']}/{active_page}"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE['url']}/assets/images/hero-truck.webp">
  <meta property="og:locale" content="en_US">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="css/styles.css">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 44 44'%3E%3Crect x='1' y='1' width='42' height='42' rx='8' fill='%23141820'/%3E%3Cpath d='M6 26 L6 18 L22 18 L26 14 L34 14 L38 18 L38 26 Z' fill='none' stroke='%23ff6b1a' stroke-width='2.5' stroke-linejoin='round'/%3E%3Ccircle cx='13' cy='30' r='3' fill='none' stroke='%23ff6b1a' stroke-width='2.5'/%3E%3Ccircle cx='31' cy='30' r='3' fill='none' stroke='%23ff6b1a' stroke-width='2.5'/%3E%3Crect x='28' y='19' width='6' height='5' fill='%23ff6b1a'/%3E%3C/svg%3E">
  <meta name="theme-color" content="#141820">

  {extra_schema}
</head>
<body>
'''


# -------- BLOG POSTS --------
BLOG_POSTS = [
    {
        "slug": "junk-removal-cost-kansas-city",
        "title": "How Much Does Junk Removal Cost in Kansas City?",
        "summary": "A straight-talk breakdown of what KC homeowners actually pay for junk hauling in 2026 — and how to avoid surprise fees.",
        "date": "2026-04-15",
        "category": "Pricing",
        "read_min": 6,
        "thumb": "hero-truck.webp",
        "full": True,
    },
    {
        "slug": "estate-cleanout-checklist",
        "title": "5 Things to Know Before an Estate Cleanout",
        "summary": "Estate clean-outs are emotional and overwhelming. Here's how to approach one in the KC metro without burning out.",
        "date": "2026-04-02",
        "category": "Estate",
        "read_min": 7,
        "thumb": "clean-interior.webp",
        "full": True,
    },
    {
        "slug": "garage-cleanout-checklist",
        "title": "The Ultimate Garage Cleanout Checklist",
        "summary": "A weekend-ready checklist for reclaiming your garage — what to keep, what to toss, what to haul away.",
        "date": "2026-03-20",
        "category": "How-to",
        "read_min": 5,
        "thumb": "garage-cleanout.webp",
        "full": False,
    },
    {
        "slug": "what-junk-removal-wont-take",
        "title": "What Junk Removal Companies Won't Take (and Why)",
        "summary": "Hazardous materials, wet paint, medical waste — here's the short list of items we can't haul, plus what to do instead.",
        "date": "2026-03-05",
        "category": "FAQ",
        "read_min": 4,
        "thumb": "construction-debris.webp",
        "full": False,
    },
    {
        "slug": "moving-out-junk-removal-guide",
        "title": "Moving Out? Here's Your Junk Removal Guide",
        "summary": "Move-out deadlines are ruthless. Use this 2-week plan to clear the junk before the truck arrives.",
        "date": "2026-02-18",
        "category": "Moving",
        "read_min": 5,
        "thumb": "crew-loading.webp",
        "full": False,
    },
    {
        "slug": "hoa-bulk-pickup-guide",
        "title": "HOA Bulk Pickup Days: A Homeowner's Guide",
        "summary": "Missed your HOA's bulk pickup day? Here's what KC homeowners should do next — and how to get ready for the next one.",
        "date": "2026-02-01",
        "category": "Community",
        "read_min": 4,
        "thumb": "yard-waste.webp",
        "full": False,
    },
]


# ---------- Pages ----------

def page_home():
    title = f"Kansas City Junk Removal — We Haul It All | {SITE['name']}"
    desc = "Locally owned junk removal serving Kansas City, Overland Park, Olathe, Lee's Summit and the entire KC metro. We show up on time, haul it all, and back it with a 100% satisfaction guarantee."

    schema = dedent(f'''
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "@id": "{SITE['url']}#business",
      "name": "The Junk Truck",
      "description": "Locally owned junk removal and hauling company serving the Kansas City metro.",
      "url": "{SITE['url']}",
      "telephone": "+1-816-298-9995",
      "priceRange": "$$",
      "image": "{SITE['url']}/assets/images/hero-truck.webp",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Kansas City",
        "addressRegion": "MO",
        "addressCountry": "US"
      }},
      "areaServed": [
        {{"@type": "City", "name": "Kansas City, MO"}},
        {{"@type": "City", "name": "Kansas City, KS"}},
        {{"@type": "City", "name": "Overland Park, KS"}},
        {{"@type": "City", "name": "Olathe, KS"}},
        {{"@type": "City", "name": "Lee's Summit, MO"}},
        {{"@type": "City", "name": "Independence, MO"}},
        {{"@type": "City", "name": "Shawnee, KS"}},
        {{"@type": "City", "name": "Blue Springs, MO"}},
        {{"@type": "City", "name": "Liberty, MO"}},
        {{"@type": "City", "name": "Leawood, KS"}},
        {{"@type": "City", "name": "Prairie Village, KS"}}
      ],
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 39.0997,
        "longitude": -94.5786
      }},
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "Junk Removal Services",
        "itemListElement": [
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Residential Junk Removal"}}}},
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Bulk Item Removal"}}}},
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "House Clean-Outs"}}}},
          {{"@type": "Offer", "itemOffered": {{"@type": "Service", "name": "Estate Sale Clean-Outs"}}}}
        ]
      }}
    }}
    </script>''')

    # Service cards grid
    service_cards = ""
    for s in SERVICES:
        service_cards += f'''<a href="services.html#{s["slug"]}" class="service-card">
          <span class="service-icon">{icon(s["icon"])}</span>
          <span class="arrow">{icon("arrow")}</span>
          <h3>{s["title"]}</h3>
          <p>{s["short"]}</p>
        </a>\n'''

    # Blog teaser — 3 most recent
    blog_cards = ""
    for post in BLOG_POSTS[:3]:
        href = f"blog/{post['slug']}.html"
        blog_cards += f'''<a href="{href}" class="post-card">
          <div class="thumb"><img src="assets/images/{post['thumb']}" alt="" loading="lazy"></div>
          <div class="body">
            <div class="meta">{post['category']} · {post['read_min']} min read</div>
            <h3>{post['title']}</h3>
            <p>{post['summary']}</p>
            <span class="read-more">Read article →</span>
          </div>
        </a>\n'''

    # Top 3 FAQ
    faq_html = ""
    for q, a in FAQS[:3]:
        faq_html += f'''<details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>\n'''

    body = f'''
<main id="main">

<!-- HERO -->
<section class="hero" aria-labelledby="hero-heading">
  <div class="container">
    <div class="hero-inner">
      <span class="eyebrow">Kansas City · Locally Owned</span>
      <h1 id="hero-heading">We Haul<br><span class="accent-word">It All.</span></h1>
      <p class="lead">From a single couch to a full house cleanout — The Junk Truck shows up on time, takes care of the heavy lifting, and leaves your space broom-clean. Serving the entire KC metro.</p>
      <div class="btn-group">
        <a href="book.html" class="btn btn-primary btn-lg">Get a Free Quote</a>
        <a href="services.html" class="btn btn-outline btn-lg">See Services</a>
      </div>
      <div class="hero-meta">
        <span class="item">{icon("check")} 100% Satisfaction</span>
        <span class="item">{icon("clock")} On-Time, Every Time</span>
        <span class="item">{icon("shield")} Licensed &amp; Insured</span>
        <span class="item">{icon("pin")} KC Metro-Wide</span>
      </div>
    </div>
  </div>
</section>

<!-- WHY US -->
<section class="section section-dark" aria-labelledby="why-heading">
  <div class="container">
    <span class="eyebrow">Why The Junk Truck</span>
    <h2 id="why-heading" style="max-width: 18ch;">Local pride. Hard work.<br>No franchise fees.</h2>
    <p class="lead max-measure" style="color: var(--bone);">This isn't a call center shipping you off to the nearest location. It's a Kansas City native who started this company from scratch, self-funded, and backs every job personally.</p>
    <div class="feature-row" style="margin-top: var(--s-7);">
      <div class="feature">
        <span class="num">01</span>
        <h3>Locally Owned</h3>
        <p>Not a franchisee. Not a chain. Every dollar stays in the KC metro.</p>
      </div>
      <div class="feature">
        <span class="num">02</span>
        <h3>On Time, Every Time</h3>
        <p>We respect your schedule. If we say 10am, we're there at 10am.</p>
      </div>
      <div class="feature">
        <span class="num">03</span>
        <h3>Professional Crew</h3>
        <p>Clean trucks. Clean uniforms. Careful work. We look the part because we are the part.</p>
      </div>
      <div class="feature">
        <span class="num">04</span>
        <h3>100% Satisfaction</h3>
        <p>If you're not happy, we make it right. Full stop. That's our guarantee.</p>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="section" aria-labelledby="services-heading">
  <div class="container">
    <div style="max-width: 720px; margin-bottom: var(--s-6);">
      <span class="eyebrow">What We Haul</span>
      <h2 id="services-heading">If it fits in the truck,<br>it's <span class="accent">out of your life.</span></h2>
      <p class="lead text-muted">Nine services, one truck, zero hassle. Residential and light commercial jobs across Kansas City and the surrounding metro.</p>
    </div>
    <div class="grid grid-3">
      {service_cards}
    </div>
    <div style="margin-top: var(--s-6);">
      <a href="services.html" class="btn btn-outline">See all services {icon("arrow")}</a>
    </div>
  </div>
</section>

<!-- SERVICE AREA TEASER -->
<section class="section" style="background: var(--bone);" aria-labelledby="area-heading">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Service Area</span>
        <h2 id="area-heading">The whole KC metro. Both sides of the line.</h2>
        <p class="lead text-muted">From the Plaza to Olathe, from Lee's Summit to Liberty — we know these streets. Not sure if we cover your zip? Just ask.</p>
        <ul class="check-list" style="list-style:none; padding:0;">
          <li style="padding-left: 28px; position: relative; margin-bottom: var(--s-2);">Kansas City MO &amp; KS, Overland Park, Olathe</li>
          <li style="padding-left: 28px; position: relative; margin-bottom: var(--s-2);">Lee's Summit, Independence, Blue Springs, Liberty</li>
          <li style="padding-left: 28px; position: relative; margin-bottom: var(--s-2);">Leawood, Prairie Village, Shawnee, Mission</li>
        </ul>
        <a href="locations.html" class="btn btn-outline">See full service area {icon("arrow")}</a>
      </div>
      <div class="service-area-map">
        {kc_metro_svg_map()}
        <p style="margin-top: var(--s-4); color: var(--bone); font-size: 0.9rem;">16+ KC metro cities served</p>
      </div>
    </div>
  </div>
</section>

<!-- BLOG TEASER -->
<section class="section" aria-labelledby="blog-teaser-heading">
  <div class="container">
    <div style="display:flex; justify-content:space-between; align-items:end; flex-wrap:wrap; gap: var(--s-4); margin-bottom: var(--s-6);">
      <div>
        <span class="eyebrow">From the blog</span>
        <h2 id="blog-teaser-heading">Straight-up KC junk advice.</h2>
      </div>
      <a href="blog.html" class="btn btn-outline">All articles {icon("arrow")}</a>
    </div>
    <div class="blog-grid">
      {blog_cards}
    </div>
  </div>
</section>

<!-- FAQ TEASER -->
<section class="section" style="background: var(--bone);" aria-labelledby="faq-teaser-heading">
  <div class="container">
    <div style="max-width: 760px;">
      <span class="eyebrow">Common Questions</span>
      <h2 id="faq-teaser-heading">Real answers.<br>No run-around.</h2>
      <div class="accordion">
        {faq_html}
      </div>
      <a href="faq.html" class="btn btn-outline" style="margin-top: var(--s-6);">See all FAQs {icon("arrow")}</a>
    </div>
  </div>
</section>

<!-- FINAL CTA -->
<section class="cta-band">
  <div class="container">
    <h2>Ready to clear it out?</h2>
    <p class="lead" style="color: #fff; margin: 0 auto var(--s-5); max-width: 540px;">Free, no-obligation quotes. Same-day pickup when we can swing it.</p>
    <div class="btn-group" style="justify-content: center;">
      <a href="book.html" class="btn btn-lg">Book a Pickup</a>
      <a href="services.html" class="btn btn-outline btn-lg">See Services</a>
    </div>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "index.html", schema) + build_nav("index.html") + body + build_footer() + "</body></html>"


def kc_metro_svg_map():
    # Stylized service-area map of KC metro (abstract, not geographic pinpoints)
    return '''<svg viewBox="0 0 600 400" aria-label="Kansas City metro service area" role="img" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;">
  <defs>
    <pattern id="dots" patternUnits="userSpaceOnUse" width="16" height="16">
      <circle cx="2" cy="2" r="1" fill="#ff6b1a" opacity="0.3"/>
    </pattern>
  </defs>
  <!-- State line -->
  <line x1="300" y1="20" x2="300" y2="380" stroke="#ff6b1a" stroke-width="2" stroke-dasharray="6 6" opacity="0.6"/>
  <text x="260" y="16" font-family="Inter, sans-serif" font-size="11" fill="#ff6b1a" font-weight="700" text-anchor="end">KS</text>
  <text x="340" y="16" font-family="Inter, sans-serif" font-size="11" fill="#ff6b1a" font-weight="700">MO</text>
  <!-- Service area blob -->
  <path d="M 100 120 Q 180 60 300 70 Q 420 60 510 130 Q 540 220 490 300 Q 400 360 300 340 Q 180 360 110 290 Q 70 210 100 120 Z"
        fill="url(#dots)" stroke="#ff6b1a" stroke-width="2" opacity="0.9"/>
  <!-- City labels -->
  <g font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#f7f3ec" text-anchor="middle">
    <circle cx="310" cy="180" r="6" fill="#ff6b1a"/>
    <text x="310" y="165">KC Metro</text>

    <circle cx="220" cy="230" r="4" fill="#f7f3ec"/>
    <text x="220" y="250">Overland Park</text>

    <circle cx="170" cy="280" r="4" fill="#f7f3ec"/>
    <text x="170" y="300">Olathe</text>

    <circle cx="410" cy="240" r="4" fill="#f7f3ec"/>
    <text x="410" y="260">Lee's Summit</text>

    <circle cx="380" cy="170" r="4" fill="#f7f3ec"/>
    <text x="380" y="155">Independence</text>

    <circle cx="260" cy="160" r="4" fill="#f7f3ec"/>
    <text x="255" y="145">Shawnee</text>

    <circle cx="340" cy="110" r="4" fill="#f7f3ec"/>
    <text x="340" y="100">Liberty</text>

    <circle cx="245" cy="190" r="4" fill="#f7f3ec"/>
    <text x="245" y="210">Leawood</text>

    <circle cx="450" cy="280" r="4" fill="#f7f3ec"/>
    <text x="450" y="300">Blue Springs</text>
  </g>
</svg>'''


def page_about():
    title = f"About The Junk Truck | Locally Owned KC Junk Removal"
    desc = "Meet Collin Grote, owner of The Junk Truck — a Kansas City native who built a locally-owned, self-funded junk removal company from the ground up."

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">About</span>
    <h1>Started from scratch.<br><span style="color: var(--orange);">Still swinging.</span></h1>
    <p class="lead">The Junk Truck is a Kansas City native son's take on what a local hauling company should be: on time, in uniform, and proud of the work.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Our Story</span>
        <h2>Locally owned.<br>Self-funded.<br>Not a franchise.</h2>
        <p class="lead text-muted">The Junk Truck was built from the ground up by Collin Grote, a Kansas City native who was tired of seeing the local service industry get swallowed up by out-of-state franchise call centers.</p>
        <p>No franchise fee. No corporate playbook written in another city. Just a local owner, a hardworking crew, and a simple promise: show up, show up on time, show up looking professional — and treat every customer like a neighbor.</p>
        <p>That commitment to the community is why we lean into "Shop Local" on every truck we send out. When you hire The Junk Truck, every dollar stays right here in the KC metro.</p>
      </div>
      <div class="img-wrap">
        <img src="assets/images/hero-truck.webp" alt="A clean Junk Truck parked in a Kansas City residential driveway at golden hour" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    <span class="eyebrow">What We Stand For</span>
    <h2 style="max-width: 16ch;">Four promises.<br>Every single job.</h2>
    <div class="feature-row" style="margin-top: var(--s-7);">
      <div class="feature">
        <span class="num">01</span>
        <h3>Show Up</h3>
        <p>When we say we'll be there, we're there. Dispatch sends updates so you're never guessing.</p>
      </div>
      <div class="feature">
        <span class="num">02</span>
        <h3>Show Up On Time</h3>
        <p>Your time matters. We give tight windows and hit them — no 4-hour "somewhere between" nonsense.</p>
      </div>
      <div class="feature">
        <span class="num">03</span>
        <h3>Show Up Professional</h3>
        <p>Clean trucks. Uniformed crew. Respectful of your home, your yard, and your neighbors.</p>
      </div>
      <div class="feature">
        <span class="num">04</span>
        <h3>100% Satisfaction</h3>
        <p>If you're not happy, we make it right. Our name's on the truck — our word's behind it.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split reverse">
      <div>
        <span class="eyebrow">Shop Local</span>
        <h2>Kansas City is our neighborhood.</h2>
        <p class="lead text-muted">Every cleanout we haul stays local. Usable items go to KC-area donation centers. Metals and electronics go to local recyclers. The rest gets disposed of responsibly — no out-of-state shortcuts.</p>
        <p>When you hire us, you're not just clearing out your garage. You're keeping a local crew employed, supporting KC-area donation partners, and making sure your dollar works for your community.</p>
        <a href="services.html" class="btn btn-primary" style="margin-top: var(--s-4);">See what we haul {icon("arrow")}</a>
      </div>
      <div class="img-wrap">
        <img src="assets/images/clean-interior.webp" alt="A clean, empty home interior with natural light — after a Junk Truck house clean-out" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Let's clear it out.</h2>
    <p class="lead" style="color:#fff; margin: 0 auto var(--s-5); max-width: 540px;">Free quote, no pressure, no franchise-fee markup.</p>
    <a href="book.html" class="btn btn-lg">Book a Pickup</a>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "about.html") + build_nav("about.html") + body + build_footer() + "</body></html>"


def page_services():
    title = f"Services — Junk Removal, Cleanouts &amp; Hauling | {SITE['name']}"
    desc = "Nine ways The Junk Truck helps KC homeowners clear out. Residential junk removal, estate clean-outs, garage cleanouts, yard waste, HOA bulk days and more."

    # Service detail sections
    service_sections = ""
    for i, s in enumerate(SERVICES):
        img_map = {
            "junk-removal": "hero-truck.webp",
            "bulk-item-removal": "crew-loading.webp",
            "house-clean-outs": "clean-interior.webp",
            "apartment-clean-outs": "clean-interior.webp",
            "garage-clean-outs": "garage-cleanout.webp",
            "construction-clean-ups": "construction-debris.webp",
            "yard-waste-removal": "yard-waste.webp",
            "estate-sale-clean-outs": "clean-interior.webp",
            "hoa-bulk-item-days": "crew-loading.webp",
        }
        img = img_map.get(s["slug"], "hero-truck.webp")
        included_html = "\n".join(f'<li>{item}</li>' for item in s["included"])
        reverse_cls = " reverse" if i % 2 == 1 else ""
        service_sections += f'''
<section class="service-detail" id="{s['slug']}">
  <div class="container">
    <div class="service-detail-grid{reverse_cls}">
      <div>
        <span class="pill">{s['title']}</span>
        <h2 style="margin-top: var(--s-3);">{s['title']}</h2>
        <div class="divider"></div>
        <p class="lead">{s['short']}</p>
        <h4 style="margin-top: var(--s-5);">What's included</h4>
        <ul class="check-list">
          {included_html}
        </ul>
        <p style="margin-top: var(--s-4);"><strong>Typical jobs:</strong> {s['scenarios']}</p>
        <a href="book.html" class="btn btn-primary" style="margin-top: var(--s-3);">Request a quote {icon("arrow")}</a>
      </div>
      <div class="img-wrap">
        <img src="assets/images/{img}" alt="{s['title']} — The Junk Truck Kansas City" loading="lazy">
      </div>
    </div>
  </div>
</section>
'''

    # Service schema
    schema = '<script type="application/ld+json">\n'
    schema += '{"@context":"https://schema.org","@graph":['
    service_list = []
    for s in SERVICES:
        service_list.append(f'{{"@type":"Service","name":"{s["title"]}","description":"{s["short"]}","provider":{{"@type":"LocalBusiness","name":"The Junk Truck","areaServed":"Kansas City, MO metro"}}}}')
    schema += ",".join(service_list)
    schema += ']}\n</script>'

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Services</span>
    <h1>We Haul It All.<br><span style="color: var(--orange);">Literally.</span></h1>
    <p class="lead">From single couches to whole-house clean-outs, here's the full list of what The Junk Truck hauls across the Kansas City metro.</p>
    <div class="btn-group" style="margin-top: var(--s-5);">
      <a href="book.html" class="btn btn-primary">Get a Free Quote</a>
      <a href="#junk-removal" class="btn btn-outline">Browse Services</a>
    </div>
  </div>
</section>

{service_sections}

<section class="cta-band">
  <div class="container">
    <h2>Not seeing what you need?</h2>
    <p class="lead" style="color:#fff; margin: 0 auto var(--s-5); max-width: 560px;">If it fits in the truck, we'll take it. Call us — we say yes a lot.</p>
    <a href="book.html" class="btn btn-lg">Ask About a Pickup</a>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "services.html", schema) + build_nav("services.html") + body + build_footer() + "</body></html>"


def page_locations():
    title = "Service Area — Kansas City Metro Junk Removal | The Junk Truck"
    desc = "The Junk Truck serves the entire KC metro: Kansas City MO &amp; KS, Overland Park, Olathe, Lee's Summit, Independence, Leawood, Shawnee, Liberty and more."

    location_cards = ""
    for name, state, copy, zips in LOCATIONS:
        location_cards += f'''<article class="location-card">
          <div class="state">{state}</div>
          <h3>Junk Removal in {name}</h3>
          <p>{copy}</p>
          <div class="zips">Zips: {zips}</div>
        </article>\n'''

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Service Area</span>
    <h1>Both sides of<br>the state line.</h1>
    <p class="lead">The Junk Truck serves every major suburb in the Kansas City metro. If you're somewhere on this list — or close to it — we'll be there.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="service-area-map" style="margin-bottom: var(--s-7);">
      {kc_metro_svg_map()}
      <p style="margin-top: var(--s-4); color: var(--bone); font-size: 0.9rem;">Service area: approximately 30-mile radius around Kansas City, MO</p>
    </div>

    <div style="max-width: 720px; margin-bottom: var(--s-6);">
      <span class="eyebrow">Where We Work</span>
      <h2>16 cities. One truck.<br>Zero hassle.</h2>
      <p class="lead text-muted">Each city below is a regular route. Not seeing your neighborhood? Reach out — we serve plenty of spots outside this list too.</p>
    </div>

    <div class="locations-grid">
      {location_cards}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Not sure if we serve your zip?</h2>
    <p class="lead" style="color:#fff; margin: 0 auto var(--s-5); max-width: 540px;">Ask us — most of the time, the answer's yes.</p>
    <a href="book.html" class="btn btn-lg">Check My Area</a>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "locations.html") + build_nav("locations.html") + body + build_footer() + "</body></html>"


def page_blog_index():
    title = "Blog — Kansas City Junk Removal Tips | The Junk Truck"
    desc = "Practical junk removal advice for KC homeowners. Pricing guides, estate cleanout checklists, HOA bulk day tips and more."

    cards = ""
    for post in BLOG_POSTS:
        href = f"blog/{post['slug']}.html"
        cards += f'''<a href="{href}" class="post-card">
          <div class="thumb"><img src="assets/images/{post['thumb']}" alt="" loading="lazy"></div>
          <div class="body">
            <div class="meta">{post['category']} · {post['read_min']} min read</div>
            <h3>{post['title']}</h3>
            <p>{post['summary']}</p>
            <span class="read-more">Read article →</span>
          </div>
        </a>\n'''

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">The Junk Truck Blog</span>
    <h1>KC junk advice,<br>straight up.</h1>
    <p class="lead">Cost guides, cleanout checklists, HOA tips, and other plainspoken advice from a Kansas City junk removal crew that's seen it all.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="blog-grid">
      {cards}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Skip the reading.<br>Let us haul it.</h2>
    <a href="book.html" class="btn btn-lg" style="margin-top: var(--s-4);">Get a Quote</a>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "blog.html") + build_nav("blog.html") + body + build_footer() + "</body></html>"


def page_faq():
    title = "FAQ — Kansas City Junk Removal Questions | The Junk Truck"
    desc = "Common questions about junk removal in Kansas City: pricing, service area, recycling, insurance, estate clean-outs, satisfaction guarantee and more."

    # FAQ accordion
    faq_html = ""
    for q, a in FAQS:
        faq_html += f'''<details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>\n'''

    # JSON-LD FAQPage schema
    faq_schema_items = []
    for q, a in FAQS:
        # escape quotes
        q_esc = q.replace('"', '\\"')
        a_esc = a.replace('"', '\\"').replace('\n', ' ')
        faq_schema_items.append(f'{{"@type":"Question","name":"{q_esc}","acceptedAnswer":{{"@type":"Answer","text":"{a_esc}"}}}}')
    schema = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(faq_schema_items) + ']}</script>'

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Frequently Asked</span>
    <h1>No mystery pricing.<br>No sales nonsense.</h1>
    <p class="lead">Ten honest answers to the questions KC homeowners ask us every week.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width: 860px;">
      <div class="accordion">
        {faq_html}
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Question not answered?</h2>
    <p class="lead" style="color:#fff; margin: 0 auto var(--s-5); max-width: 540px;">Book a quote and ask us anything. We're happy to talk through it.</p>
    <a href="book.html" class="btn btn-lg">Book a Pickup</a>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "faq.html", schema) + build_nav("faq.html") + body + build_footer() + "</body></html>"


def page_book():
    title = "Book a Pickup — Free Quote | The Junk Truck Kansas City"
    desc = "Schedule your junk removal pickup in the Kansas City metro. Free, no-obligation quotes. Same-day service often available."

    service_options = ""
    for s in SERVICES:
        service_options += f'<option value="{s["slug"]}">{s["title"]}</option>\n'

    body = f'''
<main id="main">

<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Book a Pickup</span>
    <h1>Clear it out.<br><span style="color: var(--orange);">Same day, often.</span></h1>
    <p class="lead">Tell us what you've got — we'll come out, take a look, and give you a firm price before we haul a thing. No surprises.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split" style="align-items: flex-start;">
      <div>
        <span class="eyebrow">How it works</span>
        <h2 style="font-size: clamp(1.8rem, 3vw, 2.5rem);">Three simple steps.</h2>
        <ol style="list-style: none; padding: 0; margin-top: var(--s-5);">
          <li style="display: flex; gap: var(--s-4); margin-bottom: var(--s-5);">
            <span style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 50%; background: var(--orange); color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--display); font-size: 1.2rem;">1</span>
            <div>
              <h4 style="margin-bottom: 4px;">Request a quote</h4>
              <p style="margin: 0; color: var(--muted);">Fill out the form or give us a call. Photos help — but aren't required.</p>
            </div>
          </li>
          <li style="display: flex; gap: var(--s-4); margin-bottom: var(--s-5);">
            <span style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 50%; background: var(--orange); color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--display); font-size: 1.2rem;">2</span>
            <div>
              <h4 style="margin-bottom: 4px;">We confirm a window</h4>
              <p style="margin: 0; color: var(--muted);">We'll book a 2-hour arrival window — often same-day or next-day.</p>
            </div>
          </li>
          <li style="display: flex; gap: var(--s-4);">
            <span style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 50%; background: var(--orange); color: #fff; display: flex; align-items: center; justify-content: center; font-family: var(--display); font-size: 1.2rem;">3</span>
            <div>
              <h4 style="margin-bottom: 4px;">We haul it all</h4>
              <p style="margin: 0; color: var(--muted);">On-site quote, you say go, we load up and leave the space broom-clean.</p>
            </div>
          </li>
        </ol>
        <div style="margin-top: var(--s-6); padding: var(--s-5); background: var(--bone); border-radius: var(--radius-lg);">
          <h4 style="margin-bottom: var(--s-2);">Need it urgent?</h4>
          <p style="margin: 0; color: var(--muted);">For same-day jobs or anything time-sensitive, just give us a shout directly. Phone number coming soon — in the meantime, mark "Urgent" on the form below.</p>
        </div>
      </div>

      <form class="booking-form" onsubmit="event.preventDefault(); this.querySelector('.form-confirm').style.display='block'; this.querySelector('.form-fields').style.display='none';" aria-label="Junk removal booking form">
        <h3 style="text-transform: none; font-family: var(--sans); letter-spacing: 0; font-size: 1.5rem; margin-bottom: var(--s-5);">Request a free quote</h3>
        <div class="form-fields">
          <div class="form-row two">
            <div class="field">
              <label for="f-name">Name <span class="req">*</span></label>
              <input id="f-name" name="name" type="text" required autocomplete="name">
            </div>
            <div class="field">
              <label for="f-phone">Phone <span class="req">*</span></label>
              <input id="f-phone" name="phone" type="tel" required autocomplete="tel">
            </div>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="f-email">Email</label>
              <input id="f-email" name="email" type="email" autocomplete="email">
            </div>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="f-address">Pickup Address <span class="req">*</span></label>
              <input id="f-address" name="address" type="text" required placeholder="Street, City, ZIP" autocomplete="street-address">
            </div>
          </div>
          <div class="form-row two">
            <div class="field">
              <label for="f-service">Service <span class="req">*</span></label>
              <select id="f-service" name="service" required>
                <option value="">Select a service…</option>
                {service_options}
                <option value="other">Not sure / Other</option>
              </select>
            </div>
            <div class="field">
              <label for="f-date">Preferred Date</label>
              <input id="f-date" name="date" type="date">
            </div>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="f-desc">What do you need hauled? <span class="req">*</span></label>
              <textarea id="f-desc" name="description" required placeholder="e.g. 1 couch, old fridge, garage full of boxes, yard waste from a tree trim…"></textarea>
            </div>
          </div>
          <div class="form-row">
            <div class="field upload">
              {icon("upload")}
              <div style="font-weight: 700; color: var(--ink); margin-bottom: 4px;">Add photos (optional)</div>
              <div style="font-size: 0.85rem;">Photos help us give a better quote. Drag and drop, or click to upload.</div>
              <input type="file" name="photos" accept="image/*" multiple style="margin-top: var(--s-3);">
            </div>
          </div>
          <div class="form-row">
            <label style="display:flex; gap: var(--s-3); align-items: flex-start; font-size: 0.9rem; color: var(--muted); cursor: pointer;">
              <input type="checkbox" name="urgent" style="margin-top: 4px;">
              <span>This is urgent — I need pickup within 24 hours.</span>
            </label>
          </div>
          <button type="submit" class="btn btn-primary btn-lg" style="width: 100%; justify-content: center;">Request Free Quote</button>
          <p class="hint" style="margin-top: var(--s-3); text-align: center;">By submitting, you agree to be contacted about your pickup. We'll never share your info.</p>
        </div>
        <div class="form-confirm" style="display:none; text-align:center; padding: var(--s-5) 0;">
          <div style="width: 64px; height: 64px; background: var(--orange); border-radius: 50%; margin: 0 auto var(--s-4); display: flex; align-items: center; justify-content: center; color: #fff;">{icon("check")}</div>
          <h3 style="font-family: var(--sans); text-transform: none; letter-spacing: 0; font-size: 1.5rem;">Request received.</h3>
          <p style="color: var(--muted);">Thanks! We'll get back to you within a few hours. Check your phone and email for our reply.</p>
        </div>
      </form>
    </div>
  </div>
</section>

</main>
'''
    return build_head(title, desc, "book.html") + build_nav("book.html") + body + build_footer() + "</body></html>"


# -------- Blog articles --------

def blog_post_page(post):
    """Full article or stub."""
    title = f"{post['title']} | The Junk Truck Blog"
    desc = post['summary']

    schema = '<script type="application/ld+json">' + \
        '{"@context":"https://schema.org","@type":"BlogPosting",' + \
        f'"headline":"{post["title"].replace(chr(34), chr(39))}",' + \
        f'"datePublished":"{post["date"]}",' + \
        f'"image":"{SITE["url"]}/assets/images/{post["thumb"]}",' + \
        '"author":{"@type":"Organization","name":"The Junk Truck"},' + \
        '"publisher":{"@type":"Organization","name":"The Junk Truck"}}' + \
        '</script>'

    content = BLOG_CONTENT.get(post["slug"], "<p>This article is coming soon. We're working on it — in the meantime, <a href=\"../book.html\">get a free quote</a> or browse <a href=\"../services.html\">our services</a>.</p>")

    body = f'''
<main id="main">
<article class="article">
  <div class="container">
    <div class="meta">{post['category']} · {post['read_min']} min read · {post['date']}</div>
    <h1>{post['title']}</h1>
    <p class="lead" style="color: var(--muted); font-size: 1.15rem;">{post['summary']}</p>
    <div class="hero-img"><img src="../assets/images/{post['thumb']}" alt="{post['title']}" loading="eager"></div>
    {content}
    <hr style="margin: var(--s-7) 0; border: 0; border-top: 1px solid rgba(20,24,32,0.12);">
    <div style="background: var(--bone); padding: var(--s-6); border-radius: var(--radius-lg); text-align: center;">
      <h3 style="font-family: var(--sans); letter-spacing: 0; text-transform: none; font-size: 1.4rem;">Ready to clear it out?</h3>
      <p style="color: var(--muted); margin-bottom: var(--s-4);">Free quote. No pressure. Kansas City metro-wide.</p>
      <a href="../book.html" class="btn btn-primary">Book a Pickup</a>
    </div>
    <p style="margin-top: var(--s-6); text-align: center;"><a href="../blog.html">← Back to all articles</a></p>
  </div>
</article>
</main>
'''

    # For blog posts, the head uses relative paths one level deeper
    head = build_head(title, desc, f"blog/{post['slug']}.html", schema)
    head = head.replace('href="css/', 'href="../css/')
    head = head.replace('content="https://kinggavint.github.io/junk-truck-proof/assets', 'content="https://kinggavint.github.io/junk-truck-proof/assets')

    nav = build_nav("blog.html")
    # Fix nav paths (blog posts are one level deep)
    nav_fixed = nav
    for _, href in NAV_ITEMS:
        nav_fixed = nav_fixed.replace(f'href="{href}"', f'href="../{href}"')
    nav_fixed = nav_fixed.replace('href="book.html"', 'href="../book.html"')
    nav_fixed = nav_fixed.replace('href="index.html" class="brand"', 'href="../index.html" class="brand"')
    nav_fixed = nav_fixed.replace('href="#main"', 'href="#main"')

    footer = build_footer()
    # Fix footer paths
    footer_fixed = footer
    footer_fixed = footer_fixed.replace('href="services.html', 'href="../services.html')
    footer_fixed = footer_fixed.replace('href="locations.html"', 'href="../locations.html"')
    footer_fixed = footer_fixed.replace('href="book.html"', 'href="../book.html"')
    footer_fixed = footer_fixed.replace('href="faq.html"', 'href="../faq.html"')
    footer_fixed = footer_fixed.replace('href="about.html"', 'href="../about.html"')
    footer_fixed = footer_fixed.replace('href="blog.html"', 'href="../blog.html"')
    footer_fixed = footer_fixed.replace('src="js/main.js"', 'src="../js/main.js"')

    return head + nav_fixed + body + footer_fixed + "</body></html>"


BLOG_CONTENT = {
    "junk-removal-cost-kansas-city": '''
<h2>What junk removal actually costs in Kansas City (2026)</h2>
<p>If you've ever tried to price out junk removal in Kansas City, you've probably had the same experience: you pick up the phone, ask a simple question, and the answer is "it depends." That's technically true — but it's also a useless answer if you're trying to budget for a cleanout this weekend.</p>
<p>So here's a plainspoken breakdown of what KC homeowners actually pay in 2026, based on how most local and national haulers price. Your quote will vary, but this should give you a realistic ballpark before you pick up the phone.</p>

<h2>Junk removal is priced by volume, not by weight</h2>
<p>This is the single most important thing to understand: almost every junk removal company in Kansas City — including The Junk Truck — prices based on <strong>how much space your stuff takes up in the truck</strong>. Not pounds. Not hours. Not items.</p>
<p>A typical junk removal truck is somewhere in the range of 12 to 15 cubic yards. We talk about load sizes in fractions of that:</p>

<h3>Typical 2026 KC junk removal pricing</h3>
<ul>
  <li><strong>Minimum load (1/8 truck):</strong> $125 – $175. Single items like one couch, one mattress, or a small pile of boxes.</li>
  <li><strong>Quarter truck:</strong> $200 – $300. A small room's worth — a bedroom set, a half-garage of boxes.</li>
  <li><strong>Half truck:</strong> $325 – $475. A full garage cleanout or a couple of rooms.</li>
  <li><strong>Three-quarter truck:</strong> $475 – $600. Large garage plus a basement pile, or a studio apartment's worth.</li>
  <li><strong>Full truck:</strong> $575 – $750+. A whole-house cleanout or a construction-scale debris load.</li>
</ul>
<p>Certain heavy materials — concrete, dirt, roofing, brick — can bump pricing up because they eat into the weight-per-cubic-yard our truck can legally haul. Most residential cleanouts stay in the "regular stuff" category.</p>

<h2>What's included in the price</h2>
<p>Reputable KC haulers (local or national) bake these into the quoted price:</p>
<ul>
  <li>All labor — loading, lifting, carrying down stairs</li>
  <li>Transportation</li>
  <li>Disposal and recycling fees</li>
  <li>Cleanup of the pickup area</li>
  <li>Taxes (usually)</li>
</ul>
<p>If you get a quote that looks shockingly low, ask whether disposal fees are included. Some out-of-state operators quote "labor only" and then hit you with dump charges after the fact.</p>

<h2>Single-item pricing (the small-job discount)</h2>
<p>If you just need one thing gone — a single mattress, one couch, a dead treadmill — most KC haulers offer a single-item rate that's cheaper than the minimum load. In 2026, expect:</p>
<ul>
  <li>Mattress: $95 – $150</li>
  <li>Couch or recliner: $110 – $180</li>
  <li>Refrigerator/freezer (freon handled): $115 – $165</li>
  <li>Treadmill or exercise equipment: $100 – $180</li>
  <li>TV (over 32"): $45 – $85</li>
</ul>

<h2>What makes your price go up or down</h2>
<p>Three things move a junk removal quote in Kansas City:</p>
<h3>1. Location inside the home</h3>
<p>Curbside pickup is cheapest. Basement or third-floor pickup costs more — not because the crew is greedy, but because it legitimately takes longer and is harder on their backs. Expect a 10-20% bump for difficult access.</p>
<h3>2. Special handling items</h3>
<p>Refrigerators and freezers need freon reclamation. Electronics need separate disposal. Mattresses have their own recycling stream in KC. These are usually bundled into the volume price but can bump a borderline quote.</p>
<h3>3. Accessibility</h3>
<p>Can we park within 20 feet of the stuff? Is there a clear path? Are there stairs or narrow doorways? The easier our lives, the lower your quote.</p>

<h2>How to get an honest Kansas City junk removal quote</h2>
<p>Three steps that save you money every time:</p>
<ul>
  <li><strong>Take a photo.</strong> A single wide shot of the pile or the room helps a hauler give you a tight estimate over the phone.</li>
  <li><strong>Be specific.</strong> "A couch and a few boxes" is different from "a couch, two chairs, twelve boxes, and a broken treadmill." Accuracy protects you.</li>
  <li><strong>Ask for an in-person quote before work starts.</strong> The best KC haulers won't start loading until you've okayed the final price. That's the industry standard — hold them to it.</li>
</ul>

<h2>Why local beats national</h2>
<p>National franchises have to cover a franchise fee, regional ad buys, and a corporate phone center. That overhead ends up in your quote. A locally-owned, self-funded hauler in Kansas City — like The Junk Truck — doesn't carry that weight. Same service, same trucks, same care, often 10-20% lower price.</p>
<p>Get a free no-obligation quote from us and compare. We won't hassle you, and we'll always give you the firm price before we load a thing.</p>
''',

    "estate-cleanout-checklist": '''
<h2>Estate cleanouts are hard. We'll make this easier.</h2>
<p>Estate cleanouts in Kansas City don't happen in normal times. They happen after a loss, a move to assisted living, a downsize, or the end of a long chapter. If you're here, odds are good you're already overwhelmed — so this article is designed to be short, useful, and honest.</p>
<p>Five things worth knowing before you start an estate cleanout.</p>

<h2>1. Sort before you haul — but don't over-sort</h2>
<p>The single biggest trap in an estate cleanout is trying to sort every item into "keep, donate, sell, toss." You will lose weeks doing this. For most estates, a simpler approach works:</p>
<ul>
  <li><strong>Sentimental / heirloom pile</strong> — photos, letters, specific items family members asked for. Small. Protected. Moved first.</li>
  <li><strong>Valuable pile</strong> — anything an estate sale company might want. A single afternoon is enough to decide this.</li>
  <li><strong>Everything else</strong> — goes to a hauler who sorts donation-worthy items from disposal-bound ones.</li>
</ul>
<p>That last point matters. A good KC junk removal crew will pull donation-quality furniture, appliances, and household goods out of your estate pile and make sure they get to a local donation partner — no extra work on your end.</p>

<h2>2. Talk to the realtor before you clean</h2>
<p>If the home is going on the market, the realtor might want you to leave certain items — staging furniture, appliances, even landscaping — in place. Calling them <em>before</em> a cleanout saves you from hauling out a fridge only to hear "wait, we wanted that to stay."</p>

<h2>3. Documents are the hidden landmine</h2>
<p>Tax returns, medical records, warranty paperwork, safe deposit box keys, titles, wills, insurance documents — these hide everywhere in estates. Common spots to check before anyone hauls anything:</p>
<ul>
  <li>Desk drawers and filing cabinets (obvious)</li>
  <li>Kitchen drawers near the phone</li>
  <li>Coat pockets in hall closets</li>
  <li>Shoe boxes on top shelves</li>
  <li>Books (seriously — people hide cash in books)</li>
  <li>Inside the freezer (really)</li>
</ul>
<p>Do a paper-hunt pass before you call a junk removal crew. A good hauler will flag anything that looks important, but you know your loved one's habits better than we do.</p>

<h2>4. Estate sales are optional — and often not worth it</h2>
<p>A lot of families default to "we should have an estate sale first." Sometimes that's right. Often it's not. Estate sales work well when:</p>
<ul>
  <li>There's real furniture, collectibles, or antiques with proven value</li>
  <li>The home is available for 2-3 weekends of access</li>
  <li>You're okay with strangers walking through</li>
</ul>
<p>For most estates, a direct cleanout — with donation-quality items routed to local charities — nets roughly the same financial outcome with a fraction of the emotional cost. The Junk Truck handles post-estate-sale cleanouts AND direct cleanouts. Both are fine choices.</p>

<h2>5. You don't have to be there</h2>
<p>This is the single thing families don't know: you don't have to be present for an estate cleanout. If you've already walked through, marked what stays, and flagged what matters — a professional crew can handle the rest and send you photos when it's done. That's especially useful for out-of-town family members managing a Kansas City estate from another state.</p>

<h2>Working with a KC estate cleanout service</h2>
<p>A good Kansas City estate cleanout service should:</p>
<ul>
  <li>Give you a firm on-site quote before any work starts</li>
  <li>Offer compassionate, no-pressure service (this isn't a sales job)</li>
  <li>Sort donation-quality items into a separate pile and get them to local partners</li>
  <li>Coordinate with realtors and estate attorneys when needed</li>
  <li>Leave the home broom-clean</li>
</ul>
<p>The Junk Truck does estate cleanouts across the KC metro, from the Plaza to Olathe. We treat every estate with the respect it deserves. Reach out when you're ready — no rush.</p>
''',
}


# -------- Run the build --------

def main():
    os.makedirs(os.path.join(OUT, "blog"), exist_ok=True)

    pages = {
        "index.html": page_home(),
        "about.html": page_about(),
        "services.html": page_services(),
        "locations.html": page_locations(),
        "blog.html": page_blog_index(),
        "faq.html": page_faq(),
        "book.html": page_book(),
    }
    for fname, html in pages.items():
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote {fname} ({len(html)} bytes)")

    # Blog posts
    for post in BLOG_POSTS:
        html = blog_post_page(post)
        path = os.path.join(OUT, "blog", f"{post['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Wrote blog/{post['slug']}.html ({len(html)} bytes)")

    # sitemap.xml
    urls = ["", "about.html", "services.html", "locations.html", "blog.html", "faq.html", "book.html"]
    urls += [f"blog/{p['slug']}.html" for p in BLOG_POSTS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        full = f"{SITE['url']}/{u}" if u else SITE['url'] + "/"
        sm += f'  <url><loc>{full}</loc><changefreq>monthly</changefreq><priority>{"1.0" if u == "" else "0.8"}</priority></url>\n'
    sm += '</urlset>\n'
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(sm)
    print("Wrote sitemap.xml")

    # robots.txt
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE['url']}/sitemap.xml\n")
    print("Wrote robots.txt")

    print("\nDone.")


if __name__ == "__main__":
    main()

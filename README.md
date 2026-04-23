# The Junk Truck — Kansas City Junk Removal

Locally-owned, self-funded junk removal company serving the Kansas City metro.

**Live site:** https://kinggavint.github.io/junk-truck-proof/

## What's here

Seven-page static marketing site, no build step required. Plain HTML + CSS + a tiny sprinkle of vanilla JS for mobile nav and scroll animations.

- `index.html` — Home
- `about.html` — About / founder story
- `services.html` — Services (9 offerings with deep sections)
- `locations.html` — KC metro service area (16 cities)
- `blog.html` — Blog index
- `faq.html` — FAQ (accordion, with JSON-LD)
- `book.html` — Booking / quote request form
- `blog/` — 2 full articles + 4 stub articles
- `css/styles.css` — Design system and all styling
- `js/main.js` — Mobile nav + smooth scroll + fade-up observer
- `assets/images/` — AI-generated webp imagery
- `sitemap.xml`, `robots.txt` — SEO
- `build.py` — Python script that regenerates all HTML from the content tables at the top of the file

## Development

Generate pages from scratch:

```bash
python3 build.py
```

Serve locally:

```bash
python3 -m http.server 5050
```

## Hosting

Deployed via GitHub Pages from the `main` branch root.

# Notes for Collin — Before We Go Live

Hey Collin — here's what you need to know before launch. A few things are placeholder and need your input.

## Needs your input

### 1. Logo
- Right now the site uses a **temporary SVG wordmark** ("THE JUNK TRUCK" + a small truck mark icon) in charcoal and orange.
- Whenever you upload your real logo (you mentioned a "funky/fun" one), we'll swap the wordmark out. If your logo colors push a different direction, we can retune the palette to match.

### 2. Phone number
- Your existing junktruck123.com site doesn't list a phone number, so we've used **"Book a Pickup"** as the primary CTA everywhere instead of "Call Now."
- As soon as you send us a phone number, we'll:
  - Add a "Call Now" button to the hero and nav
  - Swap "Call for a quote" placeholder text for your real number
  - Wire up tel: links site-wide so mobile taps dial you

### 3. Business hours
- Same story — not listed on the existing site, so not on this one yet.
- Once you send hours, we'll add them to the footer and the Book a Pickup page.

### 4. Email address
- We used `hello@junktruck123.com` as a placeholder. If you want a different inbox (contact@, collin@, quotes@), let us know.

### 5. Color palette — recommendation, not final
- I went with **deep charcoal + safety orange + cream**. See research.md for why.
- This is a recommendation based on your "funky-fun-but-professional" brief and your "to the moon, baby" energy. If your real logo pushes a different direction (e.g. navy, green, red), we'll retune every page in about an hour.
- Easy to change — it's all driven by CSS variables in `css/styles.css`.

### 6. Booking form wiring
- The "Book a Pickup" page has a **styled contact form**. Right now, submitting it only shows a confirmation message — it does NOT send you an email or create a calendar event.
- Two paths forward at launch:
  - **(a) Simple:** Wire the form to Formspree or Getform (~15 min) to email submissions to you.
  - **(b) Full booking:** Embed Calendly or Acuity to let customers self-schedule pickup windows (~30 min).
- You mentioned "Appointment Calendar" in the brief, so option (b) is probably what you want. We just need:
  - Your preferred booking platform (Calendly, Acuity, Square Appointments, etc.)
  - Your account's embed code or link

### 7. Testimonials / reviews
- Intentionally **not included yet**. Fake testimonials with fake names are a bad look and Google will sniff them out. When you want to add them:
  - Send 3–5 real reviews (with names / city / permission to use)
  - Or let us pull your existing Google Business Profile reviews

### 8. Real fleet photos
- Every image on the site is AI-generated right now — all generic, clean, residential-driveway vibe. No faces, no fake branded shirts.
- When you send real photos of your actual truck, crew, and before/after jobs, we'll swap them in and the site gets a credibility boost. Specifically helpful:
  - A clean hero shot of your truck in a KC driveway
  - 2–3 before/after cleanout shots (garage, yard, house)
  - A team-loading-the-truck shot (backs or side, don't need faces)

### 9. Service area map
- The KC metro map on the homepage and Locations page is a **stylized abstract illustration**, not a literal Google Map. That's intentional — service areas look cheesy when pinned on a real map at this level.
- If you want a real Google Map embed later (e.g. to highlight your dispatch zip), we can add one.

### 10. Blog content
- **Two full blog posts** are written and ready to publish: "How Much Does Junk Removal Cost in Kansas City?" and "5 Things to Know Before an Estate Cleanout". Both are ~1,000 words, SEO-friendly, and in your voice.
- **Four more blog posts** are set up as stubs with real slugs and titles — they show up in the blog index but clicking through goes to a short placeholder. When you want to expand these, we'll write 'em:
  - Garage cleanout checklist
  - What junk removal companies won't take
  - Moving out — junk removal guide
  - HOA bulk pickup guide

## What's solid and ready

- All 7 pages built and responsive (Home, About, Services, Locations, Blog, Book a Pickup, FAQ)
- Site copy is in your energetic, "locally-owned, not-a-franchise" voice throughout
- JSON-LD structured data for LocalBusiness + FAQ + Services + BlogPostings (Google SEO-ready)
- Sitemap.xml and robots.txt in place
- Mobile-first responsive tested at 375px, 768px, 1280px
- Semantic HTML, alt text on images, ARIA labels on interactive elements
- All AI images < 325KB webp (fast page loads)
- Skip-to-content link for keyboard accessibility

## Zero branding/attribution

Per the brief: no "Created with X", no "Lovable", no "Built by Computer" anywhere. Footer is just **"© 2026 The Junk Truck"**. Clean.

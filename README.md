# BL4CK4T — Zaggonaut‑inspired Astro Blog

A Zaggonaut‑inspired theme packaged as an Astro starter with:
- dynamic homepage cards, archive, tags
- SEO (canonical/OG/Twitter + JSON‑LD on posts)
- RSS, robots, and dev‑friendly sitemap endpoints
- GitHub Pages workflow

## Quick start
```bash
npm i
npm run dev
```

## Production URL
Set a repo variable (or env) for `SITE_URL` to your domain or Pages URL.
The sitemap plugin will use it to generate `/sitemap-index.xml`.

## Posts
Add Markdown files to `src/content/blog/` using this frontmatter:
```md
---
title: "Title"
description: "≤160 chars summary"
publishDate: 2025-09-15
tags: ["tag1","tag2"]
---
Content here.
```

## Deploy (GitHub Pages)
- Push to `main`
- Settings → Pages → **GitHub Actions** (source)
- Add repo variable `SITE_URL` = `https://<user>.github.io/<repo>` (or your domain)

## License
All code in this starter is newly authored for you and not copied from any external repository.
You may adapt freely.

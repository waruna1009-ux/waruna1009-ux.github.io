# Yantai Dingdingmiao Seafood Website

Professional corporate website for a Chinese frozen seafood exporter.

## Structure
- `index.html` — Home page with product highlights and trust signals
- `products.html` — Full frozen seafood catalog (8 products with specs)
- `about.html` — Company information, certifications, markets served
- `contact.html` — Inquiry form + direct contact info

## SEO & AI Indexing
- Schema.org JSON-LD on every page (Organization, Product, ContactPoint, ItemList)
- Semantic HTML5 (nav, main, article, header, footer)
- Responsive mobile-first design
- robots.txt + sitemap.xml
- Open Graph meta tags for social sharing
- Zero JS dependency for core content (curl-friendly)
- Clear product descriptions with HS codes

## Deployment (GitHub Pages)
1. Push to a GitHub repository
2. Enable GitHub Pages in Settings → Pages
3. (Optional) Add custom domain

## Preview Locally
```bash
cd ~/.hermes/agent-workspace/seafood-site
python3 -m http.server 8080
# Open http://localhost:8080
```

# Dingdingmiao Seafood — trading and sourcing website

Yantai Dingdingmiao is a trading and sourcing company for global seafood buyers. The catalog is a set of examples; unlisted products can be submitted for supplier search and quotation coordination. Availability, certifications, origin, service scope and any commission are agreed per engagement.

- Canonical public website: https://dingdingmiao-seafood.genialpike6.chatgpt.site/
- Existing synchronized public mirror: https://waruna1009-ux.github.io/
- Canonical source: `waruna1009-ux/waruna1009-ux.github.io`, branch `main`.
- Codex Sites project: see `.openai/hosting.json`. Reuse that project; never create a replacement to update this site.
- The owner explicitly authorized public Sites access on 2026-10-23. Preserve that public audience. Both copies use Sites as the preferred canonical origin, with its extensionless page URLs. GitHub remains the source repository and an existing synchronized mirror; long-term commercial hosting should use Sites rather than rely on GitHub Pages.

## Build and verify

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node scripts/check_inquiry.mjs
```

The build copies an explicit public-file allowlist into ignored `dist/`. It generates `sitemap.xml`, a supplementary `llms.txt` directory and a tracked `site-release.json` with hashes of the public files. The manifest has no self-referential commit field. GitHub Pages serves the same source files from `main`; Sites deploys those exact bytes from `dist/`. Internal documentation, tooling, inbox data and operating reports are excluded from the Sites payload. Publication identity is defined in `scripts/site_config.py`.

## Release both channels

1. Fetch canonical GitHub `main` and reconcile upstream changes without force pushing or overwriting another editor's work.
2. Obtain fresh source access for the existing Sites project. Use the installed Sites skill and its official source helper to open this checkout. Never write access credentials to disk or logs.
3. Edit the shared source. Run the checks above and preview desktop/mobile layout, navigation, filters and inquiry fields. Simulated form acceptance is not an email-delivery test.
4. Use the official Sites source helper to run remaining checks, commit and push the source, and package `dist/`. Keep the archive outside this checkout.
5. Push the exact same commit to GitHub `main` with a normal, non-force push. Verify both source branches identify that commit. If either push fails, reconcile and report the divergence.
6. Deploy the helper's archive and exact commit via Sites, preserving the current audience. Reuse a returned saved-version ID after a deployment failure.
7. Wait for GitHub Pages and Sites deployments to finish. Compare the live release manifest and public-file bytes; a repository push alone is not a successful website deployment.

## Operating rules

- Global buyers and all seafood categories; distinguish trade/sourcing services from manufacturing or inventory ownership.
- Publish only supported facts. Do not invent stock, price, certification, capacity, delivery commitments, reviews, clients or search-volume claims.
- Prioritize intent and measured results: sourcing-agent queries, product/species/form queries, specification and packing questions, then destination questions supported by current primary sources.
- Existing Clarity project: `xqu1ib3adr`. Both public hostnames are permitted; local previews and URLs with `?sitecheck` are excluded. A `site_host` tag distinguishes the host. Contact events: `whatsapp_click`, `email_click`, `inquiry_form_accepted`, `inquiry_form_error`. These are intent/service signals, not delivered messages or qualified leads. Form fields are masked and no typed values are sent as custom events. Actual statistics access remains pending.
- Weekly report: visitors, sessions, page views, sources/countries/landing pages, Search Console impressions/clicks/CTR/position, contact events, actual new inquiries and qualified leads, changes made, next actions. Preserve unavailable values as unavailable, never zero.
- Inquiry monitoring uses connected business mailbox `waruna825@outlook.com`. Check daily at 08:30 Asia/Shanghai and deduplicate by message ID. Combine inquiries and the operating report into one email to that same owner address each Monday at 09:00. Do not send routine Codex alerts or WhatsApp notifications. Do not reply to customers, confirm prices or accept orders automatically.
- WhatsApp click tracking cannot read incoming WhatsApp messages. Require a separately verified message connection before claiming monitoring.
- FormSubmit acceptance requires service activation; mailbox arrival and reply handling must be verified separately. Never submit test inquiries to external recipients without authorization.
- Do not add paid tools, ads, domains, purchases, mass outreach or new public audiences without explicit authorization.
- Never modify the owner's VPN, VPN server, whalech.com DNS, nameservers, proxy, certificates, ports or firewall. The Sites public-access authorization does not authorize any of those changes.

## Search and AI answer discovery

- Critical company facts, buyer questions and answers, product examples and contact methods must be readable in the initial HTML. Use the same content for humans and crawlers.
- Keep the company identity, canonical URL, Open Graph URL, sitemap and visible facts consistent. The company is a trader/sourcing provider, not a claimed manufacturer or guaranteed stockholder.
- Allow search crawlers through robots.txt and validate anonymous HTTPS responses without authentication. A simulated crawler user agent is an access test, not proof that a real crawler indexed the page.
- Separate search discovery from training permissions. Preserve existing permissions unless the owner changes them; never describe GPTBot training access as a search-ranking requirement.
- Structured FAQ answers must match visible answers. Do not add fabricated reviews, offers, inventory, awards or certifications. An llms.txt file is a supplementary directory, not an indexing or ranking guarantee.
- Treat absence of Search Console/Clarity access as unavailable data, not zero. Search observations, crawler eligibility, actual indexing, AI citations and customer inquiries are different evidence classes.
- Relevant guidance: https://developers.google.com/search/docs/appearance/ai-features ; https://developers.openai.com/api/docs/bots ; https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls .

Business contact: `waruna825@outlook.com` · WhatsApp `+86 13954508112`.

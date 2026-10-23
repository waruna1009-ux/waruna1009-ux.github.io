# Dingdingmiao Seafood — trading and sourcing website

Yantai Dingdingmiao is a trading and sourcing company for global seafood buyers. The catalog is a set of examples; unlisted products can be submitted for supplier search and quotation coordination. Availability, certifications, origin, service scope and any commission are agreed per engagement.

- Canonical public website: https://waruna1009-ux.github.io/
- Canonical source: `waruna1009-ux/waruna1009-ux.github.io`, branch `main`.
- Codex Sites project: see `.openai/hosting.json`. Reuse that project; never create a replacement to update this site.
- Sites is an owner-private management copy unless the owner explicitly changes its audience. All canonical links point to the public GitHub website.

## Build and verify

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node scripts/check_inquiry.mjs
```

The build copies an explicit public-file allowlist into ignored `dist/`. It generates `sitemap.xml` and a tracked `site-release.json` with hashes of the public files. The manifest has no self-referential commit field. GitHub Pages serves the same source files from `main`; Sites deploys those exact bytes from `dist/`. Internal documentation, tooling and archived CSS are excluded from the Sites payload.

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
- Existing Clarity project: `xqu1ib3adr`. Contact events: `whatsapp_click`, `email_click`, `inquiry_form_accepted`, `inquiry_form_error`. These are intent/service signals, not delivered messages or qualified leads. Form fields are masked and no typed values are sent as custom events.
- Weekly report: visitors, sessions, page views, sources/countries/landing pages, Search Console impressions/clicks/CTR/position, contact events, actual new inquiries and qualified leads, changes made, next actions. Preserve unavailable values as unavailable, never zero.
- Inquiry monitoring uses connected business mailbox `waruna825@outlook.com`. Deduplicate by message ID. Notify the owner in Codex; do not reply to customers, confirm prices or accept orders automatically.
- WhatsApp click tracking cannot read incoming WhatsApp messages. Require a separately verified message connection before claiming monitoring.
- FormSubmit acceptance requires service activation; mailbox arrival and reply handling must be verified separately. Never submit test inquiries to external recipients without authorization.
- Do not add paid tools, ads, domains, purchases, mass outreach or new public audiences without explicit authorization.

Business contact: `waruna825@outlook.com` · WhatsApp `+86 13954508112`.

# Blog operating policy

The owner delegated topics, direction, cadence, publication and continuing blog operation on 2026-10-23. The objective is relevant global buyer discovery and inquiries. Preserve the existing public Sites project, GitHub mirror, business identity and VPN boundary in README.

## Cadence and prioritization

- Use the existing Monday 09:00 Asia/Shanghai operating heartbeat. Target one useful new English buyer guide and one substantive existing-guide improvement each week. Include both in the same release and owner email; do not create extra report or notification schedules.
- The initial 2026-10-23 cleanup added two evergreen quotation guides and revised all eleven existing articles. There are thirteen articles, each with its own buyer question, original publication date and honest modification date.
- Prioritize actual inquiry questions and available Search Console queries, then unmet buying questions supported by current public search observations. Query appearances are qualitative intent evidence, not monthly search volumes.
- Cover all seafood categories and unlisted sourcing requests. Rotate specification/packing, quotation comparison, supplier and route review, and destination topics backed by current official sources. Do not repeatedly create near-duplicates for each country or keyword spelling.
- Review results every four weekly cycles. Consider organic impressions/clicks, relevant non-branded queries, landing-page visits, contact intent and qualified inquiries. Use unavailable for missing data, never zero. Do not claim traffic growth from a publication count.
- If a proposed article lacks a useful distinct question or verifiable facts, improve an existing page and record why the new item was deferred. Do not publish filler to meet a quota.

## Evidence and writing

- Start with a direct answer, then provide a useful checklist, worked example, comparison or decision sequence. Keep headings phrased for buyers and content visible in initial HTML.
- Company claims must match the owner-authorized trader/sourcing role. No owned-factory, stock, certification, fixed MOQ, fixed price, guaranteed sailing time, raw-consumption suitability or customs promise without evidence applicable to that statement.
- Scientific, regulatory, market-size and technical claims require current authoritative sources. Clearly scope country-specific information. Do not present a stale industry overview as current law. Cite sources beside the supported statements; preserve a research date in the operating record.
- Explain units and denominators. Distinguish count per pound from count per kilogram, glaze from internal moisture and thaw loss, and declared product weight from price basis and gross shipping weight.
- Label hypothetical numbers as illustrations, verify the arithmetic, and do not treat them as offers or live market prices. Do not derive popularity, availability or quality from model assumptions.
- Do not copy competing articles. Search results may identify unanswered buying questions; they are not proof of this company's capabilities or facts.
- Preserve old URLs and original publication dates for revisions. Update dateModified only for substantive changes and display both dates. Do not refresh dates alone or claim a new article was published in the past.

## Authoring and release

- Current articles are authored as static blog/*.html. Use an existing revised article as the layout reference. The one-off cleanup script outside the repository is not a build dependency and must not be rerun to overwrite later edits.
- Keep Organization, WebSite, WebPage, BlogPosting, BreadcrumbList and any visible FAQ data consistent. BlogPosting author and publisher reference the existing company identity. Do not invent an expert author.
- Link each article from blog/index.html and relevant related guides/product pages. Update the homepage highlights for new useful articles and the Blog index metadata. Avoid links that leave new pages orphaned.
- Every guide should offer a relevant inquiry form link and the real email and WhatsApp contacts. These are calls to action, not proof of messages received. Never insert customer mail content or personal data into published examples.
- Run python3 scripts/build_site.py, python3 scripts/check_site.py, node scripts/check_inquiry.mjs and appropriate desktop/mobile review. Use the Sites skill to package and publish, and push the same commit normally to GitHub main.
- Verify live release manifests and the changed URLs on both hosts after deployment. Sites may append a Cloudflare detection script to HTML; identify that exact addition separately rather than hiding other differences. The GitHub .nojekyll marker is not served by Sites.
- Record topic, query intent, evidence, changes, original/review dates, source commit, live URLs, deployment result and measurement gaps in the local editorial ledger and the weekly email.

The local editorial ledger and upcoming candidate topics are in work/website-operations/blog-editorial-state.json in the owning Codex task, not in the public website. Read the latest user requests and operating handoffs before each run.

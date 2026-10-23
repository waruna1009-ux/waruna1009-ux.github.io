#!/usr/bin/env python3
"""Check the actual release: links, sitemap, JSON-LD, visible FAQ, contacts, hashes."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re, sys, xml.etree.ElementTree as ET
from urllib.robotparser import RobotFileParser
from site_config import CANONICAL_ORIGIN as BASE, canonical_url
ROOT=Path(__file__).resolve().parents[1]
errors=[]
class Page(HTMLParser):
    # Keep inline text intact (for example, a brand span followed by a period),
    # while separating adjacent headings, paragraphs, and other block elements.
    block_tags={'address','article','aside','blockquote','br','dd','div','dl','dt','figcaption','figure','footer','h1','h2','h3','h4','h5','h6','header','hr','li','main','nav','ol','p','section','table','td','th','tr','ul'}
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.canon=[];self.description=[];self.h1=0;self.hidden=0;self.text=[];self.robots=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ('head','script','style'):self.hidden+=1
        if not self.hidden and tag in self.block_tags:self.text.append(' ')
        if tag=='h1':self.h1+=1
        if a.get('id'):self.ids.add(a['id'])
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
        if tag=='meta' and a.get('name')=='description':self.description.append(a.get('content',''))
        if tag=='meta' and a.get('name')=='robots':
            self.robots.append(a.get('content',''))
            if any(value in a.get('content','') for value in ['noindex','nosnippet','nofollow']):errors.append('Unexpected indexing/snippet restriction')
        for key in ('href','src'):
            if a.get(key):self.links.append(a[key])
    def handle_endtag(self,tag):
        if tag in ('head','script','style'):self.hidden-=1
        if not self.hidden and tag in self.block_tags:self.text.append(' ')
    def handle_data(self,text):
        if not self.hidden:self.text.append(text)
def norm(text):return re.sub(r'\s+',' ',text).strip()
pages={}
for p in list(ROOT.glob('*.html'))+list((ROOT/'blog').glob('*.html')):
    if p.name.startswith('google'):continue
    doc=Page();doc.feed(p.read_text());pages[p.resolve()]=doc
    if doc.h1!=1:errors.append(f'{p.name}: expected one h1, found {doc.h1}')
    if len(doc.canon)!=1:errors.append(f'{p.name}: canonical missing/duplicate')
    elif doc.canon[0]!=canonical_url(p.relative_to(ROOT).as_posix()):errors.append(f'{p.name}: canonical differs from primary public URL')
    if len(doc.robots)!=1:errors.append(f'{p.name}: explicit robots policy missing/duplicate')
    if len(doc.description)!=1 or len(doc.description[0])<30:errors.append(f'{p.name}: missing/empty description')
    if not any(x.startswith('mailto:waruna825@outlook.com') for x in doc.links):errors.append(f'{p.name}: missing email link')
    if not any(x.startswith('https://wa.me/8613954508112') for x in doc.links):errors.append(f'{p.name}: missing WhatsApp link')
    visible=norm(''.join(doc.text))
    types=[]
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',p.read_text(),re.S):
        try: obj=json.loads(block)
        except ValueError:errors.append(f'{p.name}: invalid JSON-LD');continue
        types.append(obj.get('@type'))
        if obj.get('@type')=='Organization':
            if obj.get('@id')!=BASE+'/#organization' or obj.get('email')!='waruna825@outlook.com' or obj.get('telephone')!='+8613954508112':errors.append(f'{p.name}: inconsistent company identity')
        if obj.get('@type') in ('WebPage','AboutPage','ContactPage','CollectionPage') and obj.get('url')!=canonical_url(p.relative_to(ROOT).as_posix()):errors.append(f'{p.name}: page schema canonical mismatch')
        if obj.get('@type')=='FAQPage':
            for faq in obj['mainEntity']:
                if norm(faq['name']) not in visible or norm(faq['acceptedAnswer']['text']) not in visible:
                    errors.append(f'{p.name}: FAQ schema not represented in visible text: '+faq['name'])
    if types.count('Organization')!=1 or types.count('WebSite')!=1:errors.append(f'{p.name}: missing/duplicate company or website entity')
    if len(visible)<200:errors.append(f'{p.name}: insufficient readable HTML content')
for p,doc in pages.items():
    for href in doc.links:
        u=urlsplit(href)
        if u.scheme and not href.startswith(BASE+'/'):continue
        if u.netloc and u.netloc!=urlsplit(BASE).netloc:continue
        target=ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') or u.netloc else p.parent/unquote(u.path)
        if not u.path:target=p
        if target.is_dir():target=target/'index.html'
        if not target.is_file() and not target.suffix and target.with_suffix('.html').is_file():target=target.with_suffix('.html')
        if not target.is_file():errors.append(f'{p.name}: broken link '+href);continue
        if u.fragment and target.resolve() in pages and unquote(u.fragment) not in pages[target.resolve()].ids:errors.append(f'{p.name}: missing fragment '+href)
canonical={x.canon[0] for x in pages.values() if x.canon}
sitemap={x.text for x in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
if canonical!=sitemap:errors.append('Sitemap differs from canonical page set')
llms_urls=re.findall(r'\]\((https://[^)]+)\)',(ROOT/'llms.txt').read_text())
if set(llms_urls)!=canonical:errors.append('llms.txt differs from canonical page set')
robots=RobotFileParser();robots.parse((ROOT/'robots.txt').read_text().splitlines())
if robots.site_maps()!=[BASE+'/sitemap.xml']:errors.append('robots sitemap does not point to primary site')
for agent in ['Googlebot','bingbot','OAI-SearchBot','PerplexityBot','Claude-SearchBot','ChatGPT-User']:
    for url in canonical:
        if not robots.can_fetch(agent,url):errors.append(f'{agent}: blocked {url}')
for p in (ROOT/'dist').rglob('*'):
    if p.is_file() and (p.name in ['README.md','AGENTS.md'] or p.suffix in ['.py','.toml'] or any(part in p.relative_to(ROOT/'dist').parts for part in ['work','outputs','.git'])):errors.append('Nonpublic operating file in release: '+str(p))
manifest=json.loads((ROOT/'site-release.json').read_text())
for rel,expected in manifest['files'].items():
    for base in (ROOT,ROOT/'dist'):
        p=base/rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:errors.append('Release hash mismatch: '+str(p))
digest=hashlib.sha256(json.dumps(manifest['files'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
if digest!=manifest['content_sha256']:errors.append('Invalid release digest')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(json.dumps({'status':'passed','pages':len(pages),'release_files':len(manifest['files']),'checks':['links and fragments','primary canonical URLs','sitemap and robots','search crawler permissions','llms directory','company identity and JSON-LD','visible FAQ and static text','contact links','public-file boundary','source and dist hashes']}))

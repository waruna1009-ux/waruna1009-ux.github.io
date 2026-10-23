#!/usr/bin/env python3
"""Build the same public files served by GitHub Pages into dist for Sites."""
from pathlib import Path
from datetime import date
import hashlib, json, re, shutil, subprocess
from html import unescape
from xml.sax.saxutils import escape
from site_config import CANONICAL_ORIGIN as BASE, canonical_url

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ['robots.txt', 'sitemap.xml', 'llms.txt', 'humans.txt', 'CNAME', '.nojekyll']

def public_files():
    paths = list(ROOT.glob('*.html')) + list((ROOT/'blog').glob('*.html'))
    paths += [ROOT/n for n in PUBLIC if (ROOT/n).is_file()]
    paths += [p for p in (ROOT/'assets').rglob('*') if p.is_file() and p.suffix.lower() in {'.css','.js','.jpg','.jpeg','.png','.webp','.svg','.ico','.woff2'}]
    return sorted(paths)

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()

def main():
    changed=set(git('diff','HEAD','--name-only').splitlines())
    changed.update(git('ls-files','--others','--exclude-standard').splitlines())
    urls=[]
    directory=[]
    for p in public_files():
        if p.suffix != '.html' or p.name.startswith('google'): continue
        rel=p.relative_to(ROOT).as_posix()
        canonical=re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"',p.read_text())
        if not canonical: raise ValueError('Missing canonical: '+rel)
        if canonical[1] != canonical_url(rel): raise ValueError('Unexpected canonical: '+rel)
        lastmod=date.today().isoformat() if rel in changed else git('log','-1','--format=%cs','--',rel)
        urls.append((canonical[1],lastmod or date.today().isoformat()))
        title=unescape(re.search(r'<title>(.*?)</title>',p.read_text(),re.S)[1])
        directory.append((rel,title,canonical[1]))
    if len({u for u,_ in urls})!=len(urls): raise ValueError('Duplicate canonical URLs')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap+=''.join('  <url><loc>'+escape(u)+'</loc><lastmod>'+d+'</lastmod></url>\n' for u,d in sorted(urls))+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap)
    summary='''# Yantai Dingdingmiao Seafood

> Seafood trading and sourcing company in Yantai, Shandong, China, welcoming global buyer inquiries across seafood categories.

We welcome products not shown in the catalog. Our role is supplier search, quotation coordination and support for an agreed transaction. Services and any fee or commission are agreed per engagement. The website is not a statement of owned factories, guaranteed stock, certification or fixed prices. Availability, origin, documents and destination suitability are confirmed per inquiry.

Contact: waruna825@outlook.com | WhatsApp +86 13954508112 | https://wa.me/8613954508112
Languages: English and Chinese.
This directory is supplementary; the linked visible pages are the primary content.

'''
    for heading,is_blog in [('Company, services and product examples',False),('Buyer guides',True)]:
        summary+='## '+heading+'\n'
        summary+=''.join('- ['+title+']('+url+')\n' for rel,title,url in directory if rel.startswith('blog/')==is_blog)
        summary+='\n'
    (ROOT/'llms.txt').write_text(summary.rstrip()+'\n')
    paths=public_files()
    checksums={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    digest=hashlib.sha256(json.dumps(checksums,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    manifest={'schema_version':1,'canonical_origin':BASE,'content_sha256':digest,'files':checksums}
    (ROOT/'site-release.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
    target=ROOT/'dist'
    if target.exists(): shutil.rmtree(target)
    for p in paths+[ROOT/'site-release.json']:
        out=target/p.relative_to(ROOT);out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,out)
    print(json.dumps({'public_files':len(checksums),'indexable_pages':len(urls),'content_sha256':digest}))

if __name__=='__main__':main()

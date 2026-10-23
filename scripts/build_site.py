#!/usr/bin/env python3
"""Build the same public files served by GitHub Pages into dist for Sites."""
from pathlib import Path
from datetime import date
import hashlib, json, re, shutil, subprocess
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://waruna1009-ux.github.io'
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
    for p in public_files():
        if p.suffix != '.html' or p.name.startswith('google'): continue
        rel=p.relative_to(ROOT).as_posix()
        canonical=re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"',p.read_text())
        if not canonical: raise ValueError('Missing canonical: '+rel)
        if not canonical[1].startswith(BASE+'/'): raise ValueError('Unexpected canonical: '+rel)
        lastmod=date.today().isoformat() if rel in changed else git('log','-1','--format=%cs','--',rel)
        urls.append((canonical[1],lastmod or date.today().isoformat()))
    if len({u for u,_ in urls})!=len(urls): raise ValueError('Duplicate canonical URLs')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap+=''.join('  <url><loc>'+escape(u)+'</loc><lastmod>'+d+'</lastmod></url>\n' for u,d in sorted(urls))+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(sitemap)
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

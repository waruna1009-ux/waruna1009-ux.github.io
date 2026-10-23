"""Shared publication identity; private operating files are never public assets."""
CANONICAL_ORIGIN = 'https://dingdingmiao-seafood.genialpike6.chatgpt.site'
MIRROR_ORIGIN = 'https://waruna1009-ux.github.io'

def canonical_url(relative_path):
    if relative_path == 'index.html':
        return CANONICAL_ORIGIN + '/'
    if relative_path.endswith('/index.html'):
        return CANONICAL_ORIGIN + '/' + relative_path[:-10]
    return CANONICAL_ORIGIN + '/' + relative_path.removesuffix('.html')

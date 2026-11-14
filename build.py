#!/usr/bin/env python3
"""Buduje statyczną stronę tomekbaczkowski.pl do folderu _site/.

Bez zależności, wystarczy Python 3.8+.
  python3 build.py                        -> _site/
  python3 -m http.server -d _site 8000    -> podgląd na http://localhost:8000

Strona = plik w src/pages/. Na górze pliku komentarz z ustawieniami w JSON:
  <!--{"path": "kariera/", "nav": "kariera/", "title": "...", "description": "..."}-->
W treści:
  {{R}}            -> względna ścieżka do katalogu głównego (działa na github.io i na domenie)
  {{> nazwa}}      -> wstawia src/partials/nazwa.html
Twarde spacje po jednoliterowych spójnikach i przyimkach wstawia build, nie trzeba ich pisać ręcznie.
"""
import json, re, shutil, datetime
from pathlib import Path

ROOT = Path(__file__).parent
SRC, OUT = ROOT / 'src', ROOT / '_site'
SITE_URL = 'https://tomekbaczkowski.pl/'

layout = (SRC / 'layout.html').read_text(encoding='utf-8')
partials = {p.stem: p.read_text(encoding='utf-8') for p in (SRC / 'partials').glob('*.html')}


def expand(html):
    for _ in range(3):  # partiale mogą zawierać partiale
        html = re.sub(r'\{\{>\s*([\w-]+)\s*\}\}', lambda m: partials[m.group(1)], html)
    return html


def rel_root(path):
    return '../' * path.count('/')


def nbsp(html):
    """Twarda spacja po a, i, o, u, w, z w tekście (nie w znacznikach, skryptach i stylach)."""
    def text(m):
        return re.sub(r'(?<![\wąćęłńóśźżĄĆĘŁŃÓŚŹŻ&;])([aiouwzAIOUWZ]) (?=\S)', '\\1\u00a0', m.group(0))
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', html, flags=re.S)
    return ''.join(p if p.startswith(('<script', '<style')) else re.sub(r'>[^<>]+<', text, p) for p in parts)


if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(SRC / 'static', OUT)

pages = []
for f in sorted((SRC / 'pages').glob('*.html')):
    raw = f.read_text(encoding='utf-8')
    m = re.match(r'\s*<!--(\{.*?\})-->\s*', raw, re.S)
    meta = json.loads(m.group(1))
    body = raw[m.end():]
    path = meta['path']  # '' = strona główna, 'kariera/' = podstrona, '404.html' = plik
    r = meta.get('root', rel_root(path))
    jsonld = meta.get('jsonld')
    jsonld_html = ''
    if jsonld:
        items = jsonld if isinstance(jsonld, list) else [jsonld]
        jsonld_html = '\n'.join('<script type="application/ld+json">' + json.dumps(i, ensure_ascii=False) + '</script>' for i in items)
    html = layout
    repl = {
        '{{CONTENT}}': expand(body),
        '{{TITLE}}': meta['title'],
        '{{DESC}}': meta['description'],
        '{{CANONICAL}}': SITE_URL + path,
        '{{JSONLD}}': jsonld_html,
        '{{ROBOTS}}': '<meta name="robots" content="noindex">' if meta.get('noindex') else '',
        '{{OG_IMAGE}}': SITE_URL + 'img/' + meta.get('image', 'portret-tomasz-baczkowski.webp'),
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    # zaznaczenie bieżącej pozycji w menu
    nav = meta.get('nav')
    html = re.sub(r' data-nav="([^"]*)"', lambda mm: ' aria-current="page"' if nav is not None and mm.group(1) == nav else '', html)
    html = nbsp(html.replace('{{R}}', r))
    target = OUT / (path + 'index.html' if path == '' or path.endswith('/') else path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8')
    if not meta.get('noindex'):
        pages.append(path)

# Przekierowania: stare adresy, które mają nie dawać błędu 404
redirects = {
    'aftersales/': 'skuteczny-aftersales/',
    'kombucha/': 'https://kombuczka.pl/',
}
for old, new in redirects.items():
    t = OUT / old / 'index.html'
    t.parent.mkdir(parents=True, exist_ok=True)
    external = new.startswith('http')
    url = new if external else SITE_URL + new
    href = new if external else rel_root(old) + new
    t.write_text(f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>Przeniesione</title>'
                 f'<link rel="canonical" href="{url}"><meta name="robots" content="noindex">'
                 f'<meta http-equiv="refresh" content="0; url={href}"></head>'
                 f'<body><p>Ta strona jest teraz tutaj: <a href="{href}">{url}</a></p></body></html>', encoding='utf-8')

today = datetime.date.today().isoformat()
(OUT / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{SITE_URL}{p}</loc><lastmod>{today}</lastmod></url>\n' for p in pages if p != '404.html') +
    '</urlset>\n', encoding='utf-8')
(OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n', encoding='utf-8')
(OUT / '.nojekyll').write_text('', encoding='utf-8')
print(f'Zbudowano {len(pages)} stron do {OUT}')

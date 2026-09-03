import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_DIR = os.path.join(ROOT, 'html')

def esc(s):
    return html.escape(str(s), quote=False)

def write_page(name, body, title, extra_css=''):
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title>
<link rel="stylesheet" href="style.css">
<style>{extra_css}</style></head>
<body>{body}</body></html>"""
    path = os.path.join(HTML_DIR, name + '.html')
    with open(path, 'w') as f:
        f.write(doc)
    print('wrote', path)

def masthead(title, sub, est=''):
    return f'<div class="masthead"><div class="title">{title}</div><div class="sub">{sub}</div>' + (f'<div class="est">{est}</div>' if est else '') + '</div>'

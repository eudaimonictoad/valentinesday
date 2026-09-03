from common import *
from content_recipes import RECIPES

CSS = """
.sect { font-family: 'IM Fell DW Pica SC'; font-size: 14pt; letter-spacing: 0.1em; text-align: center; margin: 8px 0 4px; break-after: avoid; }
.sect::before, .sect::after { content: ' ❧ '; font-family: 'Old Standard TT'; }
.r { break-inside: avoid; margin-bottom: 7px; font-size: 9.6pt; }
.r .n { font-family: 'IM Fell English SC'; font-size: 11.5pt; }
.r .m { text-align: justify; }
.r .p { font-style: italic; margin-top: 1px; }
.r .p::before { content: '☞ '; font-style: normal; }
.preface { font-size: 10.5pt; text-align: justify; margin: 6px 0 4px; }
"""

def build():
    sections = []
    for sec in dict.fromkeys(r[0] for r in RECIPES):
        items = ''.join(f'<div class="r"><div class="n">{esc(n)}</div><div class="m">{esc(m)}</div><div class="p">{esc(p)}</div></div>' for s, n, m, p in RECIPES if s == sec)
        sections.append(f'<div class="sect">{esc(sec)}</div>{items}')
    body = f"""<div class="page">
{masthead('The Household Receipt Book', 'Seventy-Four Short Receipts for the Modern Flat', 'Each with its Proper Accompaniment · Compiled by a Lady of the Fourth Floor')}
<p class="preface">The receipts that follow are brief, because the reader is busy, and honest, because the reader is clever. To each is appended the manner in which it is best enjoyed, for a dish taken in the wrong place or during the wrong pastime is only half a dish. The compiler has tested every pairing personally and regrets several.</p>
<div class="cols2">{''.join(sections)}</div>
<div class="foot">The Household Receipt Book</div>
</div>"""
    write_page('05-household-receipt-book', body, 'The Household Receipt Book', CSS)

if __name__ == '__main__':
    build()

from common import *
from content_knives import KNIVES

CSS = """
.intro { font-style: italic; text-align: center; margin: 4px 0 10px; font-size: 10.5pt; }
.knife { break-inside: avoid; margin-bottom: 9px; }
.knife .head { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px dotted #000; }
.knife .name { font-family: 'IM Fell DW Pica SC', serif; font-size: 12pt; letter-spacing: 0.04em; }
.knife .no { font-family: 'Old Standard TT', serif; font-size: 9pt; margin-right: 6px; }
.knife .wt { font-family: 'Old Standard TT', serif; font-size: 10pt; white-space: nowrap; }
.knife .origin { font-style: italic; font-size: 9.5pt; }
.knife .desc { font-size: 9.6pt; text-align: justify; margin-top: 2px; }
.knife .price { font-family: 'Old Standard TT', serif; font-size: 9.5pt; text-align: right; }
.notice { border: 1px solid #000; padding: 6px 10px; font-size: 9.5pt; text-align: center; margin-top: 8px; }
"""

def build():
    entries = []
    for i, (name, origin, wt, desc, price) in enumerate(KNIVES, 1):
        entries.append(f"""<div class="knife">
<div class="head"><div><span class="no">No. {i}.</span><span class="name">{esc(name)}</span></div><div class="wt">Weight {wt} g</div></div>
<div class="origin">Made in {esc(origin)}.</div>
<div class="desc">{esc(desc)} <span class="price">— Price ${price}</span></div>
</div>""")
    half = 12
    body = f"""
<div class="page">
{masthead('Hawthorne &amp; Daughters', 'Purveyors of Fine Cutlery · Catalogue No. 47', 'Established 1887 · Blades for Every Purpose, and Several for None')}
<p class="intro">Being a complete list of the knives we presently offer, with their weights in grams as taken on the shop scale, their places of manufacture, and a frank account of what each is for. Illustrations have been omitted this season owing to a dispute with the engraver.</p>
<div class="cols2">{''.join(entries[:half])}</div>
<div class="foot">Hawthorne &amp; Daughters · Continued Overleaf</div>
</div>
<div class="page">
<div class="cols2">{''.join(entries[half:])}</div>
<div class="notice">All weights are stated in grams and were taken with the knife dry and the scale level. A knife found to differ from its stated weight by more than a few grams is either not our knife or has been used on a mattress. Prices include postage within the county. No refunds on the Ceiling Dart.</div>
<div class="foot">Hawthorne &amp; Daughters · Catalogue No. 47 · Page the Last</div>
</div>"""
    write_page('01-knife-catalogue', body, 'Hawthorne & Daughters Cutlery Catalogue', CSS)

if __name__ == '__main__':
    build()

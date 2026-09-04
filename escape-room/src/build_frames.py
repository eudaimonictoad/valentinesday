from common import *
from content_clues import CLUES

# The six painting backs, printed instead of handwritten. Cut on the frame line and
# tape one to the back of each painting. The painting's name sits ABOVE the frame so
# it is trimmed away — she must not be told which picture she is holding.

CSS = """
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.22in 0.34in; margin-top: 2px; }
.slot { break-inside: avoid; }
.tag { font-family: 'IM Fell DW Pica SC'; font-size: 8.4pt; letter-spacing: 0.12em;
       padding-bottom: 3px; white-space: nowrap; }
.tag .sc { font-size: 7.2pt; letter-spacing: 0.06em; font-style: italic;
           font-family: 'IM Fell English'; }
.card { border: 1.2px solid #000; height: 2.12in; padding: 10px 14px;
        display: flex; flex-direction: column; justify-content: center; text-align: center; }
.card .rule { border-top: 3px double #000; width: 42%; margin: 0 auto 9px; }
.card .rule.b { margin: 9px auto 0; }
.card .txt { font-size: 11.6pt; line-height: 1.42; font-style: italic; }
.card .url { font-family: 'Old Standard TT'; font-weight: 700; font-style: normal;
                 letter-spacing: 0.02em; white-space: nowrap; }
.card .orn { font-size: 10pt; letter-spacing: 0.3em; margin-top: 7px; }
.head { font-size: 9.2pt; text-align: justify; margin: 0 0 7px; }
.masthead { padding: 7px 0 6px; margin-bottom: 7px; }
.masthead .title { font-size: 26pt; }
"""


def card(label, text):
    return f"""<div class="slot">
<div class="tag">&#9986; {label.upper()} <span class="sc">&mdash; cut on the line, this row is trimmed off</span></div>
<div class="card">
  <div class="rule"></div>
  <div class="txt">{text}</div>
  <div class="rule b"></div>
  <div class="orn">&middot; &middot; &middot;</div>
</div></div>"""


def build():
    cards = ''.join(card(l, t) for l, t in CLUES)
    body = f"""<div class="page">
{masthead('The Six Painting Backs', 'Cut these out and fasten one to the back of each picture', 'Game-master&rsquo;s sheet · the small name above each frame is for you, and is cut away')}
<p class="head">One card for each painting. The line of small capitals above a frame names the picture it
belongs to; it sits outside the frame so that cutting the card out removes it. Tape or clip the card to the back of
the painting with the writing facing out. Nothing else goes on the backs.</p>
<div class="grid">{cards}</div>
</div>"""
    write_page('14-painting-back-clues', body, 'The Six Painting Backs', CSS)


if __name__ == '__main__':
    build()

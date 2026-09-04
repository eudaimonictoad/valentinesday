import random
from common import *

# The two real entries. Page 12 of The Prophet opens "Like sheaves of corn he gathers you unto himself";
# page 15 carries "Give one another of your bread but eat not from the same loaf" (bread is its sixth word).
REAL = {
    12: "the fourth word of the first line",
    15: "the sixth word of the first sentence on the page that begins with <b>Give</b>",
}
PAGES = 84
ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
STARTS = ['And', 'For', 'But', 'You', 'Your', 'Let', 'When', 'Then', 'Love', 'Give', 'Say', 'If', 'Yet', 'Even', 'The', 'Nay', 'Verily', 'He', 'Only', 'Much']

def instruction(rng):
    kind = rng.random()
    if kind < 0.34:
        return f"the {rng.choice(ORD[:8])} word of the {rng.choice(ORD[:9])} line"
    if kind < 0.50:
        return f"the {rng.choice(ORD[:7])} word of the last line"
    if kind < 0.64:
        return f"the last word of the {rng.choice(ORD[:6])} sentence"
    if kind < 0.74:
        return f"the {rng.choice(ORD[:6])} word of the last sentence"
    return f"the {rng.choice(ORD[:8])} word of the first sentence on the page that begins with <b>{rng.choice(STARTS)}</b>"

CSS = """
.book { text-align: center; font-family: 'IM Fell DW Pica SC'; font-size: 15pt; letter-spacing: 0.15em; margin: 4px 0 0; }
.by { text-align: center; font-style: italic; font-size: 11pt; margin-bottom: 6px; }
.preface { font-size: 10.3pt; text-align: justify; margin: 4px 0 8px; }
.grid { column-count: 3; column-gap: 0.22in; column-rule: 1px solid #000; }
.e { break-inside: avoid; font-size: 9.2pt; line-height: 1.25; margin-bottom: 2.5px; display: flex; gap: 6px; }
.e .n { font-family: 'Old Standard TT'; font-weight: 700; flex: 0 0 1.9em; text-align: right; }
.rulebox { border: 1px solid #000; padding: 6px 12px; font-size: 10pt; text-align: center; margin-top: 10px; }
"""

def build():
    rng = random.Random(1923)
    entries = []
    for p in range(1, PAGES + 1):
        ins = REAL.get(p) or instruction(rng)
        entries.append(f'<div class="e"><span class="n">{p}.</span><span>{ins}.</span></div>')
    body = f"""<div class="page">
{masthead("A Reader's Concordance", 'One Word from every Page, for the Reader who has no Time for the Rest', 'The Pocket Library Series · No. 9')}
<div class="book">The Prophet</div>
<div class="by">by Kahlil Gibran</div>
<p class="preface">The busy reader cannot be expected to read a whole book, nor even a whole page. This concordance therefore names, for each page of <i>The Prophet</i>, the single word that the editors consider sufficient. Turn to the page, count as directed, and take the word. Count words as they are printed, hyphenated words as one, and do not count the page number, the chapter title, or your own doubts.</p>
<div class="grid">{''.join(entries)}</div>
<div class="rulebox">Where two or more pages are sought, the words so found are to be set side by side, in the order in which they were sought, and read as one.</div>
<div class="foot">The Pocket Library Series · A Reader's Concordance</div>
</div>"""
    write_page('08-prophet-concordance', body, "A Reader's Concordance to The Prophet", CSS)

if __name__ == '__main__':
    build()

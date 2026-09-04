# The game-master's setup guide: a flowchart of what runs in parallel, the lock
# order, every hiding place, and exactly what to write by hand. Printed LAST in
# the combined PDF, to be torn off. File name kept for the merge script.
from common import *

CSS = """
.warn { border: 3px double #000; padding: 6px 12px; text-align: center; font-family: 'IM Fell DW Pica SC'; font-size: 12pt; letter-spacing: 0.1em; margin-bottom: 8px; }
h3 { font-family: 'IM Fell DW Pica SC'; font-size: 12pt; letter-spacing: 0.08em; margin: 10px 0 4px; border-bottom: 1px solid #000; }
table { border-collapse: collapse; width: 100%; font-size: 9.4pt; margin-bottom: 6px; }
th { text-align: left; font-family: 'IM Fell DW Pica SC'; font-size: 9pt; letter-spacing: 0.08em; border-bottom: 2px solid #000; padding: 3px 5px; }
td { border-bottom: 1px solid #999; padding: 3px 5px; vertical-align: top; }
td.n { font-family: 'Old Standard TT'; font-weight: 700; white-space: nowrap; width: 1.6em; }
td.loc { font-family: 'IM Fell DW Pica SC'; font-size: 9.5pt; white-space: nowrap; }
ol { margin: 0; padding-left: 18px; font-size: 9.6pt; }
ol li { margin-bottom: 3px; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 0 16px; }
.key { font-family: 'Old Standard TT'; font-weight: 700; }
.mono { font-family: 'Old Standard TT'; letter-spacing: 0.1em; font-size: 12pt; }
.gloss dt { font-family: 'IM Fell DW Pica SC'; font-size: 10pt; margin-top: 4px; }
.gloss dd { margin: 0 0 2px 0; font-size: 9.4pt; }
.write { border: 1px solid #000; padding: 6px 10px; margin: 6px 0; font-size: 9.6pt; }
.write b { font-family: 'IM Fell DW Pica SC'; font-weight: normal; letter-spacing: 0.06em; }
svg text { font-family: 'IM Fell English', serif; }
"""

# ---------- flowchart ----------
W = 720
def box(x, y, w, h, lines, fill='#fff', color='#000', size=10.5, bold=False):
    fam = "'IM Fell DW Pica SC'" if bold else "'IM Fell English'"
    n = len(lines); lh = size * 1.25
    y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
    ts = ''.join(f'<text x="{x + w/2}" y="{y0 + i*lh:.1f}" text-anchor="middle" font-size="{size}" font-family="{fam}" fill="{color}">{esc(t)}</text>' for i, t in enumerate(lines))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="#000" stroke-width="1"/>{ts}'

def payload(x, y, w, h, lines):
    return box(x, y, w, h, lines, fill='#000', color='#fff', size=10, bold=True)

def band(x, y, w, h, label):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="#000" stroke-width="0.8" stroke-dasharray="4 3"/>'
            f'<rect x="{x+8}" y="{y-8}" width="{len(label)*6.6+12}" height="16" fill="#fff"/>'
            f'<text x="{x+14}" y="{y+4}" font-size="10" font-family="\'IM Fell DW Pica SC\'" letter-spacing="1.5">{esc(label)}</text>')

def arrow(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="1.2" marker-end="url(#ah)"/>'

def chain(x, y, w, steps, gap=8, h=28):
    """Vertical chain of step boxes; returns svg and the y just below the last box."""
    out = []; yy = y
    for i, lines in enumerate(steps):
        out.append(box(x, yy, w, h, lines))
        if i < len(steps) - 1:
            out.append(arrow(x + w/2, yy + h, x + w/2, yy + h + gap - 1))
        yy += h + gap
    return ''.join(out), yy - gap

def chart():
    s = ['<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker></defs>']
    # Tier 0
    s.append(band(10, 22, 700, 66, 'MINUTE ONE'))
    s.append(box(20, 34, 320, 44, ['HANDED TO HER: the letter and the Milk Crate painting.', 'Letter gives sarahs.quest and ends: breathe in, breathe out.']))
    s.append(box(370, 34, 330, 44, ['OUT IN THE OPEN: the nine printables, the flyer, the lemons,', 'the knife AND the scale, The Prophet, the locked suitcase.']))
    # Tier 1: A and C in parallel
    s.append(band(10, 112, 700, 258, 'OPEN AT THE SAME TIME  ·  two lines, either order'))
    a, ya = chain(20, 126, 320, [
        ['Milk Crate painting, back  →  Ed Sheeran'],
        ["Stars and Their Notes  →  The Barista's Hornpipe, two notes"],
        ['Parlour Songbook, those two shapes  →  12 and 15'],
        ['Concordance + The Prophet, pages 12 and 15  →  CORN BREAD'],
        ['Receipt Book, cornbread  →  a game of backgammon'],
    ])
    s.append(a); s.append(arrow(180, ya, 180, ya + 9))
    s.append(payload(20, ya + 10, 320, 36, ['BACKGAMMON SET', 'Plate II  ·  the Patricia painting']))
    c, yc = chain(370, 126, 330, [
        ['Put the knife on the scale  →  79 g'],
        ['Knife Catalogue, 79 g  →  No. 9, the Lemonade Knife'],
        ['Cut the lemons open  →  the Joker'],
        ["Cartomancer's Guide, the Joker  →  in the Dutch oven"],
    ])
    s.append(c); s.append(arrow(535, yc, 535, yc + 9))
    s.append(payload(370, yc + 10, 330, 36, ['DUTCH OVEN', 'Plate I  ·  the DARK BLUE key']))
    # Tier 2
    s.append(band(10, 392, 700, 76, 'OPENS WHEN THE MUSIC LINE IS DONE'))
    s.append(arrow(180, ya + 46, 180, 404))
    s.append(box(20, 406, 320, 28, ['Patricia painting → Register → a small painted egg…']))
    s.append(arrow(340, 420, 369, 420))
    s.append(payload(370, 402, 330, 36, ['WINGSPAN BOX', 'Hamlet painting  ·  fairy painting  ·  a Queen of Hearts']))
    # Tier 3: three at once
    s.append(band(10, 492, 700, 112, 'THREE AT ONCE  ·  any order'))
    lanes = [
        (20, ["Queen of Hearts → Cartomancer's Guide", '→ the back of the upstairs toilet'], ['TOILET CISTERN', 'the BLACK key']),
        (252, ['Hamlet → Hamnet → Chloé Zhao', '→ Register, Chloe → a young tree in a pot'], ['THE BONSAI', 'blue-light pen · Abyssinia & Gleaners paintings']),
        (484, ['Fairy houses → Shirley', '→ Register → a bottle kept for company'], ['LIQUOR CABINET', 'the Pig-Pen Alphabet sheet']),
    ]
    for x, lines, pay in lanes:
        s.append(arrow(535, 438, x + 108, 504))
        s.append(box(x, 506, 216, 36, lines, size=9.6))
        s.append(arrow(x + 108, 542, x + 108, 552))
        s.append(payload(x, 553, 216, 40, pay))
    # Tier 4: the lock
    s.append(band(10, 628, 700, 330, 'THE LOCK  ·  needs a piece from every line'))
    s.append(box(20, 642, 320, 44, ['Abyssinia painting + pigpen sheet → sarahs.quest,', 'the Ethiopian flag is Plate VII, turned over → HALF PAST THREE']))
    s.append(box(370, 642, 330, 44, ['Flyer → bathroom. Blue-light pen + pigpen sheet', '→ under ALIEN BLUES: BREATHE IN BREATHE OUT LOOK INSIDE']))
    s.append(arrow(535, 686, 535, 698))
    s.append(payload(370, 700, 330, 32, ['INSIDE THE MEDITATION CUSHION', 'the card, in wheel symbols']))
    s.append(arrow(180, 686, 180, 746)); s.append(arrow(535, 732, 535, 746))
    s.append(box(20, 748, 680, 44, ['THE WHEEL: pin Plate II on Plate I, set the hands to 3:30, decode the card', 'H5W 6WJ OQ OY H5W L8WWZW8  =  THE KEY IS IN THE FREEZER'], size=10.5))
    s.append(arrow(360, 792, 360, 804))
    s.append(payload(20, 806, 680, 32, ['THE FREEZER  ·  the PURPLE key, in a ziplock']))
    s.append(arrow(360, 838, 360, 852))
    s.append(box(20, 854, 216, 44, ['BLACK key (cistern)', 'opens the SUITCASE'], size=10.5))
    s.append(arrow(236, 876, 251, 876))
    s.append(box(252, 854, 216, 44, ['DARK BLUE key (Dutch oven)', 'opens the BACKPACK inside it'], size=10.5))
    s.append(arrow(468, 876, 483, 876))
    s.append(payload(484, 854, 216, 44, ['PURPLE key opens the', 'COMPARTMENT: the prize']))
    s.append(f'<text x="360" y="930" text-anchor="middle" font-size="10" font-style="italic">Nothing can be shortcut: the card is unreadable without both plates and the time, and those come from three different places.</text>')
    return f'<svg viewBox="0 0 {W} 950" width="6.85in" xmlns="http://www.w3.org/2000/svg">{"".join(s)}</svg>'

PLACES = [
 ("Her hands", "The welcome letter and the Milk Crate painting. Nothing is hidden on the painting; its back just carries the written clue."),
 ("Out in the open", "The nine printables scattered about; the flyer on the fridge; a bowl of lemons, one loaded; the knife and the kitchen scale on the counter; The Prophet on the shelf among many books; the locked suitcase"),
 ("Backgammon set", "Plate II; the Patricia painting"),
 ("Wingspan box", "The Hamlet painting; the fairy painting; a real Queen of Hearts playing card"),
 ("Toilet cistern", "The BLACK key in a ziplock bag. Nothing else. No paper, no paintings."),
 ("The bonsai", "The blue-light pen; the Abyssinia painting; the Gleaners painting (in a bag, under or beside the pot, not buried)"),
 ("Liquor cabinet", "The Pig-Pen Alphabet key sheet"),
 ("Dutch oven", "Plate I with a brad taped to it; the DARK BLUE key"),
 ("Bathroom wall or mirror", "ALIEN BLUES in dry-erase marker; the pigpen glyphs from the tracing sheet in invisible ink beneath"),
 ("Inside the meditation cushion", "The card of wheel symbols, in a small envelope, just inside the zip"),
 ("The freezer", "The PURPLE key in a ziplock, tucked behind the frozen peas. Nothing points here until the wheel is decoded."),
 ("Suitcase", "The backpack. Padlocked with the BLACK lock."),
 ("Backpack", "The prize in its inner compartment, padlocked with the PURPLE lock; the main zip padlocked with the DARK BLUE lock"),
]

def build():
    prows = ''.join(f'<tr><td class="loc">{esc(a)}</td><td>{esc(b)}</td></tr>' for a, b in PLACES)
    page1 = f"""<div class="page">
<div class="warn">Game-master's setup guide · remove these leaves before she arrives</div>
{chart()}
</div>"""
    page2 = f"""<div class="page">
<h3>Plain English for the things with odd names</h3>
<dl class="gloss">
<dt>The Concordance</dt><dd>The one-page sheet headed "A Reader's Concordance" with "The Prophet, by Kahlil Gibran" printed under the masthead. It gives one word-counting rule for each of 84 pages. She needs a real copy of The Prophet to use it; the sheet itself names the book, so put the book on the shelf among others and nothing more is needed.</dd>
<dt>Plate I and Plate II</dt><dd>The two circles on the cipher-wheel pages. Plate I, "The Dial", is the big one with clock numerals round the rim. Plate II, "The Hands", is the smaller one with two clock hands printed on it. Cut both out. Push a brad (split pin) through the centre of Plate I and tape it there; she pins Plate II on top and turns it until the hands read 3:30.</dd>
<dt>Pigpen</dt><dd>A cipher where each letter is drawn as the walls of the box it sits in. The printed Pig-Pen Alphabet sheet is the key. The only pigpen you write by hand is the wall; the flags' pigpen is already on the website.</dd>
<dt>Wheel symbols</dt><dd>Ordinary letters and digits that only mean something once the wheel is set. You copy them onto the cushion card exactly as printed below.</dd>
</dl>

<h3>Lock and load, in this order, so no key ends up locked inside its own box</h3>
<ol>
<li>Put the prize in the backpack's inner compartment. Padlock that compartment. Set its key aside: this is <span class="key">PURPLE</span>.</li>
<li>Close the backpack's main zip. Padlock it. Set its key aside: <span class="key">DARK BLUE</span>.</li>
<li>Put the backpack inside the suitcase. Padlock the suitcase. Set its key aside: <span class="key">BLACK</span>.</li>
<li>Leave the suitcase somewhere she will see it all evening. It is meant to taunt.</li>
<li>Now hide the three keys: <span class="key">BLACK</span> in a ziplock in the toilet cistern; <span class="key">DARK BLUE</span> in the Dutch oven with Plate I; <span class="key">PURPLE</span> in a ziplock bag in the freezer, behind something frozen. Nothing points at the freezer until she decodes the wheel, so it stays unsearched.</li>
<li><span class="key">LIGHT BLUE</span> and its lock are not used. Put them in a drawer.</li>
</ol>

<div class="foot">Game-master's setup guide · 2 of 4</div>
</div>
<div class="page">
<h3>Every hiding place and what goes in it</h3>
<table><tr><th>Place</th><th>Contents</th></tr>{prows}</table>
<div class="foot">Game-master's setup guide · 3 of 4</div>
</div>"""
    page3 = f"""<div class="page">
<h3>Exactly what to write by hand, and where</h3>
<div class="write"><b>The bathroom wall or mirror.</b> In dry-erase marker, large: <span class="mono">ALIEN BLUES</span>. Directly beneath it, in the invisible-ink pen, copy the pigpen shapes from the tracing sheet (the page before this guide). They read BREATHE IN BREATHE OUT LOOK INSIDE. Test a corner first: glazed tile and glass wipe clean, grout and stone do not. The mirror is the safest surface.</div>
<div class="write"><b>The cushion card.</b> Any scrap of paper or index card will do. Write in capitals, exactly: <span class="mono">H5W 6WJ OQ OY H5W L8WWZW8</span>. Put it in a small envelope. On the envelope: <i>This will mean nothing until the hour is set.</i> Tuck it just inside the cushion's zip.</div>
<div class="write"><b>The six painting backs.</b> Write on the quarter-sheet frames and attach one to each painting.<br>
Milk Crate: <i>The famous man we always see here, who is not him.</i><br>
Patricia's: <i>Just the name. Look her up.</i><br>
Hamlet: <i>We saw the film of this play. Whose film was it?</i><br>
Fairy houses: <i>What was the family name of the one who lived here?</i><br>
Abyssinia: <i>Find this country's colours at sarahs.quest, and turn them over.</i><br>
Gleaners: <i>The café sits in a market named for a country. Its colours are at sarahs.quest too.</i></div>
<div class="write"><b>The welcome letter.</b> Your words. It must contain the address <span class="mono">sarahs.quest</span>, may mention that not everything can be read on the day it is found, and must end with the line <i>breathe in, breathe out.</i></div>
<div class="write"><b>Nothing else is handwritten.</b> The flags' pigpen is on the website. The register, the card guide, the concordance and the rest are printed and final.</div>

<h3>Before she arrives: the five tests</h3>
<ol>
<li>Put your real knife on your real scale. It must read 79 g. Nearest catalogue entries are 58 g and 99 g.</li>
<li>Open your copy of The Prophet. Page 12, fourth word of the first line must be <b>corn</b>. Page 15, the first sentence beginning "Give", sixth word must be <b>bread</b>. If either fails, tell me the real page numbers and I will reprint the concordance.</li>
<li>Shine the blue-light pen on the wall. The pigpen must show. Then wipe a corner to be sure it comes off.</li>
<li>Pin the plates, set 3:30, decode the cushion card yourself. It must read THE KEY IS IN THE FREEZER.</li>
<li>Open sarahs.quest on your phone, tap Plate VII, confirm the pigpen on the back reads HALF PAST THREE.</li>
</ol>

<h3>If she stalls</h3>
<p style="font-size:9.6pt">sarahs.quest/hints.html: eighteen predicaments, each with a nudge, a firmer nudge, and the answer. Linked from the bottom of the flags page. Or just tell her; you are allowed.</p>
<div class="foot">Game-master's setup guide · 4 of 4 · the cipher solution follows, remove that too</div>
</div>"""
    write_page('10-mapping-GAMEMASTER-remove', page1 + page2 + page3, "Game-master's setup guide", CSS)

if __name__ == '__main__':
    build()

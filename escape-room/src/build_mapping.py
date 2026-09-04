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
    s.append(box(20, 34, 320, 44, ['HANDED TO HER: the letter and the Milk Crate painting.', 'The letter gives her the address sarahs.quest.']))
    s.append(box(370, 34, 330, 44, ['OUT IN THE OPEN: seven printed sheets (not the pig-pen key, not the plates),', 'the flyer, the lemons, the knife AND the scale, The Prophet, the locked suitcase.']))
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
    s.append(payload(20, ya + 10, 320, 36, ['HIDE IN THE BACKGAMMON SET:', 'Plate II (the small disc with the hands) + Patricia painting']))
    c, yc = chain(370, 126, 330, [
        ['Put the knife on the scale  →  79 g'],
        ['Knife Catalogue, 79 g  →  No. 9, the Lemonade Knife'],
        ['Cut the lemons open  →  the Joker'],
        ["Cartomancer's Guide, the Joker  →  in the Dutch oven"],
    ])
    s.append(c); s.append(arrow(535, yc, 535, yc + 9))
    s.append(payload(370, yc + 10, 330, 36, ['HIDE IN THE DUTCH OVEN:', 'Plate I (the big dial), with a brad taped to it']))
    # Tier 2
    s.append(band(10, 392, 700, 76, 'OPENS WHEN THE MUSIC LINE IS DONE'))
    s.append(arrow(180, ya + 46, 180, 404))
    s.append(box(20, 406, 320, 28, ['Patricia painting → Register → a small painted egg…']))
    s.append(arrow(340, 420, 369, 420))
    s.append(payload(370, 402, 330, 36, ['HIDE IN THE WINGSPAN BOX:', 'Hamlet painting · fairy painting · a Queen of Hearts']))
    # Tier 3: three at once
    s.append(band(10, 492, 700, 112, 'THREE AT ONCE  ·  any order'))
    lanes = [
        (20, ["Queen of Hearts → Cartomancer's Guide", '→ the back of the upstairs toilet'], ['HIDE IN THE TOILET CISTERN:', 'the BLACK key (opens the suitcase)']),
        (252, ['Hamlet → Hamnet → Chloé Zhao', '→ Register, Chloe → a jar of sweets'], ['HIDE IN THE CANDY JAR:', 'blue-light pen · Abyssinia + Gleaners paintings']),
        (484, ['Fairy houses → Shirley', '→ Register → a bottle kept for company'], ['HIDE IN THE LIQUOR CABINET:', 'the Pig-Pen Alphabet sheet']),
    ]
    for x, lines, pay in lanes:
        s.append(arrow(535, 438, x + 108, 504))
        s.append(box(x, 506, 216, 36, lines, size=9.6))
        s.append(arrow(x + 108, 542, x + 108, 552))
        s.append(payload(x, 553, 216, 40, pay))
    # Tier 4: the lock
    s.append(band(10, 628, 700, 330, 'THE LOCK  ·  needs a piece from every line'))
    s.append(box(20, 642, 320, 44, ['Abyssinia + Gleaners + pigpen sheet → sarahs.quest. Ethiopia is', 'Figure VII (HALF PAST), Italy is Figure XIV (THREE) → 3:30']))
    s.append(box(370, 642, 330, 44, ['Flyer → bathroom. Blue-light pen + pigpen sheet', 'ALIEN BLUES in marker; then BREATHE in BREATHE out open the GREEN thing you SIT on (caps in ink)']))
    s.append(arrow(535, 686, 535, 698))
    s.append(payload(370, 700, 330, 32, ['HIDE INSIDE THE MEDITATION CUSHION:', 'the card:  DW5OY7 H5W VKYJ LKRWQ']))
    s.append(arrow(180, 686, 180, 746)); s.append(arrow(535, 732, 535, 746))
    s.append(box(20, 748, 680, 44, ['THE WHEEL: pin Plate II (hands) on Plate I (dial), set 3:30, decode the card', 'DW5OY7 H5W VKYJ LKRWQ  =  BEHIND THE MANY FACES'], size=10.5))
    s.append(arrow(360, 792, 360, 804))
    s.append(payload(20, 806, 680, 32, ['HIDE BEHIND THE FRAMED PHOTO PUZZLE:  the DARK BLUE key']))
    s.append(arrow(360, 838, 360, 852))
    s.append(box(20, 854, 320, 44, ['BLACK key, from the cistern, opens the SUITCASE', 'early on. Inside: the backpack, still locked.'], size=10.5))
    s.append(arrow(340, 876, 369, 876))
    s.append(payload(370, 854, 330, 44, ['DARK BLUE key opens the BACKPACK', 'the prize']))
    s.append(f'<text x="360" y="930" text-anchor="middle" font-size="10" font-style="italic">Nothing can be shortcut: the card is unreadable without both plates and the time, and those come from three different places.</text>')
    return f'<svg viewBox="0 0 {W} 950" width="6.85in" xmlns="http://www.w3.org/2000/svg">{"".join(s)}</svg>'

PLACES = [
 ("Her hands", "The welcome letter and the Milk Crate painting. Nothing is hidden on the painting; its back just carries the written clue."),
 ("Out in the open", "Seven printed sheets scattered about: knife catalogue, songbook, Stars and Their Notes, receipt book, register, cartomancer's guide, concordance. NOT the pig-pen key (liquor cabinet) and NOT the two plates (backgammon set, Dutch oven). Also the flyer on the fridge; a bowl of lemons, one loaded; the knife and the kitchen scale on the counter; The Prophet on the shelf among many books; the locked suitcase"),
 ("Backgammon set", "Plate II; the Patricia painting"),
 ("Wingspan box", "The Hamlet painting; the fairy painting; a real Queen of Hearts playing card"),
 ("Toilet cistern", "The BLACK key in a ziplock bag. Nothing else, ever. No paper, no paintings."),
 ("The candy jar", "The blue-light pen; the Abyssinia painting; the Gleaners painting. Roll the paintings or lay them under the jar if they will not fit inside."),
 ("Liquor cabinet", "The Pig-Pen Alphabet key sheet"),
 ("Dutch oven", "Plate I, with a brad (split pin) taped to it"),
 ("Bathroom wall or mirror", "ALIEN BLUES in dry-erase marker; the pigpen glyphs from the tracing sheet in invisible ink beneath"),
 ("Inside the meditation cushion", "The cipher card, in a small envelope, tucked just inside the zip where a hand will meet it"),
 ("Behind the framed photo puzzle", "The DARK BLUE key, taped flat to the back of the frame. Nothing points here until the wheel is decoded, so it is never searched."),
 ("Suitcase", "The backpack. The suitcase itself is padlocked with the BLACK lock and left in plain sight all evening."),
 ("Backpack", "The prize. Padlocked with the DARK BLUE lock. All six paintings are placed elsewhere; none is in here."),
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
<dt>Plate I and Plate II</dt><dd><b>&ldquo;Plate&rdquo; always means one of the two cipher discs, and nothing else.</b> Plate I, The Dial, is the big circle with clock numerals round the rim. Plate II, The Hands, is the smaller circle with two clock hands on it. Cut both out. Push a brad (split pin) through the centre of Plate I and tape it there; she lays Plate II on top and turns it until the hands read 3:30. So &ldquo;hide Plate I in the Dutch oven&rdquo; simply means: put the big disc in the Dutch oven.</dd>
<dt>Figure I to Figure XX</dt><dd>The twenty flag cards on sarahs.quest. They carry no country names, only numbers, so Figure VII is the seventh card along. She never needs the number; she recognises Ethiopia and Italy by their colours. The numbers are only here so you can check the right card without counting.</dd>
<dt>Pigpen</dt><dd>A cipher where each letter is drawn as the walls of the box it sits in. The printed Pig-Pen Alphabet sheet is the key. The only pigpen you write by hand is the wall; the flags' pigpen is already on the website.</dd>
<dt>Wheel symbols</dt><dd>Ordinary letters and digits that only mean something once the wheel is set. You copy them onto the cushion card exactly as printed below.</dd>
</dl>

<h3>Lock and load, in this order, so no key ends up locked inside its own box</h3>
<ol>
<li>Put the prize in the backpack. Close it and padlock it. Its key is <span class="key">DARK BLUE</span>.</li>
<li>Put the backpack inside the suitcase. Close the suitcase and padlock it. Its key is <span class="key">BLACK</span>.</li>
<li>Stand the suitcase somewhere she will see it all evening. It is meant to taunt.</li>
<li>Hide <span class="key">BLACK</span> in a ziplock in the toilet cistern. She reaches it mid-game, opens the suitcase, and finds the backpack still locked. That is the moment the evening turns.</li>
<li>Tape <span class="key">DARK BLUE</span> flat to the back of the framed photo puzzle. Masking tape, pressed down so it cannot rattle. Nothing points here until the wheel is decoded.</li>
<li><span class="key">PURPLE</span> and <span class="key">LIGHT BLUE</span> are not used. Put them in a drawer.</li>
</ol>
<p style="font-size:9.4pt;font-style:italic">Two locks is the whole scheme. The wheel exists to produce the second key, so it cannot be skipped.</p>
<div class="foot">Game-master's setup guide &middot; 2 of 5</div>
</div>
<div class="page">
<h3>Every hiding place and what goes in it</h3>
<table><tr><th>Place</th><th>Contents</th></tr>{prows}</table>
<div class="foot">Game-master's setup guide · 3 of 5</div>
</div>"""
    page3 = f"""<div class="page">
<h3>Everything you write by hand · there are only five things</h3>

<div class="write"><b>1 · The welcome letter.</b> Your words, your handwriting. It must do three jobs and no more:
give her the address <span class="mono">sarahs.quest</span>; warn her that some things she finds will not make
sense on the day she finds them; and end with a line in your own voice. Do not explain any puzzle.
Do not mention the suitcase. If you are stuck for an opening: <i>&ldquo;There are six paintings in this apartment and
every one of them is a question. You will need a scale, a knife, a pin, and more patience than I deserve.&rdquo;</i></div>

<div class="write"><b>2 · The six painting backs.</b> Write these on the quarter-sheet frames and clip or tape one to each painting.<br>
&nbsp;&nbsp;<b>Milk Crate</b> &mdash; <i>The famous man we always see here, who is not him.</i><br>
&nbsp;&nbsp;<b>Patricia&rsquo;s</b> &mdash; <i>Just the name. Look her up.</i><br>
&nbsp;&nbsp;<b>Hamlet</b> &mdash; <i>We saw the film of this play. Whose film was it? Look her up by her first name.</i><br>
&nbsp;&nbsp;<b>Fairy houses</b> &mdash; <i>What was the family name of the one who lived here? Look her up.</i><br>
&nbsp;&nbsp;<b>Abyssinia</b> &mdash; <i>This country has another name now. Find its colours at sarahs.quest, and turn them over.</i><br>
&nbsp;&nbsp;<b>Gleaners</b> &mdash; <i>The caf&eacute; sits in a market named for a country. Its colours are at sarahs.quest too. You will need this one and Abyssinia both.</i></div>

<div class="write"><b>3 · The wall.</b> Two inks on one surface. The tracing sheet two pages back shows the whole thing laid out.<br>
&nbsp;&nbsp;<b>Line one, dry-erase marker, large:</b> <span class="mono">ALIEN BLUES</span><br>
&nbsp;&nbsp;<b>Line two, mixed.</b> The lowercase words go in dry-erase marker. The CAPITAL words go in invisible ink, as pig-pen shapes, in the gaps:<br>
&nbsp;&nbsp;<span class="mono">BREATHE in BREATHE out open the GREEN thing you SIT on</span><br>
&nbsp;&nbsp;So what she sees walking in is <i>ALIEN BLUES / ___ in ___ out open the ___ thing you ___ on</i>, a sentence with holes in it.
Under the blue light the holes fill with shapes, and with the pig-pen sheet the shapes read BREATHE, BREATHE, GREEN, SIT. That is 22 shapes to draw.
The visible words give nothing away; the hidden ones are the answer, so she still needs the pen and the sheet. Test a corner first:
glass and glazed tile wipe clean, grout and stone do not. The mirror is the safest surface in the room.</div>

<div class="write"><b>4 · The cipher card.</b> Any scrap of paper. In capitals, exactly, with the spaces where they are:
<div class="mono" style="text-align:center;font-size:15pt;margin:6px 0">DW5OY7 H5W VKYJ LKRWQ</div>
Put it in a small envelope. On the envelope write: <i>This will mean nothing until the hour is set.</i>
Tuck it just inside the cushion&rsquo;s zip, where a hand will meet it straight away.</div>

<div class="write"><b>5 · Three hint envelopes</b> (optional, but they save the evening). Seal three envelopes and label them
<i>If you are stuck on the music</i>, <i>If you are stuck on the knife</i>, and <i>If you are stuck at the very end</i>.
Inside each, one sentence: <i>Everything you need is at sarahs.quest/hints.html &mdash; and I will not think less of you.</i></div>

<h3>What you do not write</h3>
<p style="font-size:9.6pt">The flags&rsquo; pigpen is already on the website. The register, the card guide, the concordance,
the songbook, the knife catalogue and the recipe book are printed and final. The only cipher you draw by hand is the wall.</p>
<div class="foot">Game-master&rsquo;s setup guide · 4 of 5</div>
</div>
<div class="page">
<h3>The five tests, before she arrives</h3>
<ol>
<li><b>The knife.</b> Put your real knife on your real scale. It must read 79 g. The nearest catalogue entries are 58 g and 99 g, so you have about 14 g of slack either way. If it is wildly off, pick a different knife.</li>
<li><b>The book.</b> Open your copy of The Prophet. Page 12, fourth word of the first line, must be <b>corn</b>. Page 15, the first sentence beginning &ldquo;Give&rdquo;, sixth word, must be <b>bread</b>. Editions differ and this is the single most likely thing to break.</li>
<li><b>The wall.</b> Shine the blue-light pen on your writing. The hidden shapes must show clearly between the marker words. Then wipe a corner to be certain both inks come off.</li>
<li><b>The wheel.</b> Cut both plates, pin them, set the hands to half past three, and decode the cipher card yourself. It must read BEHIND THE MANY FACES.</li>
<li><b>The website.</b> Open sarahs.quest on your phone. Tap Figure VII, the green-yellow-red flag with the blue disc: its back must read HALF PAST. Then tap Figure XIV, the green-white-red vertical stripes: its back must read THREE. Together they give half past three.</li>
</ol>

<h3>The order to set the room up</h3>
<ol>
<li>Lock the backpack, put it in the suitcase, lock the suitcase, stand it in the open.</li>
<li>Hide the two keys: BLACK in the cistern, DARK BLUE behind the framed puzzle.</li>
<li>Place all six paintings: Milk Crate in her envelope; Patricia in the backgammon set; Hamlet and the fairy houses in the Wingspan box with the Queen of Hearts; Abyssinia and Gleaners with the candy jar. None goes in the backpack.</li>
<li>Plate II in the backgammon set. Plate I in the Dutch oven. Pig-pen sheet in the liquor cabinet.</li>
<li>Load one lemon with the Joker and set the bowl out. Knife and scale on the counter.</li>
<li>Cipher card into the cushion. Write the wall. Flyer on the fridge.</li>
<li>Scatter the seven open sheets around the room: knife catalogue, songbook, Stars and Their Notes, receipt book, register, cartomancer's guide, concordance. The Prophet onto the shelf among other books. Keep the pig-pen key and both plates for their hiding places.</li>
<li>Tear the last six leaves out of the printed packet and hide them from yourself.</li>
</ol>

<h3>If she stalls</h3>
<p style="font-size:9.6pt"><span class="mono">sarahs.quest/hints.html</span> holds eighteen predicaments, each with a nudge,
then a firmer nudge, then the answer outright. It is linked in a box at the top of the flags page, so she can reach it
on her own and you never have to be the one who gives it away. Or just tell her; you are allowed.</p>
<div class="foot">Game-master&rsquo;s setup guide · 5 of 5 · the cipher solution follows, remove that too</div>
</div>"""
    write_page('10-mapping-GAMEMASTER-remove', page1 + page2 + page3, "Game-master's setup guide", CSS)

if __name__ == '__main__':
    build()

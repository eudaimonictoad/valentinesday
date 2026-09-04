# The game-master's mapping sheet. Printed LAST in the combined PDF, to be torn off.
from common import *

CSS = """
.warn { border: 3px double #000; padding: 8px 12px; text-align: center; font-family: 'IM Fell DW Pica SC'; font-size: 13pt; letter-spacing: 0.1em; margin-bottom: 10px; }
table { border-collapse: collapse; width: 100%; font-size: 9.2pt; margin-bottom: 8px; }
th { text-align: left; font-family: 'IM Fell DW Pica SC'; font-size: 9pt; letter-spacing: 0.08em; border-bottom: 2px solid #000; padding: 3px 5px; }
td { border-bottom: 1px solid #999; padding: 3px 5px; vertical-align: top; }
td.n { font-family: 'Old Standard TT'; white-space: nowrap; width: 2.2em; }
td.loc { font-family: 'IM Fell DW Pica SC'; font-size: 9.5pt; }
h3 { font-family: 'IM Fell DW Pica SC'; font-size: 12pt; letter-spacing: 0.08em; margin: 10px 0 4px; border-bottom: 1px solid #000; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 0 18px; }
ul { margin: 0; padding-left: 16px; font-size: 9.4pt; }
li { margin-bottom: 3px; }
.key { font-family: 'Old Standard TT'; font-weight: 700; }
.mono { font-family: 'Old Standard TT'; letter-spacing: 0.08em; }
"""

STEPS = [
 ("0", "Handed to her: the letter and the Milk Crate painting", "The letter names sarahs.quest and ends 'breathe in, breathe out, and sit with it'"),
 ("A1", "Milk Crate painting, back: the famous man we always see here", "Ed Sheeran"),
 ("A2", "Stars and Their Notes, under Ed Sheeran", "The Barista's Hornpipe; the dotted half note, then the pair of beamed eighths"),
 ("A3", "Parlour Songbook, that air, those two shapes", "12 and 15"),
 ("A4", "Concordance, pages 12 and 15, with The Prophet", "CORN and BREAD"),
 ("A5", "Receipt Book, cornbread", "best eaten while playing a game of backgammon"),
 ("A6", "THE BACKGAMMON SET", "Plate II, the knife, the Patricia painting"),
 ("B1", "Register of Names, Patricia", "a small painted egg, of the sort kept in a box of birds"),
 ("B2", "THE WINGSPAN BOX", "the scale, the Hamlet painting, the fairy painting, a Queen of Hearts"),
 ("B3", "Cartomancer's Guide, Queen of Hearts", "at the back of the upstairs toilet"),
 ("B4", "THE TOILET CISTERN", "the BLACK key, in a ziplock"),
 ("B5", "Hamlet painting: the film of this play, by this director", "Hamnet, Chloé Zhao"),
 ("B6", "Register of Names, Chloe", "a young tree in a pot, and the soil beneath it"),
 ("B7", "THE BONSAI", "the blue-light pen"),
 ("B8", "Fairy painting: the family name of the one who lived here", "Shirley"),
 ("B9", "Register of Names, Shirley", "a bottle kept for company, among the other bottles"),
 ("B10", "THE LIQUOR CABINET", "the Pig-Pen Alphabet key sheet"),
 ("C1", "The knife on the scale", "79 g"),
 ("C2", "Knife Catalogue, No. 9", "The Lemonade Knife: cut lemons open"),
 ("C3", "The bowl of lemons, cut open", "the Joker"),
 ("C4", "Cartomancer's Guide, the Joker", "in the Dutch oven"),
 ("C5", "THE DUTCH OVEN", "Plate I, and the DARK BLUE key"),
 ("D1", "The suitcase, with the BLACK key", "the backpack, locked"),
 ("D2", "The backpack, with the DARK BLUE key", "the prize, and one locked compartment"),
 ("E1", "sarahs.quest, Abyssinia painting: Ethiopia, Plate VII, turned over", "HALF PAST THREE, in pigpen"),
 ("E2", "The flyer, the blue-light pen, the pigpen key: the bathroom wall under ALIEN BLUES", "BREATHE IN BREATHE OUT SIT WITH IT"),
 ("E3", "THE MEDITATION CUSHION", "the final card, in wheel symbols"),
 ("E4", "Plate I + Plate II pinned, set to 3:30, decode the card", "LOOK BEHIND THE FIRST PAINTING"),
 ("E5", "Behind the Milk Crate painting, the one she was handed first", "the PURPLE key"),
 ("E6", "The locked compartment, with the PURPLE key", "the sixth painting and the last card"),
]

PLACES = [
 ("Handed to her", "The welcome letter, the Milk Crate painting with the PURPLE key taped behind it"),
 ("Out in the open", "The nine printables, the flyer on the fridge, a bowl of lemons with one loaded, The Prophet among many books, the locked suitcase"),
 ("The backgammon set", "Plate II, the knife, the Patricia painting"),
 ("The Wingspan box", "The scale, the Hamlet painting, the fairy painting, a real Queen of Hearts"),
 ("The toilet cistern", "The BLACK key in a ziplock. Nothing else. No paper, no paintings."),
 ("The bonsai", "The blue-light pen"),
 ("The liquor cabinet", "The Pig-Pen Alphabet key sheet"),
 ("The Dutch oven", "Plate I with a brad taped to it, and the DARK BLUE key"),
 ("The bathroom wall", "ALIEN BLUES in dry-erase marker, pigpen in invisible ink beneath"),
 ("The meditation cushion", "The final card, written in wheel symbols"),
 ("Behind the Milk Crate painting", "The PURPLE key, taped flat under paper"),
 ("The suitcase", "The backpack"),
 ("The backpack", "The prize, plus a locked compartment holding the sixth painting and the last card"),
]

def build():
    rows = ''.join(f'<tr><td class="n">{n}</td><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for n, a, b in STEPS)
    prows = ''.join(f'<tr><td class="loc">{esc(a)}</td><td>{esc(b)}</td></tr>' for a, b in PLACES)
    body = f"""<div class="page">
<div class="warn">Game-master's sheet · remove these last two leaves before she arrives</div>
<h3>The chain, in order of dependency</h3>
<table><tr><th>#</th><th>She does</th><th>She gets</th></tr>{rows}</table>
<div class="foot">Game-master's sheet · 1 of 2</div>
</div>
<div class="page">
<h3>Every hiding place and what goes in it</h3>
<table><tr><th>Place</th><th>Contents</th></tr>{prows}</table>
<div class="two">
<div>
<h3>The four keys</h3>
<ul>
<li><span class="key">BLACK</span> opens the suitcase. Hidden in the toilet cistern, reached by the Queen of Hearts.</li>
<li><span class="key">DARK BLUE</span> opens the backpack. Hidden in the Dutch oven beside Plate I.</li>
<li><span class="key">PURPLE</span> opens the compartment inside the backpack. Taped behind the Milk Crate painting, the very first thing she was handed. The cipher wheel is what tells her.</li>
<li><span class="key">LIGHT BLUE</span> is not used. Keep it in your pocket.</li>
</ul>
<h3>Three branches, then the lock</h3>
<ul>
<li>Branch A, music, ends at the backgammon set with Plate II.</li>
<li>Branch B, names, ends with the pen, the pigpen sheet and the black key.</li>
<li>Branch C, the knife, ends at the Dutch oven with Plate I and the dark blue key.</li>
<li>The wheel needs Plate I, Plate II and the time. The time comes from the flags. So all three branches must finish.</li>
</ul>
</div>
<div>
<h3>The final card, in wheel symbols</h3>
<p class="mono" style="font-size:11pt">MFF6 DW5OY7 H5W LO8QH 9KOYHOYA</p>
<p style="font-size:9.4pt;font-style:italic">Reads: LOOK BEHIND THE FIRST PAINTING. Copy those symbols by hand onto a card and hide it under the meditation cushion.</p>
<h3>Before she arrives</h3>
<ul>
<li>Weigh the knife. It must read 79 g. The nearest entries are 58 g and 99 g.</li>
<li>Check pages 12 and 15 of your copy of The Prophet against the concordance.</li>
<li>Test the blue-light pen on the wall, and that it wipes off.</li>
<li>Cut one spare lemon to be sure the joker survives.</li>
<li>Assemble the wheel at 3:30 and decode the card yourself.</li>
</ul>
</div>
</div>
<div class="foot">Game-master's sheet · 2 of 2 · the cipher solution follows, remove that too</div>
</div>"""
    write_page('10-mapping-GAMEMASTER-remove', body, "Game-master's mapping sheet", CSS)

if __name__ == '__main__':
    build()

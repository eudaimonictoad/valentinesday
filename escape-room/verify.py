# Triple-check the whole clue graph: python3 escape-room/verify.py  (run from escape-room/)
# Every check below is a link in the chain or a way the chain could break.
import json, re, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, 'src')
H = lambda n: open(f'html/{n}.html').read()
ok, bad = [], []
def chk(label, cond, detail=''):
    (ok if cond else bad).append(label + (f"  [{detail}]" if detail else ''))

stars = H('04-stars-and-their-notes'); seg = stars[stars.index('Ed Sheeran'):][:420]
chk("A2 Ed Sheeran -> Barista's Hornpipe", 'Barista' in seg)
chk("A2 Ed's two notes named", 'dotted half note, then the pair of beamed eighth notes' in seg)
song = json.load(open('src/songbook_data.json'))
ed = next(s for s in song if 'Barista' in s['title'])
chk("A3 dotted_half = 12", ed['numbering']['dotted_half'] == 12, ed['numbering']['dotted_half'])
chk("A3 eighth_pair = 15", ed['numbering']['eighth_pair'] == 15, ed['numbering']['eighth_pair'])
dupes = [s['title'] for s in song if s['title'] != ed['title']
         and s['numbering'].get('dotted_half') == 12 and s['numbering'].get('eighth_pair') == 15]
chk("A3 no other air gives the same 12/15 pair", not dupes, dupes)
con = H('08-prophet-concordance')
chk("A4 page 12 rule present", 'the fourth word of the first line' in con)
chk("A4 page 15 rule present", 'the sixth word of the first sentence on the page that begins with' in con)
rec = H('05-household-receipt-book')
chk("A5 exactly one backgammon", rec.count('backgammon') == 1, rec.count('backgammon'))
chk("A5 backgammon is on cornbread", 'Cornbread' in rec[:rec.index('backgammon')][-1400:])

reg = H('06-register-of-names')
def keep(name):
    m = re.search(re.escape(name) + r'</span> <span class="o">[^<]*</span> [^<]*<span class="k">Keepsake: ([^.]*)', reg)
    return m.group(1) if m else None
chk("B1 Patricia -> painted egg (Wingspan)", 'painted egg' in (keep('Patricia') or ''), keep('Patricia'))
chk("B6 Chloe -> a jar of sweets (the candy jar)", 'jar of sweets' in (keep('Chloe') or ''), keep('Chloe'))
chk("B9 Shirley -> a bottle (liquor cabinet)", 'bottle kept for company' in (keep('Shirley') or ''), keep('Shirley'))
chk("Sarah has her own entry with a real keepsake", 'Sushi' in (keep('Sarah') or ''), keep('Sarah'))
chk("no Sally to be confused with Sarah", '>Sally<' not in reg and 'Sally</span>' not in reg)
for nm in ('Patricia', 'Chloe', 'Shirley'):
    chk(f"{nm}'s keepsake is unique in the register", reg.count(keep(nm)) == 1)

cards = H('07-cartomancers-pocket-guide')
chk("C4 Coloured Joker -> Dutch oven", 'The Coloured Joker</b>' in cards and 'fortune is sought <i>in the Dutch oven' in cards)
chk("Joker is set like the other suits, not boxed", 'class="joker"' not in cards)
chk("B3 Queen of Hearts -> toilet cistern",
    'Queen of Hearts</b> — a kind and loyal woman; its fortune is sought <i>at the back of the upstairs toilet' in cards)
fortunes = re.findall(r'fortune is sought <i>([^<]*)', cards)
chk("52 cards + two jokers have fortunes", len(fortunes) == 54, len(fortunes))
chk("all fortunes distinct", len(set(fortunes)) == len(fortunes))
REAL = ['backgammon', 'wingspan', 'liquor', 'meditation', 'cushion', 'suitcase', 'backpack', 'sweets', 'candy', 'frame', 'picture', 'photo', 'puzzle', 'jigsaw']
chk("no card fortune points at a real hiding place", not [f for f in fortunes if any(w in f.lower() for w in REAL)])
chk("toilet and Dutch oven appear exactly once each",
    len([f for f in fortunes if 'toilet' in f.lower() or 'dutch oven' in f.lower()]) == 2)
pairings = re.findall(r'<div class="p">([^<]*)', rec)
chk("no recipe pairing points at a real hiding place",
    not [p for p in pairings if any(w in p.lower() for w in ['wingspan', 'liquor', 'dutch oven', 'toilet', 'cistern', 'meditation', 'candy jar', 'suitcase', 'backpack', 'jigsaw', 'puzzle', 'picture', 'frame', 'photo'])])

kn = H('01-knife-catalogue')
import content_knives as CK
chk("C1 exactly one 79 g knife", kn.count('Weight 79 g') == 1)
chk("no other knife within 15 g of 79", not [(n, w) for n, o, w, d, p in CK.KNIVES if w != 79 and abs(w - 79) < 15])
chk("C2 the 79 g knife is the lemon one", 'lemon' in next(d for n, o, w, d, p in CK.KNIVES if w == 79).lower())

import cipher_data as C
msg = 'BEHIND THE MANY FACES'
chk("E4 final card round-trips", C.decode(C.encode(msg)) == msg, C.encode(msg))
sol = H('02-cipher-wheel-SOLUTION-gamemaster-only')
chk("E4 wheel time is 3:30", 'read <b>3:30</b>' in sol)
chk("E4 rotation is 200 degrees", 'turned 200°' in sol)
chk("solution sheet is clearly marked", 'game-master only' in sol.lower())

# ---- the wall tracing sheet matches the plan, and only seven sheets lie in the open ----
wall = open('html/pigpen-message.html').read()
chk("wall sheet reads the current wall line", 'BREATHE IN BREATHE OUT OPEN THE GREEN THING YOU SIT ON' in wall)
chk("wall sheet shows the marker words in plain type", '>open<' in wall and '>thing<' in wall)
gm0 = open('html/10-mapping-GAMEMASTER-remove.html').read()
chk("guide says seven sheets in the open, not nine", 'nine printables' not in gm0 and 'seven printed sheets' in gm0.lower() or 'Seven printed sheets' in gm0)

# ---- all six paintings: each is placed, each has a written clue, none duplicated ----
gm = open('html/10-mapping-GAMEMASTER-remove.html').read()
PAINTINGS = ['Milk Crate', 'Patricia', 'Hamlet', 'Fairy houses', 'Abyssinia', 'Gleaners']
for name in PAINTINGS:
    chk(f"painting '{name}' has a written clue on the guide", name in gm, name)
chk("no phantom seventh painting in the backpack", 'sixth painting' not in gm)
chk("all six paintings placed in the set-up order", 'Place all six paintings' in gm)

fl = open('flags.html').read()
chk("E1 Ethiopia figure gives half the time", "'HALF PAST'" in fl)
chk("E1 Italy figure gives the other half", "msg: 'THREE'" in fl)
chk("E1 both flag paintings are load-bearing", "'HALF PAST'" in fl and "msg: 'THREE'" in fl)
chk("E1 flags carry no country names", 'Ethiopia<' not in fl and '>Italy<' not in fl)
chk("E1 no flag duplicates a route", 'TUCK AND DRAW' not in fl)
chk("E1 flag cards are Figures, not Plates", 'Plate ${ROMAN' not in fl and '>Plate <' not in fl)

# ---- F: the framer's delivery card, and the two painting spots it names ----
cfg = json.load(open('src/config.json'))
fr = H('13-framers-delivery-card')
ab, gl = cfg['abyssinia_location'], cfg['gleaners_location']
chk("F1 framer's card names the Abyssinia spot", ab in fr, ab)
chk("F1 framer's card names the Gleaners spot", gl in fr, gl)
chk("F2 the two painting spots are different places", ab != gl)
chk("F3 card leaks neither painting's subject",
    not [w for w in ('Abyssinia', 'Ethiop', 'Ital', 'Glean', 'Africa', 'harvest', 'market') if w in fr],
    [w for w in ('Abyssinia', 'Ethiop', 'Ital', 'Glean', 'Africa', 'harvest', 'market') if w in fr])
chk("F4 no painting goes anywhere near water", not [w for w in ('toilet', 'cistern', 'bath', 'sink', 'shower', 'kettle') if w in (ab + ' ' + gl).lower()])
from build_cards import PLACES as CARDPLACES
def core(p):
    for pre in ('nestled in the ', 'inside the ', 'inside a ', 'beneath the ', 'behind the ',
                'under the ', 'in the ', 'on the ', 'at the ', 'in a ', 'under a '):
        if p.startswith(pre): return p[len(pre):]
    return p
hits = [p for p in CARDPLACES if core(p) and core(p) in (ab + ' | ' + gl)]
chk("F5 neither painting spot collides with a card fortune", not hits, hits)
chk("F6 candy jar no longer holds the paintings",
    'Abyssinia painting' not in gm.split('The candy jar')[1].split('</tr>')[0] if 'The candy jar' in gm else False)
chk("F7 guide's candy-jar row names the framer's card", "framer's delivery card" in gm)
chk("F8 guide's tear-off count matches the real game-master section",
    'eight</b> leaves' in gm and 'last six leaves' not in gm and 'seven</b> leaves' not in gm)
chk("F9 set-up order places the pen and card in the jar", 'into the candy jar' in gm)

chk("F10 no reprint cover hard-codes a painting location",
    not [f for f in ('reprint-cover-catchup', 'reprint-cover-paintings')
         if os.path.exists(f'html/{f}.html') and (ab in H(f) or gl in H(f))],
    [f for f in ('reprint-cover-catchup', 'reprint-cover-paintings')
     if os.path.exists(f'html/{f}.html') and (ab in H(f) or gl in H(f))])

from content_clues import CLUES
backs = H('14-painting-back-clues')
chk("G1 all six painting clues are printed on cards", all(t in backs for _, t in CLUES),
    [l for l, t in CLUES if t not in backs])
chk("G1 the guide points at the cards instead of repeating them",
    'The Six Painting Backs' in gm and not [t for _, t in CLUES if t in gm])
chk("G2 each painting name sits outside its frame, to be trimmed",
    backs.count('this row is trimmed off') == 6, backs.count('this row is trimmed off'))
chk("G3 the clue cards do not name a hiding place",
    not [w for w in ('cupboard', 'candy jar', 'cistern', 'Dutch oven', 'backgammon', 'Wingspan') if w in backs])


print('\n'.join('PASS  ' + s for s in ok))
if bad: print('\n' + '\n'.join('FAIL  ' + s for s in bad))
print(f"\n{len(ok)} passed, {len(bad)} failed")
sys.exit(1 if bad else 0)

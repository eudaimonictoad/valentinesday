import json
from common import *

SUITS = [('Hearts', '♥', 'matters of the heart'), ('Diamonds', '♦', 'matters of money and the house'), ('Clubs', '♣', 'matters of work and friendship'), ('Spades', '♠', 'matters of trouble and change')]
RANKS = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
MEANINGS = {
 'Hearts': ['a new love, or an old one returning', 'a meeting of two minds', 'a letter that pleases', 'a change of dwelling', 'a gift given freely', 'a surprise visit', 'a broken promise, mended', 'an invitation', 'a wish granted', 'the family gathered', 'a warm-hearted friend', 'a kind and loyal woman', 'a generous man'],
 'Diamonds': ['a ring, or an important document', 'a small quarrel over a small sum', 'a legal matter', 'an inheritance', 'a prosperous venture', 'an early marriage', 'a loss, soon recovered', 'a journey by land', 'a restless night', 'money from an unexpected quarter', 'a messenger with news', 'a woman fond of gossip', 'a man of business'],
 'Clubs': ['wealth and good fortune', 'an opposition overcome', 'a happy marriage', 'a change for the worse, then better', 'help from a friend', 'a business success', 'a secret admirer', 'a run of good luck at games', 'a new friendship', 'a long journey', 'a dark-haired young man', 'a woman of quick temper', 'a faithful friend'],
 'Spades': ['a misfortune, or a great decision', 'a deception', 'a parting', 'illness, briefly', 'a difficulty at home', 'a change of heart', 'a loss of a friend', 'a caution against haste', 'the worst card, and then it passes', 'a night of worry', 'an untrustworthy young man', 'a widow, or a woman alone', 'an ambitious man'],
}
PLACES = ['in the cutlery drawer', 'beneath the doormat', 'behind the clock', 'in a coat pocket', 'under the bed', 'in the breadbox', 'in the coffee grinder', 'in the fruit bowl', 'inside a shoe', 'under the bathmat', 'on the highest shelf',
          # index 11 = the Queen of Hearts. This one is real: a Queen of Hearts is planted for her to find.
          'at the back of the upstairs toilet, where a noble woman does not look twice',
          'in the toaster oven', 'in the letterbox', 'behind the curtains', 'in the umbrella stand', 'inside a book of poems', 'in the medicine cabinet', 'in the vegetable drawer', 'under the kettle', 'in the sewing box', 'behind the mirror', 'in the laundry basket', 'in the spice drawer', 'beneath the rug', 'in the fridge door', 'under the sink', 'in the sugar jar', 'in the bag of rice', 'behind the radiator', 'in the toolbox', 'under the stairs', 'in the bath', 'on the windowsill', 'in the sock drawer', 'nestled in the mixing bowls', 'in the hall closet', 'in the recycling', 'at the bottom of the wardrobe', 'in the tea caddy', 'under the lamp', 'in the bicycle basket', 'inside the chess set', 'behind the books', 'in the freezer', 'in the desk drawer', 'under the cutting board', 'under the television', 'in the dishwasher', 'in a tub of protein powder', 'in the salt cellar', 'inside the Coup box']
assert len(PLACES) >= 52

CSS = """
.suit { margin-bottom: 8px; }
.suit h3 { font-family: 'IM Fell DW Pica SC'; font-size: 13pt; letter-spacing: 0.08em; border-bottom: 1px solid #000; margin-bottom: 3px; }
.suit h3 span { font-family: 'DejaVu Sans'; font-size: 12pt; }
.c { font-size: 9.3pt; line-height: 1.25; margin-bottom: 2px; }
.c b { font-family: 'IM Fell English SC'; font-weight: normal; font-size: 10pt; }
.c i { }
.joker { border: 2px solid #000; padding: 6px 10px; margin-top: 8px; font-size: 10pt; text-align: center; }
.joker b { font-family: 'IM Fell DW Pica SC'; font-size: 12pt; letter-spacing: 0.08em; }
.preface { font-size: 10.5pt; text-align: justify; margin: 6px 0 8px; }
"""

def build():
    cfg = json.load(open(os.path.join(ROOT, 'src', 'config.json')))
    blocks = []
    p = 0
    for suit, sym, theme in SUITS:
        rows = ''
        for rank, meaning in zip(RANKS, MEANINGS[suit]):
            rows += f'<div class="c"><b>{rank} of {suit}</b> — {meaning}; its fortune is sought <i>{PLACES[p]}</i>.</div>'
            p += 1
        blocks.append(f'<div class="suit"><h3><span>{sym}</span> {suit} <span class="small" style="font-family:\'IM Fell English\';font-style:italic;letter-spacing:0;text-transform:none">— {theme}</span></h3>{rows}</div>')
    # the two Jokers, set as a fifth suit so they do not stand out
    jrows = (f'<div class="c"><b>The Coloured Joker</b> — the fool who knows everything and says nothing; its fortune is sought <i>{esc(cfg["joker_location"])}</i>.</div>'
             f'<div class="c"><b>The Black Joker</b> — the fool who says everything and knows nothing; its fortune is sought <i>inside a rolled-up yoga mat</i>.</div>')
    blocks.append(f'<div class="suit"><h3><span>✦</span> Jokers <span class="small" style="font-family:\'IM Fell English\';font-style:italic;letter-spacing:0;text-transform:none">— matters that fit nowhere else</span></h3>{jrows}</div>')
    body = f"""<div class="page">
{masthead("The Cartomancer's Pocket Guide", 'The Meaning of every Card, and where its Fortune is to be Sought', 'As practised in the Kitchens of Europe · Sixth Printing')}
<p class="preface">Draw a card, or be given one, or find one where no card ought to be. Read its meaning below, and then, if you are brave, go and look for its fortune in the place appointed. The places are traditional and have not been altered in six printings. The cards do not care whether you believe them.</p>
<div class="cols2">{''.join(blocks)}</div>
<div class="foot">The Cartomancer's Pocket Guide</div>
</div>"""
    write_page('07-cartomancers-pocket-guide', body, "The Cartomancer's Pocket Guide", CSS)

if __name__ == '__main__':
    build()

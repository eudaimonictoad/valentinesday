import random, json
from common import *
from music import TYPES
from build_songbook import ED_SONG, ED_NOTES

CELEBS = [
 ("Taylor Swift", "I write the bridge first and the rest of the song is just an excuse for it."),
 ("Harry Styles", "A note is only as good as the trousers you play it in."),
 ("Beyoncé", "Every rest is a choice."),
 ("Dolly Parton", "A rest is just a note that's thinking."),
 ("Elton John", "I have a piano in every room and a favourite note in every piano."),
 ("Billie Eilish", "Quiet notes are louder."),
 ("Adele", "If it doesn't make somebody cry, add a dot to it."),
 ("Bruno Mars", "Play it twice, and the second time wear a hat."),
 ("Lady Gaga", "I was born with this note."),
 ("Rihanna", "I don't play the notes. The notes play me, and they pay for the privilege."),
 ("Hozier", "There is a church somewhere that owes me this note."),
 ("Olivia Rodrigo", "This is the note I'd play at my ex's wedding."),
 ("Stevie Wonder", "You can hear a smile in a triplet."),
 ("Sabrina Carpenter", "Short, sweet, and it leaves before you're ready."),
 ("Paul McCartney", "John never liked this one, which is why I play it."),
 ("Chappell Roan", "Loud, pink, and in the wrong key on purpose."),
 ("Bad Bunny", "Any note is a dance note if you commit."),
 ("Phoebe Bridgers", "It's the sad one. Obviously it's the sad one."),
 ("Keanu Reeves", "I don't play. I listen. This one's nice."),
 ("Lizzo", "I play this on the flute while doing something else entirely."),
 ("Shakira", "The notes don't lie."),
 ("Zendaya", "I was told to pick one, so I picked two."),
 ("Céline Dion", "I hold this note until the room agrees with me."),
 ("Bruce Springsteen", "Four bars of this and the whole county shows up."),
 ("Kacey Musgraves", "Slow it down and it turns into a porch."),
 ("Ed Sheeran", "I could play this one in any coffee shop in the world, and I have."),
 ("Noah Kahan", "It's the sound of leaving Vermont and coming straight back."),
 ("Tom Hanks", "I don't know what it's called, but I like the look of it."),
 ("Doja Cat", "I don't have a favourite note. Fine. Two."),
 ("Charli XCX", "Fast. Faster than that."),
 ("Pedro Pascal", "I would protect this note with my life."),
 ("Mitski", "It's a rest. Let it rest."),
]

CSS = """
.intro { font-style: italic; text-align: center; font-size: 10.5pt; margin: 6px 0 10px; }
.celeb { break-inside: avoid; margin-bottom: 8px; font-size: 10pt; }
.celeb .who { font-family: 'IM Fell DW Pica SC'; font-size: 12pt; letter-spacing: 0.04em; border-bottom: 1px dotted #000; }
.celeb .q { font-style: italic; }
.celeb .fav { margin-top: 1px; }
"""

def build():
    rng = random.Random(77)
    songs = json.load(open(os.path.join(ROOT, 'src', 'songbook_data.json')))
    entries = []
    for name, quip in CELEBS:
        if name == 'Ed Sheeran':
            title = ED_SONG; notes = [t for t, _ in ED_NOTES]
        else:
            song = rng.choice(songs); title = song['title']
            notes = rng.sample(sorted(song['numbering']), 2)
        n1, n2 = (TYPES[t][0] for t in notes)
        entries.append(f"""<div class="celeb"><div class="who">{esc(name)}</div>
<div class="q">“{esc(quip)}”</div>
<div class="fav">Favourite air: <b>{esc(title)}</b>.<br>Favourite notes: {esc(n1)}, then {esc(n2)}.</div></div>""")
    body = f"""<div class="page">
{masthead('The Stars &amp; Their Notes', 'A Musical Miscellany · From the pages of The Parlour Gazette')}
<p class="intro">We wrote to thirty-two celebrated persons and asked each of them two impertinent questions: which air from <i>The Parlour Songbook</i> they play most often, and which two note shapes in it they hold dearest. To our astonishment, all thirty-two replied. Their answers are printed below without correction.</p>
<div class="cols2">{''.join(entries)}</div>
<div class="foot">The Parlour Gazette · Musical Miscellany</div>
</div>"""
    write_page('04-stars-and-their-notes', body, 'The Stars and Their Notes', CSS)

if __name__ == '__main__':
    build()

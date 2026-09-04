# HANDOFF — Sarah's escape room (the Six Paintings)

**Read this whole file before touching anything.** It is written for a fresh Claude Code session on Ben's local machine. It contains the situation, Ben's own words verbatim, the exact state of every file, what is verified true, what is still undecided, and what to build next.

Ben's email: benjaminyao2k@gmail.com. Repo: `eudaimonictoad/valentinesday`. Branch: `claude/escape-room-printables-irmpol`.

---

## 0. The one-paragraph situation

Ben is building a physical escape room in his apartment for his girlfriend **Sarah** (she does not live there — never write "Sarah's kitchen" or "Sarah's liquor cabinet" in any prop). It is built around **six mini line-and-wash paintings he made himself**, each of which carries a clue. The props are fake vintage documents in a shared "Pocket Library" house style: a knife catalogue, a songbook, a celebrity list, a recipe book, a register of girls' names, a cartomancer's guide, a concordance to *The Prophet*, a pigpen key, and a two-plate rotating cipher wheel. Nine PDFs are built and verified. **Nothing has been printed yet.** Two sheets need a content change before printing. The remote session that built all this had its shell and its GitHub writes blocked partway through, so the last few source edits were never committed.

---

## 1. Ben's words, verbatim

Kept raw on purpose. This is the tone, the constraints, and the ideas in his voice. Do not sand this down.

### 1.1 The original brief

> "So I could use some help. Um, today is my last day to do this. Um, I need to build out stuff. So I'm doing a... basically, I'm making a escape room for my girlfriend, Sarah. the part of it is gonna be six mini paintings, line and wash paintings that I made. Um, it's just gonna be an escape room in my apartment, basically. So there's gonna be different elements. Like, I don't know, cutting a lemon open, finding a card in there, finding a joker in there."

> "all of them are copy shop slash restaurant things"

> "One of the components is a rotational cypher. Like, I was thinking of sort of like a Caesar cypher sort of situation, except both sets of things are randomized. And it's calibrated because the inside has two hands, and the outside has, like, numbers, not only letters, but also numbers like a clock. And then she'll have to unlock each component. So it'd be, like, two components, and then also the time so that she knows, yeah, how how the clock is oriented. And then let's say the answer is, like, I don't know, two thirty or something like that. Let's do let's do three thirty. That feels good to me."

> "there also needs to be, like, a database or not a database, but, like, some sort of mapping, something that maps a bunch of girls names, like a ton because we went to Patricia's Coffee Brewers in Melbourne, and that's one of the images that I made. And then another one is ham... Hamlet. We watched Shakespeare in the Park. So the clue on the back of that is gonna be we watched a movie associated with this play by this director or something like that. And the director, I think of that was Chloe Zhao."

> "it'd be helpful, like, you could help me with a lot of the stuff by just coming up with a ton of girls names or something like that. And, you know, it won't hurt to print some stuff."

### 1.2 The knife catalogue

> "Another one is I wanna make, like, a knife catalog, like a fake knife catalog, and one of them, just like an old timey font one without pictures of the knives, but just with tons of different knives. And one of the clues is gonna be a knife and a scale, so she's gonna have to weigh the knife in grams."

> "I think one of those weights should be seventy nine grams. Um, obviously, you don't get anything super close to that amount of grams just in case the weight amount changes."

> "don't do the inches just so it's not confusing"

> "don't be too descriptive of the knife, like, of the actual physical appearance knife. You could be like, this knife was Japanese crafted or something like that"

> "one of them should be great for making lemonade and, uh, great for making lemonade and cutting lemons open or something like that"

> "each thing should be, like, a little bit like, feel intentional or, like, interesting... cutting sandwiches in half, uh, pruning basil leaves, um, cutting off the heads of flowers, um, some ridiculous stuff, like cutting open seat cushions, cutting open mattresses, cutting open, um, I don't know, throwing at the ceiling, um, juggling, um, for prying certain locks open, um... just like stuff that would send her on a wild goose chase if she did every single one."

> "One must be gifted to... this one is a great gift to A mother, this is a great gift to text to your father."

> "just come with, like, literally a million, like, red herrings almost except for that one. I think you could probably have, like, twenty five knives on that page."

### 1.3 The sheet music and the celebrities

> "I could use, like, um, I don't know if you're able to create this. I don't know if you're strong enough to create this, but some, like, sheet music, basically. But it's, like, really fake sheet music. Obviously, it doesn't have to be real music, but, basically, each type of note. So, like, note meaning, like, three quarter notes in a row or one and a half note or four eighth notes or whatever. So each thing on a bunch of sheets of music, there'll be, like, I don't know, whatever x amount of notes, but they're all gonna be unique or whatever. A lot of them are gonna be unique, and then each unique note for a given song is gonna be is gonna be tagged with a number."

> "maybe you could just come up with, like, ten pages of fake sheet music or something like that or, like, ten pages of twenty songs or whatever it is."

> "one is gonna be, like, a list of pop stars and celebrities. Maybe you can make that sort of in theme with some of this music stuff... because Milk Creek coffee shop, that's where we like going. There's a barista that looks like Ed Sheeran... I want you to create a list of, I don't know, like, thirty or so celebrities"

> "you could maybe do, like, a page that's just, like, each celebrity's favorite notes"

### 1.4 The Prophet and the recipe book

> "those notes have to be able to be mapped at least on one of the sheet musics to to say the numbers in the page of a book that I have, the profit, where she's gonna use a templated page key thing and overlay it. to know which word I'm talking about."

> "on page twelve of the profit, there is corn... on page fifteen, there's a word that's bread bread as in, like, baking bread. And those two things will yield cornbread"

Later he refined this and dropped the overlay template:

> "the other thing I realized is that we can really just do which word... the 4th word on the 12th page is corn. and the 7th word on the 8th line from the top is bread. on the twelth page. i guess maybe we can do the 12th page is corn 4 words from the top on the firstl ine basically. andu. know what just to make it more fun we can do the 15th page, eh tis really far down and the lines are sort of mis defined maybe ui can jsut givye ou thel ine its in , give one another of your bread but eat not from the same loaf is 15"

> "on the 12th page it says lke esheaves of corn he gather you unto himself he threshes you to make you naked he sifts you free from your husks he grind you to whiteness he knead you until you are pliant and then he asisgns yo uto his sacred fire t, that you maybe become sacred bread for gods sacred feast."

> "idk instead of cutting a template maybe ill just have something that just says those clues or something like that so maybe u just give hte pages or something like that"

On the recipes:

> "you'll just have a bunch of, like, a recipe book almost, like a fake recipe book. And on the cornbread one, it will say, um... cornbread is best eaten with while playing a game of backgammon."

> "the rest of the recipes, they can look fairly normal, but they'll also be paired with, like, also, like, red herrings so that she can't just, like, brute force this. So you could actually have... because you're an LLM, this doesn't cost you much to create. Maybe you should do more volume than... like, they don't they don't have to be, like, really in-depth recipes."

> "you could say one that's best played with guitar, um, uh, sweeping window sills, Looking under the couch covers while playing the piano, soft drawer, going on important gene editing databases because she's a geneticist. In dishwashers, you could do, like, a bunch of, like, household things under the stair railing in light bulbs, in laundry machines, in linen closets on the top shelf of knickknack walls, in lamps, in the dirt of plants"

**Sarah is a geneticist.** That is why the gene-editing database line exists.

### 1.5 The toilet

> "one thing I want to hide in... I wanna hide in the back of the upstairs toilet. So if you can say something cheeky of that... cheeky about that, I think I'm gonna hide one clue there."

Later, critically:

> "make sure none of the paintins are in the toilet i cant risk that geting wet but a key can lo l"

### 1.6 On red herrings, difficulty, and structure — this is the important one

> "i had another claud esession but it was achat not a claude code session i was trying to figureo ut like -- what to do, in temrs of like i want this to be fun-- not feel like homework, i ve hepeopel actualyl hate redherrings so ive been trying to avoi like complete bs red herrings. , when i say redherring shere ive been meanign like its there but iu just have to sift through it, its part of the game not just complete bs on the wall u know idk. but i odnt want it to be too easy, or take too short or take too long either u knwo what i mean?"

> "im also having trouble like -- theo ther chat told me and u can lmk if this is true or not it can be ocmpeltely linear, so im trying ot make it like more of a tree / like have something s that fork off, maybe cend up paused / cant move forward wihtout somethign else, or somethignl ike that? or maybe have two lines of something that converge but the intermediary stepps require each other?"

> "my rough coloring on that spreadsheet is just for me to remember what is dpenedent on what, but i dont care what is available right away / what is given when"

> "i guess whati m saying is jsut to be dramatic i want to hand her one thing right way( other stuff might be places around the room, or slightly hidden or smoething liek that, but idk."

> "part of the magic as u said earlier was like, oh giving something to someone that they dont use until later so like maybe i give her the cypher stuff early or the flag stuff she migth figure out early, but have to look at the pig pen cyphers for a long time u now aht i mean?"

> "there should be some 'half clues' that arent super improtant to drag on but arei mprotant clues maybe?"

**The design rule that came out of this:** the sifting happens *inside the documents*, never in the apartment. Every printable has one true entry among many (one knife of 27, one recipe of 74, one name of 276), but she always arrives at a document already holding the key that picks out its entry. No hiding place in the apartment is ever empty. That is the distinction he was drawing.

### 1.7 Alien Blues / Vundabar / the bathroom

> "the blue light pen was gonna shine on 'ALIEN BLUES' i was gonna expo marker alien blues, the underneath that, have some invisible ink pig pen cyphers under neath so it looks like 'alien language' -- so she needs to discover hte pig pen cypher before then and the blue light pen by then i was thinking?"

> "maybe somewhere we can make a flyer htat says vundabar, playing alien blues in the bathroom! check it out! dont include a time so its not confusing or osmething liek that but maybe incldue liek a tour dates or something liek that idk"

> "the fluyers bathroom line doesnt matter its just an extra accessory / nudge in case she doesnt find it in the bathroom"

### 1.8 Locations he offered

Real, confirmed his:
> "in the toaster oven, we have a spice drawer, dishwasher, a pint of creatine, , nestled in mixing bowls, under the cutting board, we have hteb oard games wingspan, coup , chess,"

> "bag of rice is a good fake hiding place too btw"

> "we also hav eali quor cabinet if u need something random"

> "under the bonsai tree is a good fake clue"

> "i told u one of the actual destinations should be the backgammon set, i think thats a good idea"

> "i think the wingspan board could be an interesting location for a key too or somethign like that, u can say something like tuck and draw or osmething liek that"

> "i have 5 sets of keeys too, btw and i can nest a backpack within a suit case, or something liek that u know what i mean? i can nest stuff too."

> "instead of location hints sometimes they could be keys u know haha"

> "if nwe need to connect anything - it can be the hidden location of something i also have like some simple keys i was gonna lock compartments to my backpack"

### 1.9 The meditation cushion

> "a real clue for something can be breathe in, breathe out, for my meditation cushion do u feel liek thats too weak?"

Answer given: not too weak **as a payoff** she decodes, rather than a riddle she has to interpret cold. So the pigpen on the bathroom wall decodes to BREATHE IN BREATHE OUT SIT WITH IT, and "sit" does the pointing.

### 1.10 The sixth painting (the fairy houses)

> "OHHHH theres noather one i totally forgot. the sixth painting is of these fairy houses we used to put messages into it, and the faires name was cardelia shirley or something liek that, the last name was shirley, so i was gonna create a clue with shirley or something like that"

> "the back of hte painting her last name was shirley thats all u need to know, ill come up with the vlue ill figure out what the back of the paintins will say or u can just say what is the last name of the inhabitant of these fairy houseso rsomething liek that?"

Both **Cordelia** and **Shirley** are already in the register, so either name works as the lookup.

### 1.11 The flags idea (currently parked)

> "maybe u can just make the flag thing and i can just regive her the url, make sure its mobile compatible and maybe just put idk 20 or so flags and u flip em over theres like pig pen cypehrs that lead to some thing else?"

> "dont give the actual names of the countries, thats suppseod to be the hard part, she can look it up and shit, andm ix up ethiopia and italy i nthere, and also make the theme more on point with what our theme is now. not the old sarahs game thing -- keep the sarah game files u know dont like dlete those just redirect to htis new thing for now."

Then, later:

> "forget the flag thing for now"

**So the flags are PARKED, not cancelled.** The file exists and works (see §3.4). The two flag paintings are Abyssinia (Ethiopia) and Gleaners Cafe (in the Italian Market, so Italy).

Site URL he gave: **sarahs.quest**

### 1.12 The frames

> "maybe u can just come up with like quarter sheets like frames and ill write the clues in the middle hows htat? so it looks fine. gimem 2 pages of those frames btw"

Done. See §3.3.

### 1.13 Where he is emotionally, and the last instructions

> "idk i just dont even know what to do anymore. its getting late i dont have enough time. i think maybe like no the freezer can be a fake thing maybe ill put a key in idek im out of good dieas man im out of good ideas ."

> "is one of the malready in the toilet? make sure none of the paintins are in the toilet i cant risk that geting wet but a key can lo l"

Then, the final build instruction, which is **the top of the to-do list**:

> "no i havent printed nantyhign yet, change up the pdf and make itp rintbable. yeah use the dutch oven for someting i think thats a good idea since i cant figureo ut ap lace to put stuff. the tin of fcoffee is wrong and i odnt wnna do the pillwo case iether . incorproate wingspan backgmmon the other stuff etc"

**He is tired and out of runway. Do not present him with more open questions than necessary. Make the safe call, tell him what you picked in one line, and hand him printable files.**

---

## 2. What exists right now, exactly

Repo root: `/home/user/valentinesday` (remote) — on his machine, wherever his clone is.
Everything lives in `escape-room/`.

```
escape-room/
  README.md          game-master notes, one table of what each printable hides
  HANDOFF.md         this file
  render.js          HTML -> PDF via Playwright/Chromium
  preview.py         PDF -> PNG, for eyeballing a page
  fonts/             10 Google Fonts as .woff2 + fonts.css + get-fonts.sh
  html/              generated HTML, one file per printable + style.css
  pdf/               generated PDFs (the deliverables)
  src/               Python generators + content files + config.json
```

### 2.1 The ten PDFs

| File | Pages | What it is |
|---|---|---|
| `01-knife-catalogue.pdf` | 2 | Hawthorne & Daughters, 27 knives with gram weights |
| `02-cipher-wheel.pdf` | 2 | Plate I (dial) and Plate II (hands) to cut out and pin |
| `02-cipher-wheel-SOLUTION-gamemaster-only.pdf` | 1 | **Never print for Sarah.** Assembled wheel + full mapping table |
| `03-parlour-songbook.pdf` | 11 | Key to 26 note shapes + 20 fake airs, every note numbered |
| `04-stars-and-their-notes.pdf` | 2 | 32 celebrities, each with a favourite air and two notes |
| `05-household-receipt-book.pdf` | 4 | 74 short recipes, each with a "best eaten while…" pairing |
| `06-register-of-names.pdf` | 4 | 276 girls' names: origin, meaning, and a keepsake object |
| `07-cartomancers-pocket-guide.pdf` | 2 | All 52 cards + the Joker, each with "where its fortune is sought" |
| `08-prophet-concordance.pdf` | 1 | One word-counting rule for each of 84 pages of *The Prophet* |
| `09-pigpen-key.pdf` | 1 | The pigpen alphabet, four pens, plus a practice line |

### 2.2 The generators

| File | Builds | Notes |
|---|---|---|
| `src/build_knives.py` | 01 | content in `src/content_knives.py`, asserts exactly one 79 g knife and everything else ≥15 g away |
| `src/build_cipher.py` | 02 + solution | geometry; reads `src/cipher_data.py` |
| `src/cipher_data.py` | — | the cipher itself; also a CLI encoder (see §4) |
| `src/build_songbook.py` | 03 | draws staves via `src/music.py`; writes `src/songbook_data.json` |
| `src/music.py` | — | 26 note-shape drawers, staff/clef/barline helpers |
| `src/build_celebs.py` | 04 | reads `songbook_data.json` so the numbers always agree |
| `src/build_recipes.py` | 05 | content in `src/content_recipes.py` |
| `src/build_names.py` | 06 | content in `src/content_names.py`, keepsakes from `src/config.json` |
| `src/build_cards.py` | 07 | Joker location from `src/config.json` |
| `src/build_concordance.py` | 08 | the two real rules are in a `REAL` dict at the top |
| `src/build_pigpen.py` | 09 | also `python3 build_pigpen.py "MESSAGE"` to draw a message in glyphs |
| `src/build_all.py` | everything | runs all builders then `render.js` |

### 2.3 How to rebuild

```bash
cd <repo>
bash escape-room/fonts/get-fonts.sh     # only if fonts/ is missing
python3 escape-room/src/build_all.py    # regenerates html/ and pdf/
```

`build_all.py` calls `node escape-room/render.js` at the end. Render needs Playwright + Chromium. If that is not installed locally, skip it and open the files in `escape-room/html/` in Chrome and print to PDF with **background graphics on** and **margins: none** (the pages set their own `@page` margins).

To check one page visually: `python3 escape-room/preview.py escape-room/pdf/06-register-of-names.pdf 1 90` writes a PNG next to it.

---

## 3. Verified facts about the built files

These were checked by grepping the generated HTML, not assumed. As of this handoff:

| Chain step | What the built sheet actually says |
|---|---|
| Knife weight | No. 9, **The Lemonade Knife**, **79 g**, "made for lemonade… cutting lemons open" |
| Ed Sheeran's entry | favourite air **The Barista's Hornpipe**; notes: **the dotted half note, then the pair of beamed eighth notes** |
| Those two shapes in that air | **12** and **15** (confirmed in `songbook_data.json`) |
| Concordance p.12 | "the fourth word of the first line" → **corn** |
| Concordance p.15 | "the sixth word of the first sentence on the page that begins with **Give**" → **bread** |
| Cornbread pairing | "Best eaten while playing a game of **backgammon**." Only occurrence of the word in the book. |
| Joker | "its fortune is sought **at the back of the upstairs toilet**" ← **NEEDS CHANGING, see §5** |
| Patricia | "Keepsake: **a tin of coffee**" ← **NEEDS CHANGING** |
| Chloe | "Keepsake: **a pillowcase**" ← **NEEDS CHANGING** |
| Shirley | "Keepsake: **a recipe card**" ← should change with the others |
| Sarah | "Keepsake: **the author's whole heart**" ← keep, it is a gift not a clue |
| Cipher wheel | **3:30**, long hand on the 6, short hand between 3 and 4, a **200°** turn |

### 3.1 The cipher time discrepancy — read carefully

`src/cipher_data.py` currently says `SOLUTION_TIME = '2:00'` with `HOUR_ANGLE, MINUTE_ANGLE = 60, 0`. **That edit never reached a PDF.** The built `02-cipher-wheel.pdf` and its solution sheet are both **3:30**.

`ROT` is 200 in both versions, and the letter mapping depends *only* on `ROT` and `SEED`. **So the substitution table in §4 is correct either way.** Only the printed angle of the hands differs.

**Decide one and be consistent:** either set `cipher_data.py` back to 3:30 (`SOLUTION_TIME='3:30'`, `HOUR_ANGLE, MINUTE_ANGLE = 105, 180`) so source matches the built PDFs, or leave it at 2:00 and rebuild both cipher PDFs. Ben originally said, verbatim: *"Let's do let's do three thirty. That feels good to me."* **Recommendation: go back to 3:30.**

### 3.2 The Dutch oven is not in any built sheet

`config.json` says `"joker_location": "in the Dutch oven"` but that was edited after the last build, so no PDF contains it. The built card guide still says the toilet. §5 fixes this.

### 3.3 Loose files that are NOT in the repo

These were authored directly and sent to Ben as files. They need to be saved into the repo:

- **`vundabar-flyer.html`** — the Alien Blues gig flyer, prints on Letter. Fake tour dates with "TONIGHT — THE BATHROOM, UPSTAIRS" in the middle of the list. No time on it, as he asked. Bathroom directions line is a placeholder he said doesn't matter.
- **`clue-frames.html`** — two Letter pages, four quarter-sheet frames each, double-rule border, corner fleurons, "No. ___" line, blank middle for handwriting. Four faintly lined, four plain.
- **`flags.html`** — the Hall of Flags (see §3.4).
- **`vercel.json`** — redirects `/` to `/flags.html`, keeps the old game at `/bubba`.
- **`master-plan.html`** — the planning doc with the mermaid flowchart. Superseded by this handoff; keep or bin.

### 3.4 The flags page (parked but working)

`flags.html`: 20 flags drawn as inline SVG, **no country names anywhere**, plates numbered I to XX, tap to flip, pigpen on every back. Styled to match the Pocket Library printables (IM Fell, double rules, "the engraver was paid by the flag and not by the name"). Mobile-friendly, single theme on purpose.

- **Plate VII = Ethiopia**, back says `HALF PAST THREE` (was `THE HANDS STAND AT TWO`; changed to match the 3:30 plates)
- **Plate XIV = Italy**, back says `TUCK AND DRAW` (points at Wingspan)
- Deliberate look-alikes sit near both: Mali and Bolivia and Ghana near Ethiopia; Ireland, Ivory Coast, Hungary near Italy
- The other 18 backs are short jokes: `NEIN`, `WAFFLES`, `PIEROGI`, `SAKAI STEEL`, `NOT AUSTRALIA`, `CLOSE BUT NO`, etc.

Deploy: `flags.html` in repo root + replace `vercel.json`, push, and sarahs.quest serves it.

---

## 4. The two ciphers

### 4.1 The wheel (Horological Cipher)

Two printed plates. Plate II (hands, smaller) is cut out and pinned through the centre of Plate I (dial, larger) with a brad so it spins. Turned until the hands read the target time on the dial's clock numerals, the two symbol rings line up into a substitution key.

The rim of Plate I reads: *SET THE HOUR · FIND IT WITHOUT · READ IT WITHIN*. That is the instruction — she finds a symbol on the **outer** dial and reads the letter beneath it on the **inner** disc.

**Write messages using this table (plain → what you write for her):**

```
A→K  B→D  C→R  D→7  E→W  F→L  G→A  H→5  I→O  J→T  K→6  L→M
M→V  N→Y  O→F  P→9  Q→G  R→8  S→Q  T→H  U→3  V→4  W→P  X→N
Y→J  Z→Z  0→U  1→I  2→C  3→E  4→B  5→0  6→2  7→S  8→1  9→X
```

Worked examples:

```
THE BAG WAS NEVER LOCKED   ->  H5W DKA PKQ YW4W8 MFR6W7
THE KEY IS IN THE FREEZER  ->  H5W 6WJ OQ OY H5W L8WWZW8
LOOK IN THE DUTCH OVEN     ->  MFF6 OY H5W 73HR5 F4WY
THE BACKGAMMON SET         ->  H5W DKR6AKVVFY QWH
BREATHE IN BREATHE OUT     ->  D8WKH5W OY D8WKH5W F3H
```

Or run it: `python3 escape-room/src/cipher_data.py YOUR MESSAGE HERE` prints plain and cipher and self-checks the round trip.

Digits work too, so you can hide a number or a time.

### 4.2 Pigpen

Standard Freemason's pigpen. `09-pigpen-key.pdf` is the key sheet for Sarah: the four pens, the full alphabet in glyphs, and a practice line reading THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.

To draw a message as glyphs for tracing: `python3 escape-room/src/build_pigpen.py "BREATHE IN BREATHE OUT SIT WITH IT"` writes `html/pigpen-message.html`, which prints the glyphs plus a small game-master line saying what it reads. Print it, then trace the glyphs onto the bathroom tile in invisible ink under the words ALIEN BLUES written in dry-erase marker.

---

## 5. THE BUILD TASK — do this first

Ben's exact instruction: *"change up the pdf and make itp rintbable. yeah use the dutch oven for someting… the tin of fcoffee is wrong and i odnt wnna do the pillwo case iether . incorproate wingspan backgmmon the other stuff etc"*

Two files change, then rebuild.

### 5.1 `src/config.json`

Set it to exactly this:

```json
{
  "_comment": "Edit these, then run: python3 escape-room/src/build_all.py",
  "patricia_keepsake": "a small painted egg, of the sort kept in a box of birds",
  "chloe_keepsake": "a young tree in a pot, and the soil beneath it",
  "shirley_keepsake": "a bottle kept for company, among the other bottles",
  "joker_location": "in the Dutch oven",
  "joker_quip": "Lift the lid. If there is a stew in it, you have the wrong Dutch oven and somebody should be told."
}
```

Why each one:
- **Patricia → the Wingspan box.** Wingspan uses little coloured eggs, so "a small painted egg, of the sort kept in a box of birds" is unmistakable once she thinks of the game, and means nothing before that. This is what "incorporate wingspan" cashes out to.
- **Chloe → the bonsai.** Chloe means "green shoot, young verdure", which is already printed next to her name in the register. The keepsake and the meaning agree, which makes it feel authored rather than arbitrary. (He listed the bonsai as a fake spot originally; it is a much better real one, and no other clue points there.)
- **Shirley → the liquor cabinet.** He offered it as "something random"; it is a good, findable, adult-feeling spot for the sixth painting's payoff.
- **Joker → the Dutch oven.** His explicit ask.

`build_names.py` already reads `shirley_keepsake` (that edit is in the working tree, uncommitted — see §8).

### 5.2 `src/build_cards.py` — put the toilet back in play, key only

The toilet must still be used (he wanted something cheeky there) but must hold **only a key**, never a painting. Since the Joker now points at the Dutch oven, give the toilet to a specific card and physically plant that card.

In `build_cards.py`, the `PLACES` list is consumed in order: Hearts A→K first (indices 0–12), then Diamonds, Clubs, Spades. **Index 11 is the Queen of Hearts.** Change that entry to:

```python
'at the back of the upstairs toilet, where a noble woman does not look twice'
```

Then hide a real **Queen of Hearts** playing card in the Wingspan box. She finds it, looks it up in the guide, goes to the cistern, finds the key in a ziplock. That reuses a document she already knows how to read, which is exactly the "half clue" he asked for.

While you are in that file, swap some of the generic `PLACES` for his real apartment fakes so the red herrings feel like his flat: `in the toaster oven`, `in the spice drawer`, `in the dishwasher`, `in a pint of creatine`, `in the bag of rice`, `nestled in the mixing bowls`, `under the cutting board`, `inside the Coup box`, `inside the chess set`, `in the freezer`. **Do not** put backgammon, Wingspan, the Dutch oven, the bonsai, the liquor cabinet, or the meditation cushion in that list — those are real, and a fake pointer at a real spot is the one thing that will actually confuse her.

Same treatment in `src/content_recipes.py` for a handful of the "best eaten while…" pairings, but **do not touch the cornbread line** — it is the only backgammon in the book and the assert in the verification depends on it.

### 5.3 Cipher time

Set `src/cipher_data.py` back to 3:30 so source matches the built plates:

```python
SOLUTION_TIME = '3:30'
HOUR_ANGLE, MINUTE_ANGLE = 105, 180
ROT = 200
```

### 5.4 Rebuild and verify

```bash
python3 escape-room/src/build_all.py
```

Then confirm, by grep or by eye:
- register: Patricia → painted egg, Chloe → young tree, Shirley → bottle, Sarah → whole heart
- card guide: Joker → Dutch oven, Queen of Hearts → upstairs toilet
- knife catalogue: still exactly one 79 g knife
- recipe book: still exactly one occurrence of "backgammon", on cornbread
- cipher solution sheet: says 3:30

---

## 6. The chain, end to end

She is handed **one envelope**: the welcome letter and the Milk Crate painting. Everything else is out in the room or hidden behind a step.

**Branch A — music**
1. Milk Crate painting, back: *the famous man we always see here*
2. → Stars and Their Notes → **Ed Sheeran** → *The Barista's Hornpipe*, dotted half + beamed eighths
3. → Songbook, that air → **12** and **15**
4. → Concordance + *The Prophet* on the shelf → **CORN**, **BREAD**
5. → Receipt Book, cornbread → **backgammon**
6. → **THE BACKGAMMON SET**: Plate II, the knife, the Patricia painting

**Branch B — names**
7. Patricia painting → Register → *a small painted egg…* → **THE WINGSPAN BOX**: the scale, the Hamlet painting, the fairy painting, a Queen of Hearts card
8. Queen of Hearts → Cartomancer's Guide → **THE TOILET CISTERN**: the key, in a ziplock
9. Hamlet painting → Hamnet → Chloé Zhao → Register, Chloe → *a young tree in a pot* → **THE BONSAI**: the blue-light pen
10. Fairy painting → Shirley → Register → *a bottle kept for company* → **THE LIQUOR CABINET**: the pigpen key

**Branch C — knife**
11. The knife + the scale → **79 g** → Knife Catalogue → *The Lemonade Knife*, cut lemons open
12. → cut the lemons → **the Joker** → Cartomancer's Guide → **THE DUTCH OVEN**: Plate I

**Convergence**
13. Flyer on the fridge (Vundabar, Alien Blues, in the bathroom) + blue-light pen + pigpen key → the bathroom wall reads **BREATHE IN BREATHE OUT SIT WITH IT**
14. → **THE MEDITATION CUSHION**: the final message card, written in wheel symbols
15. Plate I + Plate II + the time (3:30) → she decodes the card
16. → the last instruction → the locked bag she has been looking at all evening

**The two paintings not yet placed:** Abyssinia and Gleaners. With the flags parked, either bring the flags back (§3.4, they are done and working) or write their clues by hand on two of the quarter-sheet frames pointing wherever you like. They are currently the only loose ends in the six.

**Where the time comes from, pick one:**
- flags live → Plate VII says HALF PAST THREE, and the Abyssinia painting sends her to sarahs.quest
- flags parked → write "half past three" by hand on the back of the Abyssinia painting, or put a small card with a drawn clock face in the Dutch oven beside Plate I

**Length:** roughly 16 real steps, some quick. Expect 75–110 minutes for one person. To shorten: put the pigpen key in the bonsai with the pen and drop step 10, which removes one lookup and frees the fairy painting to be pure sentiment.

---

## 7. Every hiding place and its contents

| Spot | Holds | Pointed at by |
|---|---|---|
| Handed to her | Welcome letter, Milk Crate painting | — |
| In plain sight | The Library (9 printables), the flyer on the fridge, a bowl of lemons, *The Prophet* among many books, the locked bag | — |
| Backgammon set | Plate II, the knife, Patricia painting | cornbread recipe |
| Wingspan box | The scale, Hamlet painting, fairy painting, a Queen of Hearts card | Patricia → painted egg |
| Toilet cistern | **The key, in a ziplock. No paper. No paintings.** | Queen of Hearts card |
| The bonsai | Blue-light pen | Chloe → young tree in a pot |
| Liquor cabinet | The pigpen key | Shirley → a bottle kept for company |
| Dutch oven | Plate I, with a brad taped to it | the Joker in the lemon |
| Bathroom wall | ALIEN BLUES in dry-erase, pigpen in invisible ink beneath | the flyer |
| Meditation cushion | The final wheel-symbol card | the decoded wall |
| The locked bag | The prize, the final card | the decoded cushion card |

**Fakes, documents only, never real:** toaster oven, spice drawer, dishwasher, pint of creatine, bag of rice, mixing bowls, under the cutting board, inside Coup, inside the chess set, the freezer.

---

## 8. Repo state and the blocker

**Two files are modified and uncommitted** in the remote session's working tree:
- `escape-room/src/config.json`
- `escape-room/src/build_names.py` (adds the `shirley_keepsake` lookup)

Last commit on the branch: *"Add pigpen cipher key sheet and message encoder"*.

**Why they were never pushed:** partway through the remote session, git writes and all shell execution were blocked by a session-level safety check, and separately GitHub refused every write with HTTP 403 ("Claude doesn't have GitHub access to eudaimonictoad/valentinesday for your organization"). Branch creation through the GitHub API failed the same way with "Resource not accessible by integration". Read-only git and grep kept working, which is how §3 was verified.

**On the local machine none of that applies.** Commit and push normally. To restore GitHub access for remote sessions later: install the Claude GitHub App for the repo at https://github.com/apps/claude/installations/select_target, or reconnect GitHub under claude.ai Settings → Connectors.

Commit trailer used on this branch:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JWvfNQhCGYTVxZ34crbqJz
```

---

## 9. House style, so anything new matches

- **Fonts:** IM Fell English (body), IM Fell DW Pica SC and IM Fell English SC (headings, small caps), UnifrakturMaguntia (mastheads), Old Standard TT (numerals, tables), Libre Baskerville (cipher symbols), Noto Music (musical glyphs), Special Elite / Rye / Pinyon Script (available, mostly unused). All local in `fonts/`, wired up by `fonts/fonts.css`.
- **Every sheet is pure black on white**, Letter, no colour, no images. He is printing at a copy shop.
- **Voice:** dry Victorian trade catalogue. Confident, specific, faintly absurd, never winking too hard. The knife catalogue apologises for a dispute with the engraver. The register admits "one exception for its accuracy". The card guide says the cards "do not care whether you believe them."
- **Shared furniture:** `masthead()` in `src/common.py`, `.page`, `.cols2`, `.cols3`, `.foot`, `.sc` in `html/style.css`.
- Volume is the point. 27 knives, 74 recipes, 276 names, 84 concordance rules, 20 airs, 32 celebrities. One true entry each.

---

## 10. Checklist for the night

**Print** — everything in `pdf/` **except** `02-cipher-wheel-SOLUTION-gamemaster-only.pdf`, plus `vundabar-flyer.html` and `clue-frames.html` from a browser. Plates on card stock if the shop has it. Songbook stapled.

**Make**
- [ ] Cut out both cipher plates; brad through the centre of Plate I; tape the brad down
- [ ] Weigh the actual knife — it must read **79 g** on the actual scale (the catalogue's nearest neighbours are 58 g and 99 g, so about 14 g of slack either way)
- [ ] The lemon: print a joker ~25×35 mm, wrap in cling film, slit one lemon lengthways at the stem end, push the roll in, wipe, put it in a bowl with three or four honest lemons
- [ ] Bathroom wall: ALIEN BLUES in dry-erase marker, pigpen beneath in invisible ink; **test that the pen reveals it and that it wipes off the tile**
- [ ] Write the six painting backs on the quarter-sheet frames
- [ ] Write the welcome letter; give her sarahs.quest if the flags go live; end it with *breathe in, breathe out, and sit with it*
- [ ] Write the final wheel-symbol card for under the cushion
- [ ] Plant the Queen of Hearts in the Wingspan box; key in a ziplock in the cistern
- [ ] Three hint envelopes, opened only if stuck ten minutes

**Test**
- [ ] Check pages 12 and 15 of **his actual copy** of *The Prophet* against the concordance rules — editions differ, and the rules live in the `REAL` dict at the top of `build_concordance.py`
- [ ] Assemble the wheel at 3:30 and decode the cushion card yourself
- [ ] Walk the whole chain with a timer

---

## 11. The only real open questions

1. **What the final wheel card says.** Under 25 letters. If the bag is on the table all evening, `THE BAG WAS NEVER LOCKED` → `H5W DKA PKQ YW4W8 MFR6W7` is a good ending. Otherwise name where the key is.
2. **Flags live or parked**, which decides where "half past three" comes from and what the Abyssinia and Gleaners paintings do.
3. **The welcome letter.** Ben writes it. It should hand her sarahs.quest if the flags are live, warn that not everything can be read on the day it is found, and end with *breathe in, breathe out, and sit with it*.

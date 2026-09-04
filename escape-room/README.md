# Escape-room printables (game-master notes)

Print everything in `pdf/` in black and white on Letter paper. **`pdf/ALL-escape-room-print-me.pdf` is the one file to print.** Its last four pages are for you only (the wall tracing sheet, the three-page setup guide with flowchart and lock order, and the cipher solution); tear them off before she arrives. `verify.py` re-checks every link in the chain.

| File | What it is | The real clue inside |
|---|---|---|
| `01-knife-catalogue.pdf` | Hawthorne & Daughters cutlery catalogue, 27 knives with weights in grams | No. 9, *The Lemonade Knife*, **79 g**, "made for lemonade… cutting lemons open". Every other weight is at least 15 g away from 79. |
| `02-cipher-wheel.pdf` | Two plates of the Horological Cipher: Plate I (the dial) and Plate II (the hands). Cut both out, pin Plate II on the centre of Plate I with a brad. | Turned so the hands read **3:30**, the dial and the inner disc line up into the substitution key. Cipher text is written in dial (outer) symbols; she finds each on the dial and reads the symbol beneath it on the inner disc (the rim says *find it without, read it within*). Letters and digits both work. |
| `02-cipher-wheel-SOLUTION-…pdf` | Assembled wheel at 3:30, the full mapping table, and an example. | To write your own message: `python3 escape-room/src/cipher_data.py YOUR MESSAGE HERE` |
| `03-parlour-songbook.pdf` | 20 fake airs, each note shape numbered; page 1 is a key to the note shapes (no numbers). | In *The Barista's Hornpipe*, the **dotted half note = 12** and the **pair of beamed eighths = 15**. Every other air has its own random numbering. |
| `04-stars-and-their-notes.pdf` | 32 celebrities, each with a favourite air and two favourite notes | **Ed Sheeran → The Barista's Hornpipe → the dotted half note, then the pair of beamed eighths → 12, 15** → pages 12 and 15 in the concordance (file 08) → corn + bread. |
| `05-household-receipt-book.pdf` | 74 short recipes, each with a "best enjoyed while…" pairing | **Cornbread: "Best eaten while playing a game of backgammon."** All other pairings are red herrings (household hiding spots, other board games, etc.). |
| `06-register-of-names.pdf` | 275 girls' names with origin, meaning, and a "keepsake" object | **Patricia → a small painted egg (the Wingspan box). Chloe → a young tree in a pot (the bonsai). Shirley → a bottle kept for company (the liquor cabinet).** Sarah → a stuffed animal named Sushi. All in `src/config.json`. |
| `07-cartomancers-pocket-guide.pdf` | Meaning of all 52 cards and where each "fortune is sought" | **Joker → at the back of the upstairs toilet** (with a cheeky line about lifting the lid). Change in `src/config.json`. |
| `08-prophet-concordance.pdf` | "A Reader's Concordance" to *The Prophet*: one counting rule per page, 1 to 84 | **Page 12: the fourth word of the first line = corn. Page 15: the sixth word of the first sentence beginning with "Give" = bread** ("Give one another of your bread…"). All other pages give random words. Footer says to read words in the order sought. Replaces the cut-out template. |

## Changing the three placeholder locations

Edit `src/config.json` (Patricia's keepsake, Chloe's keepsake, the Joker's location and its quip), then rebuild:

```
python3 escape-room/src/build_all.py
```

That regenerates the HTML in `html/` and the PDFs in `pdf/`. It needs the fonts (`bash escape-room/fonts/get-fonts.sh` downloads them once) and Node + Playwright with Chromium for the PDF step; if that's not on your machine, open the HTML files in Chrome and print to PDF with backgrounds on.

The PDFs and font files are not committed (GitHub access from this session only allowed text files); the PDFs were delivered directly in the chat.

## Changing the Prophet words

The two real page rules live in `REAL` at the top of `src/build_concordance.py`; every other page gets a random rule.

## Changing the cipher answer

`src/cipher_data.py` holds `SOLUTION_TIME`, `HOUR_ANGLE`, `MINUTE_ANGLE` (where the hands must point, degrees clockwise from 12) and `ROT` (how far Plate II must be turned, a multiple of 10). Rebuild after editing.

## Layout

- `src/` Python generators (one per printable) and content files
- `html/` generated HTML (open in a browser to preview or print)
- `pdf/` generated PDFs
- `fonts/` Google Fonts used by the pages (IM Fell, Old Standard, Unifraktur, Noto Music)
- `render.js` HTML → PDF via Playwright; `preview.py` PDF → PNG for checking

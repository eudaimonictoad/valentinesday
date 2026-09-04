# Assemble the print-ready packs from pdf/*.pdf.  Run after: python3 src/build_all.py
#   python3 pack.py
# Produces ALL-escape-room-print-me.pdf (the one file to print) and the two reprint packs.
import os, pymupdf

os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = lambda n: os.path.join('pdf', n + '.pdf')

# (file, bookmark)  — order is the printed order. HERS first, then the game-master leaves.
HERS = [
    ('01-knife-catalogue',          'Knife catalogue'),
    ('02-cipher-wheel',             'Cipher plates I and II'),
    ('03-parlour-songbook',         'Parlour songbook'),
    ('04-stars-and-their-notes',    'Stars and their notes'),
    ('05-household-receipt-book',   'Household receipt book'),
    ('06-register-of-names',        'Register of names'),
    ('07-cartomancers-pocket-guide', "Cartomancer's guide"),
    ('08-prophet-concordance',      'Prophet concordance'),
    ('09-pigpen-key',               'Pig-pen alphabet'),
    ('11-vundabar-flyer',           'Vundabar flyer'),
    ('12-clue-frames',              'Clue frames (12 blanks)'),
    ('13-framers-delivery-card',    "Framer's delivery card"),
]
# These MUST stay last and MUST stay together: the set-up order tells him to tear
# off exactly this many leaves from the back.
GM = [
    ('pigpen-message',                        'GM: wall to trace (remove)'),
    ('10-mapping-GAMEMASTER-remove',          'GM: setup guide (remove)'),
    ('02-cipher-wheel-SOLUTION-gamemaster-only', 'GM: cipher solution (remove)'),
]


def merge(parts, out):
    """parts: list of (pdf-stem, bookmark or None). Returns {stem: (first_page, n_pages)}."""
    doc = pymupdf.open()
    toc, where = [], {}
    for stem, mark in parts:
        src = pymupdf.open(P(stem))
        start = doc.page_count + 1
        doc.insert_pdf(src)
        where[stem] = (start, src.page_count)
        if mark:
            toc.append([1, mark, start])
        src.close()
    doc.set_toc(toc)
    doc.save(os.path.join('pdf', out), garbage=4, deflate=True)
    doc.close()
    return where


# The change that moved the two flag paintings out of the candy jar. He has already
# printed the 40-page packet, so this pack is only what that change touches.
REPRINT_PAINTINGS = [
    ('reprint-cover-paintings',       None),
    ('13-framers-delivery-card',      "HERS: new sheet, goes after the clue frames"),
    ('10-mapping-GAMEMASTER-remove',  'YOURS: replaces packet 35-39, setup guide'),
]


def main():
    where = merge(HERS + GM, 'ALL-escape-room-print-me.pdf')
    total = sum(n for _, n in where.values())
    gm_pages = sum(where[s][1] for s, _ in GM)
    hers = total - gm_pages
    print(f'ALL-escape-room-print-me.pdf  {total} pages   hers 1-{hers}, game-master {hers+1}-{total}')
    for stem, mark in HERS + GM:
        a, n = where[stem]
        print(f'   {a:>3}-{a+n-1:<3} {mark}')
    # The guide instructs him to tear off the last seven leaves. Keep that honest.
    assert gm_pages == 7, f'game-master section is {gm_pages} pages; the setup guide says seven'
    print(f'\ngame-master leaves to tear off: {gm_pages}  (setup guide says seven)')

    w2 = merge(REPRINT_PAINTINGS, 'REPRINT-paintings-moved.pdf')
    n2 = sum(n for _, n in w2.values())
    print(f'\nREPRINT-paintings-moved.pdf  {n2} pages  (1 cover + {n2-1} to print)')
    for stem, mark in REPRINT_PAINTINGS:
        a, n = w2[stem]
        print(f'   {a:>3}-{a+n-1:<3} {mark or "cover"}')


if __name__ == '__main__':
    main()

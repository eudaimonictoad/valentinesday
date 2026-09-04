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
    ('14-painting-back-clues',      'The six painting backs'),
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


# Ben printed the 40-page packet and nothing since. This is everything that has
# changed since then, in packet order: six sheets of hers, seven of his.
REPRINT_CATCHUP = [
    ('reprint-cover-catchup',        None),
    ('02-cipher-wheel',              'HERS: replaces packet 3-4, cipher plates'),
    ('07-cartomancers-pocket-guide', 'HERS: replaces packet 26-27, card guide'),
    ('09-pigpen-key',                'HERS: replaces packet 29, pig-pen alphabet'),
    ('14-painting-back-clues',       'NEW: the six painting backs, cut up during set-up'),
    ('13-framers-delivery-card',     'HERS: new sheet, after the clue frames'),
    ('pigpen-message',               'YOURS: replaces packet 34, the wall to trace'),
    ('10-mapping-GAMEMASTER-remove', 'YOURS: replaces packet 35-39, setup guide'),
    ('02-cipher-wheel-SOLUTION-gamemaster-only', 'YOURS: replaces packet 40, solution'),
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

    w3 = merge(REPRINT_CATCHUP, 'REPRINT-everything-since-your-print.pdf')
    n3 = sum(n for _, n in w3.values())
    print(f'\nREPRINT-everything-since-your-print.pdf  {n3} pages  (cover + {n3-1} to print)')
    for stem, mark in REPRINT_CATCHUP:
        a, n = w3[stem]
        print(f'   {a:>3}-{a+n-1:<3} {mark or "cover"}')
    cover3 = w3['reprint-cover-catchup'][1]
    assert cover3 == 1, f'the catch-up cover is {cover3} pages; it tells him to print from page 2'
    assert n3 - cover3 == 14, f'catch-up pack is {n3-cover3} sheets, the cover says fourteen'



if __name__ == '__main__':
    main()

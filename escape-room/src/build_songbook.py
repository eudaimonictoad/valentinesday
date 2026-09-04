import random, json, os
from common import *
from music import *

SEED = 1215
SONGS = [
 ("Air for a Rainy Tuesday", "Mrs. E. Pennywhistle", "Andante", 4),
 ("The Copy-Shop Reel", "Trad., arr. O. Blount", "Lively", 4),
 ("Waltz for a Geneticist", "L. Marchetti", "Tempo di valse", 3),
 ("The Milkmaid's Lament", "Anon., 18th c.", "Slowly, with feeling", 4),
 ("Coffee at Dawn", "T. Ashby", "Moderato", 4),
 ("A Nocturne for the Park", "C. Devereux", "Quietly", 3),
 ("The Lemon Tree Polka", "F. Kraus", "Allegretto", 4),
 ("The Painter's Gavotte", "J. Lindqvist", "Gracefully", 4),
 ("March of the Small Paintings", "H. Whitlock", "Alla marcia", 4),
 ("The Tram to Brunswick", "A. Moreno", "Steadily", 4),
 ("Song of the Sock Drawer", "Anon.", "Comfortably", 3),
 ("The Barista's Hornpipe", "H. Whitlock", "Briskly", 4),
 ("Minuet for Two Teacups", "L. Marchetti", "Tempo di minuetto", 3),
 ("The Landlord's Jig", "Trad., arr. O. Blount", "Fast, and then faster", 4),
 ("Lullaby for a Houseplant", "Mrs. E. Pennywhistle", "Very gently", 3),
 ("The Fire-Escape Waltz", "C. Devereux", "Swaying", 3),
 ("Hymn to the Dishwasher", "T. Ashby", "Solemnly", 4),
 ("The Sunday Crossword Rag", "R. Okafor", "Not too fast", 4),
 ("Serenade for the Last Slice", "J. Lindqvist", "Longingly", 4),
 ("Farewell to the Fourth Floor", "A. Moreno", "Maestoso", 4),
]
# Ed Sheeran's favourite notes in his favourite air map to pages 12 and 15 of The Prophet.
ED_SONG = "The Barista's Hornpipe"
ED_NOTES = [('dotted_half', 12), ('eighth_pair', 15)]

W = 700; INDENT = 62; MEASURES = 4; SYSTEMS = 3
MW = (W - INDENT) / MEASURES

def choose_types(rng, beats, forced=()):
    pool = [k for k in TYPES if not (beats == 3 and k in ('whole', 'whole_rest'))]
    n = rng.randint(8, 11)
    chosen = set(forced)
    chosen.update(('quarter',))
    while len(chosen) < n:
        chosen.add(rng.choice(pool))
    return sorted(chosen)

def fill_measure(rng, types, beats):
    """Random sequence of note types whose durations sum to `beats`, fitting the measure width."""
    for _ in range(400):
        seq, total, width = [], 0, 0
        while total < beats and len(seq) < 7:
            cands = [t for t in types if TYPES[t][1] <= beats - total + 1e-9]
            if not cands: break
            t = rng.choice(cands)
            seq.append(t); total += TYPES[t][1]; width += GLYPH_WIDTH[t]
        if abs(total - beats) < 1e-9 and width + 8 * (len(seq) + 1) <= MW - 6:
            return seq
    return ['quarter'] * beats

def make_song(rng, title, beats, forced=()):
    types = choose_types(rng, beats, [t for t, _ in forced])
    nums = rng.sample(range(1, 41), len(types))
    numbering = dict(zip(types, nums))
    for t, n in forced:
        # swap so that the forced type gets its required number
        other = [k for k, v in numbering.items() if v == n]
        if other:
            numbering[other[0]] = numbering[t]
        numbering[t] = n
    for _ in range(200):
        measures = [fill_measure(rng, types, beats) for _ in range(MEASURES * SYSTEMS)]
        used = {t for m in measures for t in m}
        if used == set(types):
            break
    else:
        # force any missing type into some measure by replacing a quarter note of equal length
        # iterate in `types` order, not set order: a set's iteration order varies
        # with PYTHONHASHSEED, which made every rebuild produce different music
        for t in [x for x in types if x not in used]:
            for m in measures:
                if 'quarter' in m and TYPES[t][1] == 1:
                    m[m.index('quarter')] = t; break
    pitches = {}
    return {'title': title, 'beats': beats, 'types': types, 'numbering': numbering, 'measures': measures}

def song_svg(song, rng):
    beats = song['beats']; out = []
    top0 = 54
    sysH = 100
    height = top0 + SYSTEMS * sysH
    for s in range(SYSTEMS):
        top = top0 + s * sysH
        out.append(staff(0, top, W))
        out.append(clef_and_time(0, top, beats))
        out.append(barline(INDENT, top))
        for mi in range(MEASURES):
            m = song['measures'][s * MEASURES + mi]
            x0 = INDENT + mi * MW
            widths = [GLYPH_WIDTH[t] for t in m]
            gap = (MW - 6 - sum(widths)) / (len(m) + 1)
            x = x0 + 3 + gap
            for t, w in zip(m, widths):
                pos = rng.choice([1, 2, 3, 4, 5, 6]) if 'rest' not in t else 4
                g, ww, xc = TYPES[t][2](x, top, pos)
                out.append(g)
                out.append(label(xc, top, song['numbering'][t]))
                x += w + gap
            out.append(barline(x0 + MW, top, final=(s == SYSTEMS - 1 and mi == MEASURES - 1)))
    return f'<svg viewBox="0 0 {W} {height}" width="{W}" height="{height}" xmlns="http://www.w3.org/2000/svg">' + ''.join(out) + '</svg>'

CSS = """
.song { break-inside: avoid; margin-bottom: 14px; }
.song .t { font-family: 'IM Fell DW Pica SC'; font-size: 17pt; letter-spacing: 0.05em; text-align: center; }
.song .meta { display: flex; justify-content: space-between; font-style: italic; font-size: 10pt; margin: 0 2px 0; }
.song svg { display: block; width: 7.3in; }
.pagehead { display: flex; justify-content: space-between; font-family: 'IM Fell DW Pica SC'; font-size: 9.5pt; letter-spacing: 0.12em; border-bottom: 1px solid #000; margin-bottom: 6px; }
.gloss { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 4px 14px; margin-top: 8px; }
.gloss .g { display: flex; align-items: center; gap: 10px; border-bottom: 1px dotted #000; padding-bottom: 2px; }
.gloss .g svg { flex: 0 0 auto; }
.gloss .g .n { font-size: 9.5pt; line-height: 1.15; }
.preface { font-size: 10.5pt; text-align: justify; margin: 6px 0; }
"""

def glossary_svg(t):
    top = 34; w = 70
    g, ww, xc = TYPES[t][2](16, top, 3)
    return f'<svg viewBox="0 0 {w} 72" width="{w}" height="72" xmlns="http://www.w3.org/2000/svg">{staff(0, top, w)}{g}</svg>'

def build():
    rng = random.Random(SEED)
    songs = []
    for title, comp, tempo, beats in SONGS:
        forced = ED_NOTES if title == ED_SONG else ()
        s = make_song(rng, title, beats, forced)
        s['composer'] = comp; s['tempo'] = tempo
        songs.append(s)
    # verify Ed's numbers
    ed = next(s for s in songs if s['title'] == ED_SONG)
    for t, n in ED_NOTES:
        assert ed['numbering'][t] == n, (t, ed['numbering'])
        # numbering alone is not enough: the shape has to actually be printed in the
        # air, or Stars and Their Notes points at a note that is not on the page.
        assert any(t in m for m in ed['measures']), \
            f'{t} is numbered {n} but never appears in {ED_SONG}'
    with open(os.path.join(ROOT, 'src', 'songbook_data.json'), 'w') as f:
        json.dump([{ 'title': s['title'], 'beats': s['beats'], 'numbering': s['numbering']} for s in songs], f, indent=1)

    pages = []
    gl = ''.join(f'<div class="g">{glossary_svg(t)}<div class="n">{esc(TYPES[t][0])}</div></div>' for t in TYPES)
    pages.append(f"""<div class="page">
{masthead('The Parlour Songbook', 'Twenty Airs for the Beginning Player', 'With every Note Shape numbered for ready Reference · Whitlock &amp; Sons, Music Sellers')}
<p class="preface">In this collection each note shape that appears in an air is marked with a small figure above it, so that the student may look up the shape in this Key and learn its name and value before attempting the piece. The figures differ from air to air, as every air has its own lesson plan; a shape's figure in one air tells you nothing of its figure in another. Play slowly, count aloud, and do not be discouraged by the Landlord's Jig.</p>
<div class="sc center" style="font-size:13pt;margin-top:4px">A Key to the Note Shapes</div>
<div class="gloss">{gl}</div>

</div>""")
    for i in range(0, len(songs), 2):
        pair = songs[i:i+2]
        blocks = ''
        for s in pair:
            blocks += f"""<div class="song"><div class="t">{esc(s['title'])}</div>
<div class="meta"><span>{esc(s['tempo'])}</span><span>{esc(s['composer'])}</span></div>{song_svg(s, rng)}</div>"""
        pn = i // 2 + 1
        pages.append(f"""<div class="page"><div class="pagehead"><span>The Parlour Songbook</span><span>Airs {i+1} &amp; {i+2}</span><span>Page {pn}</span></div>{blocks}<div class="foot">Whitlock &amp; Sons · Page {pn} of {len(songs)//2}</div></div>""")
    write_page('03-parlour-songbook', ''.join(pages), 'The Parlour Songbook', CSS)
    return songs

if __name__ == '__main__':
    build()

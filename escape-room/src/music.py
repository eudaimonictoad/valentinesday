# Fake sheet-music drawing. Every note shape is drawn with stems up so that the
# same shape always looks the same and can be matched against the glossary.
import math
SP = 8            # staff line spacing
STAFF_H = 4 * SP

def head(xc, y, filled):
    fill = '#000' if filled else 'none'
    return f'<ellipse cx="{xc:.1f}" cy="{y:.1f}" rx="5.6" ry="3.9" transform="rotate(-22 {xc:.1f} {y:.1f})" fill="{fill}" stroke="#000" stroke-width="1.7"/>'

def stem(xc, y, length=30):
    xs = xc + 5.4
    return f'<line x1="{xs:.1f}" y1="{y-1:.1f}" x2="{xs:.1f}" y2="{y-length:.1f}" stroke="#000" stroke-width="1.4"/>', xs, y - length

def flag(xs, yt, n=1):
    out = []
    for i in range(n):
        y = yt + i * 7
        out.append(f'<path d="M{xs:.1f},{y:.1f} C{xs+1.5:.1f},{y+9:.1f} {xs+11:.1f},{y+10:.1f} {xs+8:.1f},{y+23:.1f} C{xs+10:.1f},{y+14:.1f} {xs+5:.1f},{y+11:.1f} {xs:.1f},{y+10:.1f} Z" fill="#000"/>')
    return ''.join(out)

def dot(xc, y, pos):
    yd = y - 3.5 if pos % 2 == 0 else y
    return f'<circle cx="{xc+9.5:.1f}" cy="{yd:.1f}" r="1.9" fill="#000"/>'

def beam(x1, x2, y, n=1):
    out = []
    for i in range(n):
        yy = y + i * 6.5
        out.append(f'<polygon points="{x1-0.7:.1f},{yy:.1f} {x2+0.7:.1f},{yy:.1f} {x2+0.7:.1f},{yy+4:.1f} {x1-0.7:.1f},{yy+4:.1f}" fill="#000"/>')
    return ''.join(out)

def music_text(x, y, ch, size=32, anchor='start'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="Noto Music" font-size="{size}" text-anchor="{anchor}">{ch}</text>'

def pos_y(top, pos):
    return top + STAFF_H - pos * (SP / 2)

# Each drawer: (svg, width, centre_x) given left x, staff top, pitch position
def d_whole(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    return head(xc, y, False), 16, xc
def d_half(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, False) + s, 16, xc
def d_dotted_half(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, False) + s + dot(xc, y, pos), 20, xc
def d_quarter(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s, 16, xc
def d_dotted_quarter(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s + dot(xc, y, pos), 20, xc
def d_eighth(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s + flag(xs, yt, 1), 22, xc
def d_dotted_eighth(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s + flag(xs, yt, 1) + dot(xc, y, pos), 24, xc
def d_sixteenth(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s + flag(xs, yt, 2), 22, xc

def beamed(x, top, poses, nbeams, gap=16):
    out = []; xs_list = []
    ytop = min(pos_y(top, p) for p in poses) - 32
    for i, p in enumerate(poses):
        xc = x + 7 + i * gap; y = pos_y(top, p)
        out.append(head(xc, y, True))
        xs = xc + 5.4
        out.append(f'<line x1="{xs:.1f}" y1="{y-1:.1f}" x2="{xs:.1f}" y2="{ytop:.1f}" stroke="#000" stroke-width="1.4"/>')
        xs_list.append(xs)
    out.append(beam(xs_list[0], xs_list[-1], ytop, nbeams))
    w = 7 + (len(poses) - 1) * gap + 10
    return ''.join(out), w, x + w / 2, ytop, xs_list

def d_eighth_pair(x, top, pos):
    s, w, xc, yt, _ = beamed(x, top, [pos, min(pos + 1, 7)], 1)
    return s, w, xc
def d_sixteenth_quad(x, top, pos):
    s, w, xc, yt, _ = beamed(x, top, [pos, pos + 1, pos, max(pos - 1, 0)], 2, gap=14)
    return s, w, xc
def d_sixteenth_pair(x, top, pos):
    s, w, xc, yt, _ = beamed(x, top, [pos, pos], 2)
    return s, w, xc
def d_triplet(x, top, pos):
    s, w, xc, yt, _ = beamed(x, top, [pos, pos + 1, pos], 1, gap=15)
    s += f'<text x="{xc:.1f}" y="{yt-3:.1f}" font-family="Old Standard TT" font-style="italic" font-size="10" text-anchor="middle">3</text>'
    return s, w, xc
def d_dotted_eighth_sixteenth(x, top, pos):
    # dotted eighth + sixteenth: single beam across, a short second beam on the right note
    s, w, xc, yt, xs = beamed(x, top, [pos, pos], 1, gap=18)
    s += dot(x + 7, pos_y(top, pos), pos)
    s += beam(xs[1] - 7, xs[1], yt + 6.5, 1)
    return s, w, xc

def d_whole_rest(x, top, pos):
    return music_text(x + 2, top + SP, '\U0001D13B', 30), 18, x + 9
def d_half_rest(x, top, pos):
    return music_text(x + 2, top + 2 * SP, '\U0001D13C', 30), 18, x + 9
def d_quarter_rest(x, top, pos):
    return music_text(x + 2, top + 2 * SP, '\U0001D13D', 30), 14, x + 7
def d_eighth_rest(x, top, pos):
    return music_text(x + 2, top + 2 * SP, '\U0001D13E', 30), 14, x + 7
def d_sixteenth_rest(x, top, pos):
    return music_text(x + 2, top + 2 * SP, '\U0001D13F', 30), 14, x + 7

def d_tie(x, top, pos):
    y = pos_y(top, pos); x1 = x + 7; x2 = x + 29
    s1, _, _ = stem(x1, y); s2, _, _ = stem(x2, y)
    arc = f'<path d="M{x1+2:.1f},{y+5:.1f} Q{(x1+x2)/2:.1f},{y+15:.1f} {x2-2:.1f},{y+5:.1f}" fill="none" stroke="#000" stroke-width="1.5"/>'
    return head(x1, y, True) + s1 + head(x2, y, True) + s2 + arc, 38, (x1 + x2) / 2
def d_chord(x, top, pos):
    p2 = pos + 2 if pos + 2 <= 8 else pos - 2
    y1 = pos_y(top, pos); y2 = pos_y(top, p2); xc = x + 7
    s, xs, yt = stem(xc, min(y1, y2))
    return head(xc, y1, True) + head(xc, y2, True) + s, 16, xc
def d_fermata(x, top, pos):
    y = pos_y(top, min(pos, 3)); xc = x + 7
    s, xs, yt = stem(xc, y, 24)
    return head(xc, y, True) + s + music_text(xc - 1, yt - 3, '\U0001D110', 24, 'middle'), 18, xc
def d_staccato(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    return head(xc, y, True) + s + f'<circle cx="{xc:.1f}" cy="{y+7.5:.1f}" r="1.8" fill="#000"/>', 16, xc
def d_accent(x, top, pos):
    y = pos_y(top, pos); xc = x + 7
    s, xs, yt = stem(xc, y)
    acc = f'<path d="M{xc-5:.1f},{y+7:.1f} L{xc+5:.1f},{y+10.5:.1f} L{xc-5:.1f},{y+14:.1f}" fill="none" stroke="#000" stroke-width="1.6"/>'
    return head(xc, y, True) + s + acc, 16, xc
def d_grace(x, top, pos):
    y = pos_y(top, pos); yg = pos_y(top, pos + 1); xg = x + 5; xc = x + 22
    g = f'<g transform="translate({xg:.1f},{yg:.1f}) scale(0.62) translate({-xg:.1f},{-yg:.1f})">' + head(xg, yg, True) + stem(xg, yg, 26)[0] + flag(xg + 5.4, yg - 26, 1) + '</g>'
    slash = f'<line x1="{xg+2:.1f}" y1="{yg-9:.1f}" x2="{xg+9:.1f}" y2="{yg-15:.1f}" stroke="#000" stroke-width="1.2"/>'
    s, xs, yt = stem(xc, y)
    return g + slash + head(xc, y, True) + s, 32, xc
def d_sharp(x, top, pos):
    y = pos_y(top, pos); xc = x + 16
    s, xs, yt = stem(xc, y)
    return music_text(x + 1, y + 4, '♯', 22) + head(xc, y, True) + s, 26, xc
def d_flat(x, top, pos):
    y = pos_y(top, pos); xc = x + 16
    s, xs, yt = stem(xc, y)
    return music_text(x + 1, y + 3, '♭', 22) + head(xc, y, True) + s, 26, xc

# key: (display name, duration in quarter beats, drawer)
TYPES = {
 'whole':            ('the whole note', 4, d_whole),
 'half':             ('the half note', 2, d_half),
 'dotted_half':      ('the dotted half note', 3, d_dotted_half),
 'quarter':          ('the quarter note', 1, d_quarter),
 'dotted_quarter':   ('the dotted quarter note', 1.5, d_dotted_quarter),
 'eighth':           ('the single eighth note', 0.5, d_eighth),
 'dotted_eighth':    ('the dotted eighth note', 0.75, d_dotted_eighth),
 'sixteenth':        ('the single sixteenth note', 0.25, d_sixteenth),
 'eighth_pair':      ('the pair of beamed eighth notes', 1, d_eighth_pair),
 'triplet':          ('the eighth-note triplet', 1, d_triplet),
 'sixteenth_quad':   ('the run of four beamed sixteenths', 1, d_sixteenth_quad),
 'sixteenth_pair':   ('the pair of beamed sixteenths', 0.5, d_sixteenth_pair),
 'dotted_eighth_sixteenth': ('the dotted eighth and sixteenth (the gallop)', 1, d_dotted_eighth_sixteenth),
 'whole_rest':       ('the whole rest', 4, d_whole_rest),
 'half_rest':        ('the half rest', 2, d_half_rest),
 'quarter_rest':     ('the quarter rest', 1, d_quarter_rest),
 'eighth_rest':      ('the eighth rest', 0.5, d_eighth_rest),
 'sixteenth_rest':   ('the sixteenth rest', 0.25, d_sixteenth_rest),
 'tie':              ('the two tied quarter notes', 2, d_tie),
 'chord':            ('the two-note chord', 1, d_chord),
 'fermata':          ('the note with a fermata', 1, d_fermata),
 'staccato':         ('the staccato note', 1, d_staccato),
 'accent':           ('the accented note', 1, d_accent),
 'grace':            ('the grace note', 1, d_grace),
 'sharp':            ('the sharpened note', 1, d_sharp),
 'flat':             ('the flattened note', 1, d_flat),
}
GLYPH_WIDTH = {k: TYPES[k][2](0, 0, 2)[1] for k in TYPES}

def staff(x, top, width):
    return ''.join(f'<line x1="{x}" y1="{top + i*SP}" x2="{x+width}" y2="{top + i*SP}" stroke="#000" stroke-width="1"/>' for i in range(5))

def clef_and_time(x, top, beats):
    s = music_text(x + 2, top + 3 * SP, '\U0001D11E', 34)
    s += f'<text x="{x+38}" y="{top+2*SP-1}" font-family="Old Standard TT" font-weight="700" font-size="21" text-anchor="middle">{beats}</text>'
    s += f'<text x="{x+38}" y="{top+4*SP-1}" font-family="Old Standard TT" font-weight="700" font-size="21" text-anchor="middle">4</text>'
    return s

def barline(x, top, final=False):
    if final:
        return f'<line x1="{x-4}" y1="{top}" x2="{x-4}" y2="{top+STAFF_H}" stroke="#000" stroke-width="1"/><line x1="{x}" y1="{top}" x2="{x}" y2="{top+STAFF_H}" stroke="#000" stroke-width="3.5"/>'
    return f'<line x1="{x}" y1="{top}" x2="{x}" y2="{top+STAFF_H}" stroke="#000" stroke-width="1.1"/>'

def label(xc, top, num):
    return f'<text x="{xc:.1f}" y="{top-40:.1f}" font-family="Old Standard TT" font-weight="700" font-size="10.5" text-anchor="middle">{num}</text>'

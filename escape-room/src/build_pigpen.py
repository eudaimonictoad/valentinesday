# Pigpen (Freemason's) cipher: key sheet for Sarah, and an encoder for the game-master.
#   python3 build_pigpen.py                 -> html/09-pigpen-key.html
#   python3 build_pigpen.py "YOUR MESSAGE"  -> html/pigpen-message.html (the message drawn in pigpen glyphs)
import sys
from common import *

GRID1 = 'ABCDEFGHI'; GRID2 = 'JKLMNOPQR'; X1 = 'STUV'; X2 = 'WXYZ'

def glyph(letter, x, y, s=26, sw=2.2):
    """SVG for one pigpen glyph with its top-left at (x, y) and side length s."""
    L = letter.upper(); out = []
    line = lambda x1, y1, x2, y2: out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="{sw}" stroke-linecap="square"/>')
    dot = lambda: out.append(f'<circle cx="{x+s/2:.1f}" cy="{y+s/2:.1f}" r="{s*0.09:.1f}" fill="#000"/>')
    if L in GRID1 or L in GRID2:
        i = (GRID1 + GRID2).index(L) % 9; r, c = divmod(i, 3)
        if r > 0: line(x, y, x + s, y)
        if r < 2: line(x, y + s, x + s, y + s)
        if c > 0: line(x, y, x, y + s)
        if c < 2: line(x + s, y, x + s, y + s)
        if L in GRID2: dot()
    elif L in X1 or L in X2:
        i = (X1 + X2).index(L) % 4; cx, cy = x + s / 2, y + s / 2
        if i == 0:   line(x, y, cx, cy); line(cx, cy, x + s, y)              # S/W : V shape
        elif i == 1: line(x, y, cx, cy); line(cx, cy, x, y + s)              # T/X : > shape
        elif i == 2: line(x + s, y, cx, cy); line(cx, cy, x + s, y + s)      # U/Y : < shape
        else:        line(x, y + s, cx, cy); line(cx, cy, x + s, y + s)      # V/Z : ^ shape
        if L in X2: dot()
    return ''.join(out)

def key_figure(x, y, cell=44):
    """The classic key: two 3x3 grids and two X's, letters inside."""
    out = []
    for gi, (letters, dotted) in enumerate(((GRID1, False), (GRID2, True))):
        gx = x + gi * (cell * 3 + 40)
        for i in range(1, 3):
            out.append(f'<line x1="{gx + i*cell}" y1="{y}" x2="{gx + i*cell}" y2="{y + 3*cell}" stroke="#000" stroke-width="2.5"/>')
            out.append(f'<line x1="{gx}" y1="{y + i*cell}" x2="{gx + 3*cell}" y2="{y + i*cell}" stroke="#000" stroke-width="2.5"/>')
        for i, L in enumerate(letters):
            r, c = divmod(i, 3)
            out.append(f'<text x="{gx + c*cell + cell/2}" y="{y + r*cell + cell/2 + 1}" text-anchor="middle" dominant-baseline="central" font-family="Libre Baskerville" font-weight="700" font-size="20">{L}</text>')
            if dotted:
                out.append(f'<circle cx="{gx + c*cell + cell/2}" cy="{y + r*cell + cell - 8}" r="3" fill="#000"/>')
    for xi, (letters, dotted) in enumerate(((X1, False), (X2, True))):
        xx = x + 2 * (cell * 3 + 40) + xi * (cell * 3 + 40); size = 3 * cell
        out.append(f'<line x1="{xx}" y1="{y}" x2="{xx + size}" y2="{y + size}" stroke="#000" stroke-width="2.5"/>')
        out.append(f'<line x1="{xx + size}" y1="{y}" x2="{xx}" y2="{y + size}" stroke="#000" stroke-width="2.5"/>')
        pos = [(size/2, size*0.22), (size*0.2, size/2), (size*0.8, size/2), (size/2, size*0.8)]
        for L, (px, py) in zip(letters, pos):
            out.append(f'<text x="{xx + px}" y="{y + py}" text-anchor="middle" dominant-baseline="central" font-family="Libre Baskerville" font-weight="700" font-size="20">{L}</text>')
            if dotted:
                out.append(f'<circle cx="{xx + px + 16}" cy="{y + py + 9}" r="3" fill="#000"/>')
    return ''.join(out)

def alphabet_table(x, y, cols=13, cell=48):
    out = []
    for i, L in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        r, c = divmod(i, cols)
        gx = x + c * cell; gy = y + r * (cell + 30)
        out.append(glyph(L, gx + 11, gy, 26))
        out.append(f'<text x="{gx + 24}" y="{gy + 48}" text-anchor="middle" font-family="IM Fell DW Pica SC" font-size="15">{L}</text>')
    return ''.join(out)

def message_svg(text, s=22, gap=8, per_line=22, annotate=False):
    """Draw a message in pigpen glyphs; spaces become gaps, other characters are kept as text."""
    words = text.upper().split(' ')
    lines = []; cur = []
    for w in words:
        if sum(len(x) + 1 for x in cur) + len(w) > per_line and cur:
            lines.append(cur); cur = []
        cur.append(w)
    if cur: lines.append(cur)
    out = []; y = 10 if not annotate else 22
    for ln in lines:
        x = 10
        for w in ln:
            for ch in w:
                if ch.isalpha():
                    out.append(glyph(ch, x, y, s, 2))
                else:
                    out.append(f'<text x="{x + s/2}" y="{y + s*0.8}" text-anchor="middle" font-family="Libre Baskerville" font-weight="700" font-size="{s}">{esc(ch)}</text>')
                if annotate:
                    out.append(f'<text x="{x + s/2}" y="{y - 5}" text-anchor="middle" font-family="Old Standard TT" font-size="{s*0.5:.1f}" fill="#777">{esc(ch)}</text>')
                x += s + gap
            x += s * 0.9
        y += s + (26 if not annotate else 34)
    return f'<svg viewBox="0 0 {per_line*(s+gap)+60} {y}" width="{per_line*(s+gap)+60}" height="{y}" xmlns="http://www.w3.org/2000/svg">{"".join(out)}</svg>'

CSS = """
.fig { display: block; margin: 8px auto; }
.cap { text-align: center; font-style: italic; font-size: 10.5pt; margin: 2px 0 10px; }
.preface { font-size: 10.5pt; text-align: justify; margin: 6px 0; }
.sc2 { font-family: 'IM Fell DW Pica SC'; font-size: 13pt; letter-spacing: 0.1em; text-align: center; margin-top: 10px; }
.msg { border: 1px solid #000; padding: 16px 12px; margin: 12px 0; text-align: center; }
"""

def build():
    body = f"""<div class="page">
{masthead("The Pig-Pen Alphabet", 'A Key to the Cipher of the Freemasons, the Rosicrucians, and Schoolchildren', 'Pocket Library Series · No. 4')}
<p class="preface">Each letter is written not by its name but by the shape of the pen it lives in. Find the letter in one of the four figures below and draw the lines that enclose it, and nothing else; the dot marks the second set. To read a message, do the same in reverse: match the shape to its pen, and take the letter that sits in it. The alphabet is set out in full underneath for the impatient.</p>
<svg class="fig" viewBox="0 0 690 140" width="690" height="140" xmlns="http://www.w3.org/2000/svg">{key_figure(4, 4)}</svg>
<div class="cap">The four pens. Left to right: letters A to I, letters J to R (dotted), S to V, W to Z (dotted).</div>
<div class="sc2">The Alphabet in Full</div>
<svg class="fig" viewBox="0 0 640 170" width="640" height="170" xmlns="http://www.w3.org/2000/svg">{alphabet_table(8, 8)}</svg>
<div class="sc2">For Practice</div>
<div class="cap">The line below reads: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG</div>
<div style="text-align:center">{message_svg('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 20, 6, 26)}</div>
<div class="foot">Pocket Library Series · The Pig-Pen Alphabet</div>
</div>"""
    write_page('09-pigpen-key', body, 'The Pig-Pen Alphabet', CSS)

def build_message(text):
    """Game-master tracing sheet: each glyph drawn full size with its letter above it."""
    body = f"""<div class="page">
{masthead('The Wall', 'Trace these shapes in invisible ink', 'Game-master copy · not for Sarah · remove before she arrives')}
<p class="preface">Write <b>ALIEN BLUES</b> above these in dry-erase marker, then copy the shapes below beneath it in the invisible-ink pen. The small grey letter over each shape is what that shape means; do not copy the letters, only the shapes. Leave a clear gap between words.</p>
<div class="msg">{message_svg(text, 26, 10, 12, annotate=True)}</div>
<p class="small center">Reads: <b>{esc(text.upper())}</b></p>
<div class="foot">Game-master copy · The Wall</div>
</div>"""
    write_page('pigpen-message', body, 'Wall message to trace', CSS)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        build_message(' '.join(sys.argv[1:]))
    else:
        build()

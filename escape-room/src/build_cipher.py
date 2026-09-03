import math
from common import *
from cipher_data import *

def pol(cx, cy, r, a):
    t = math.radians(a)
    return cx + r * math.sin(t), cy - r * math.cos(t)

def dial_svg(cx=350, cy=350):
    R = 345
    s = []
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="2.5"/>')
    for r, w in ((326, 1), (296, 1.5), (245, 1)):
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#000" stroke-width="{w}"/>')
    # minute ticks and hour ticks
    for m in range(60):
        a = m * 6
        long = (m % 5 == 0)
        x1, y1 = pol(cx, cy, 296, a); x2, y2 = pol(cx, cy, 296 - (10 if long else 5), a)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="{2 if long else 0.8}"/>')
    # clock numerals, upright like a clock face
    for n in range(1, 13):
        x, y = pol(cx, cy, 311, n * 30)
        s.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Old Standard TT" font-weight="700" font-size="21">{n}</text>')
    # slot dividers and symbols on the symbol band
    for k in range(N):
        a = k * 10 + 5
        x1, y1 = pol(cx, cy, 245, a); x2, y2 = pol(cx, cy, 296, a)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="0.7"/>')
    for k in range(N):
        a = k * 10
        x, y = pol(cx, cy, 270, a)
        s.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central" transform="rotate({a} {x:.1f} {y:.1f})" font-family="Libre Baskerville" font-weight="700" font-size="23">{OUTER[k]}</text>')
    # rim inscription along the outer band
    s.append(f'<defs><path id="rim" d="M {cx - 336},{cy} a 336,336 0 1,1 672,0 a 336,336 0 1,1 -672,0"/></defs>')
    rim = '· SET THE HOUR · FIND IT WITHOUT · READ IT WITHIN ' * 2 + '· SET THE HOUR · FIND IT WITHOUT · READ IT WITHIN'
    s.append(f'<text font-family="IM Fell DW Pica SC" font-size="12.5" letter-spacing="2" textLength="2100" lengthAdjust="spacing"><textPath href="#rim" startOffset="0">{rim}</textPath></text>')
    # centre mark
    s.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="none" stroke="#000" stroke-width="1"/><line x1="{cx-9}" y1="{cy}" x2="{cx+9}" y2="{cy}" stroke="#000" stroke-width="0.8"/><line x1="{cx}" y1="{cy-9}" x2="{cx}" y2="{cy+9}" stroke="#000" stroke-width="0.8"/>')
    s.append(f'<text x="{cx}" y="{cy-60}" text-anchor="middle" font-family="IM Fell DW Pica SC" font-size="15" letter-spacing="3">PLATE I · THE DIAL</text>')
    s.append(f'<text x="{cx}" y="{cy+70}" text-anchor="middle" font-family="IM Fell English" font-style="italic" font-size="12">Plate II turns upon this centre.</text>')
    return ''.join(s)

def hands_svg(cx=350, cy=350, rotation=0, with_labels=True):
    R = 240
    s = [f'<g transform="rotate({rotation} {cx} {cy})">']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="2.5"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="196" fill="none" stroke="#000" stroke-width="1.2"/>')
    for k in range(N):
        a = k * 10 + 5
        x1, y1 = pol(cx, cy, 196, a); x2, y2 = pol(cx, cy, R, a)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="0.7"/>')
    for k in range(N):
        a = k * 10
        x, y = pol(cx, cy, 218, a)
        s.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central" transform="rotate({a} {x:.1f} {y:.1f})" font-family="Libre Baskerville" font-weight="700" font-size="23">{INNER[k]}</text>')
    # hands: hour (short, broad) and minute (long, slender), drawn as filled polygons pointing outward
    def hand(angle, length, width):
        tip = pol(cx, cy, length, angle)
        l = pol(cx, cy, width, angle - 90); r = pol(cx, cy, width, angle + 90)
        tail = pol(cx, cy, 22, angle + 180)
        return f'<polygon points="{tail[0]:.1f},{tail[1]:.1f} {l[0]:.1f},{l[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} {r[0]:.1f},{r[1]:.1f}" fill="#000"/>'
    s.append(hand(HAND_HOUR, 150, 9))
    s.append(hand(HAND_MINUTE, 190, 5))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#000"/><circle cx="{cx}" cy="{cy}" r="3" fill="#fff"/>')
    if with_labels:
        # labels placed away from the hands
        s.append(f'<text x="{cx}" y="{cy+110}" text-anchor="middle" font-family="IM Fell DW Pica SC" font-size="14" letter-spacing="2">PLATE II · THE HANDS</text>')
        s.append(f'<text x="{cx}" y="{cy+135}" text-anchor="middle" font-family="IM Fell English" font-style="italic" font-size="11">Cut round the edge. Pin at the centre.</text>')
    s.append('</g>')
    return ''.join(s)

CSS = """
.plate { text-align: center; }
.plate svg { width: 7.3in; height: 7.3in; display: block; margin: 0 auto; }
.plate .cap { font-family: 'IM Fell DW Pica SC'; letter-spacing: 0.15em; font-size: 11pt; margin-top: 6px; }
.plate .note { font-style: italic; font-size: 10pt; }
.sol td, .sol th { border: 1px solid #000; padding: 2px 6px; font-family: 'Old Standard TT', serif; font-size: 10pt; text-align: center; }
.sol { border-collapse: collapse; margin: 6px auto; }
.box { border: 1px solid #000; padding: 8px 12px; font-size: 10pt; margin: 8px 0; }
"""

def build():
    body = f"""
<div class="page plate">
<div class="masthead"><div class="title">The Horological Cipher</div><div class="sub">Plate I of II · The Dial</div></div>
<svg viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg">{dial_svg()}</svg>
<div class="note">Cut round the outermost edge. The second plate turns upon the centre mark.</div>
</div>
<div class="page plate">
<div class="masthead"><div class="title">The Horological Cipher</div><div class="sub">Plate II of II · The Hands</div></div>
<svg viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg">{hands_svg()}</svg>
<div class="note">Cut round the edge and fasten upon the centre of Plate I with a pin, so that it turns freely. Set the hour.</div>
</div>"""
    write_page('02-cipher-wheel', body, 'The Horological Cipher', CSS)

    # solution sheet for the game-master only
    m = OUTER_TO_INNER
    rows = ''.join(f'<tr><td>{o}</td><td>{m[o]}</td></tr>' for o in SYMBOLS)
    # split into 3 side-by-side tables
    cols = [SYMBOLS[i::3] for i in range(3)]
    tables = ''.join('<table class="sol"><tr><th>Dial</th><th>Hands</th></tr>' + ''.join(f'<tr><td>{o}</td><td>{m[o]}</td></tr>' for o in c) + '</table>' for c in cols)
    sample = 'LOOK BEHIND THE MIRROR AT 3 30'
    body = f"""
<div class="page">
<div class="masthead"><div class="title">Cipher Solution Sheet</div><div class="sub">For the game-master only · do not print for Sarah</div></div>
<div class="box"><b>How it works.</b> Plate II (the hands) is pinned on top of Plate I (the dial) and turned until the hands read <b>{SOLUTION_TIME}</b> on the dial's clock numerals: the long hand exactly on the 6, the short hand halfway between the 3 and the 4. That is a turn of {ROT}° clockwise from the printed position. The rim of the dial says <i>find it without, read it within</i>: a secret message is written in <b>dial symbols</b>; for each one, find it on the outer dial and read the symbol lined up with it on the inner disc. Letters and digits both take part, so you can hide a number, a time, or a word.</div>
<div style="display:flex;gap:10px;justify-content:center;align-items:flex-start;">
<svg viewBox="0 0 700 700" style="width:3.4in;height:3.4in" xmlns="http://www.w3.org/2000/svg">{dial_svg()}{hands_svg(rotation=ROT, with_labels=False)}</svg>
<div style="display:flex;gap:6px">{tables}</div>
</div>
<div class="box"><b>Example.</b> Plain: <span style="font-family:'Old Standard TT'">{sample}</span><br>Written for Sarah (dial symbols): <span style="font-family:'Old Standard TT';font-size:13pt;letter-spacing:2px">{encode(sample)}</span><br>
To make your own: <code>python3 escape-room/src/cipher_data.py YOUR MESSAGE HERE</code></div>
<div class="box small">Plate II's hands are deliberately printed at an angle that reads as no sensible time; only when turned {ROT}° do they show {SOLUTION_TIME}. If you would rather a different answer, change SOLUTION_TIME, HOUR_ANGLE, MINUTE_ANGLE and ROT in <code>src/cipher_data.py</code> (ROT must be a multiple of 10) and rebuild.</div>
</div>"""
    write_page('02-cipher-wheel-SOLUTION-gamemaster-only', body, 'Cipher Solution Sheet', CSS)

if __name__ == '__main__':
    build()

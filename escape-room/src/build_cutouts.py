from common import *
from cipher_data import encode

# Everything that used to be "write this on a scrap of paper" in the setup guide.
# The cipher card especially: one mistyped character and the last lock never opens,
# so it is generated straight from cipher_data rather than copied by hand.

PLAIN = 'BEHIND THE MANY FACES'
CARD = encode(PLAIN)
ENVELOPE = 'This will mean nothing until the hour is set.'
HINTS = [
    'If you are stuck on the music',
    'If you are stuck on the knife',
    'If you are stuck at the very end',
]
SLIP = ('Everything you need is at sarahs.quest/hints.html '
        '&mdash; and I will not think less of you.')

CSS = """
h3 { font-family: 'IM Fell DW Pica SC'; font-size: 11.5pt; letter-spacing: 0.1em;
     border-bottom: 1px solid #000; margin: 14px 0 3px; }
h3 .n { font-style: italic; font-family: 'IM Fell English'; letter-spacing: 0;
        text-transform: none; font-size: 9.5pt; }
.row { display: flex; gap: 0.3in; margin-top: 7px; }
.row.three > * { flex: 1; }
.cut { border: 1px dashed #000; padding: 13px 16px; text-align: center; }
.cipher { font-family: 'Old Standard TT'; font-weight: 700; font-size: 21pt;
          letter-spacing: 0.16em; white-space: nowrap; }
.cipher-card { flex: 1; padding: 22px 10px; }
.label { font-size: 12.5pt; font-style: italic; }
.hintlab { font-family: 'IM Fell DW Pica SC'; font-size: 11pt; letter-spacing: 0.05em; padding: 15px 8px; }
.slip { font-size: 10.5pt; font-style: italic; padding: 13px 10px; }
.note { font-size: 9.4pt; margin: 3px 0 0; color: #000; }
.note b { font-family: 'IM Fell DW Pica SC'; font-weight: normal; letter-spacing: 0.05em; }
"""


def build():
    body = f"""<div class="page">
{masthead('Cut-Outs', 'The cipher card, and the labels for four envelopes',
          'Game-master&rsquo;s sheet · none of this is written by hand')}

<h3>The cipher card <span class="n">&mdash; into a small envelope, just inside the meditation cushion&rsquo;s zip</span></h3>
<p class="note">Printed rather than copied: one wrong character here and the last lock never opens.
The second card is a spare. What it decodes to is on your solution sheet, not on this one &mdash; an offcut
of this page should never be able to give the ending away.</p>
<div class="row">
  <div class="cut cipher-card"><div class="cipher">{CARD}</div></div>
  <div class="cut cipher-card"><div class="cipher">{CARD}</div></div>
</div>

<h3>That envelope <span class="n">&mdash; glue or copy this onto the front</span></h3>
<div class="row">
  <div class="cut" style="flex:1"><div class="label">{ENVELOPE}</div></div>
  <div class="cut" style="flex:1"><div class="label">{ENVELOPE}</div></div>
</div>

<h3>Three hint envelopes <span class="n">&mdash; optional, and they save the evening</span></h3>
<p class="note">Seal three envelopes, label them with these, and leave them somewhere she will find them
if she needs them. The same slip goes inside each.</p>
<div class="row three">
  {''.join(f'<div class="cut hintlab">{h}</div>' for h in HINTS)}
</div>
<div class="row three">
  {''.join(f'<div class="cut slip">{SLIP}</div>' for _ in HINTS)}
</div>

<div class="foot">Cut-Outs · the cipher card and four envelopes</div>
</div>"""
    write_page('15-cutouts', body, 'Cut-Outs', CSS)


if __name__ == '__main__':
    build()

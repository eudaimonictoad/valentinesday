import json, random
from common import *
from content_names import NAMES, KEEPSAKES

CSS = """
.cols3 { column-count: 3; column-gap: 0.22in; column-rule: 1px solid #000; }
.nm { break-inside: avoid; font-size: 8.6pt; line-height: 1.22; margin-bottom: 3.5px; text-align: left; }
.nm .h { font-family: 'IM Fell DW Pica SC'; font-size: 9.6pt; letter-spacing: 0.03em; }
.nm .o { font-style: italic; }
.nm .k { font-family: 'Old Standard TT'; font-size: 8.2pt; }
.preface { font-size: 10pt; text-align: justify; margin: 4px 0 6px; }
.letter { font-family: 'UnifrakturMaguntia'; font-size: 15pt; break-after: avoid; margin-top: 3px; }
"""

def build():
    cfg = json.load(open(os.path.join(ROOT, 'src', 'config.json')))
    special = {'Patricia': cfg['patricia_keepsake'], 'Chloe': cfg['chloe_keepsake'], 'Shirley': cfg.get('shirley_keepsake', 'a bright meadow'), 'Sarah': cfg.get('sarah_keepsake', "the author's whole heart")}
    rng = random.Random(1887)
    pool = [k for k in KEEPSAKES if k not in special.values()]
    rng.shuffle(pool)
    entries = []; last = ''
    for i, (name, origin, meaning) in enumerate(sorted(NAMES)):
        keep = special.get(name, pool[i % len(pool)])
        letter = ''
        if name[0] != last:
            last = name[0]; letter = f'<div class="letter">{last}</div>'
        entries.append(f'{letter}<div class="nm"><span class="h">{esc(name)}</span> <span class="o">({esc(origin)})</span> {esc(meaning)}. <span class="k">Keepsake: {esc(keep)}.</span></div>')
    body = f"""<div class="page">
{masthead('A Register of Feminine Names', 'Their Origins, their Meanings, and the Keepsake proper to each', 'Compiled for the use of Godparents, Registrars, and the Curious · Third Edition, Enlarged')}
<p class="preface">It is an old custom, now nearly forgotten, that every given name carries with it a keepsake: a small object which the bearer of the name is said to be lucky in, and which those who love her are wise to look to. This register sets down, for {len(NAMES)} names in common use, the tongue from which each is drawn, its meaning, and its keepsake. The compiler makes no claims for the custom beyond its antiquity, and one exception for its accuracy.</p>
<div class="cols3">{''.join(entries)}</div>
</div>"""
    write_page('06-register-of-names', body, 'A Register of Feminine Names', CSS)

if __name__ == '__main__':
    build()

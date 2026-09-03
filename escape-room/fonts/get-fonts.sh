#!/usr/bin/env bash
# Re-downloads the Google Fonts used by the printables into this folder (run once before building).
set -e
cd "$(dirname "$0")"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
python3 - "$UA" <<'PY'
import re, subprocess, sys, os
UA = sys.argv[1]
fams = ["IM+Fell+English:ital@0;1", "IM+Fell+DW+Pica+SC", "IM+Fell+English+SC", "UnifrakturMaguntia",
        "Old+Standard+TT:ital,wght@0,400;0,700;1,400", "Special+Elite", "Noto+Music",
        "Libre+Baskerville:ital,wght@0,400;0,700;1,400", "Rye", "Pinyon+Script"]
out = []
for fam in fams:
    css = subprocess.run(['curl', '-sS', '-A', UA, f'https://fonts.googleapis.com/css2?family={fam}&display=swap'], capture_output=True, text=True, check=True).stdout
    for sub, body in re.findall(r'/\* (\w[\w-]*) \*/\s*@font-face \{(.*?)\}', css, re.S):
        if sub not in ('latin', 'music'): continue
        url = re.search(r'url\((https://[^)]+)\)', body).group(1)
        name = re.search(r"font-family: '([^']+)'", body).group(1)
        sty = re.search(r"font-style: (\w+)", body).group(1)
        wt = re.search(r"font-weight: (\d+)", body).group(1)
        fn = f"{name.replace(' ', '')}-{sty}-{wt}-{sub}.woff2"
        if not os.path.exists(fn):
            subprocess.run(['curl', '-sS', '-o', fn, url], check=True)
        out.append(f"@font-face{{font-family:'{name}';font-style:{sty};font-weight:{wt};src:url('{fn}') format('woff2');}}")
open('fonts.css', 'w').write('\n'.join(out))
print(len(out), 'font faces ready')
PY

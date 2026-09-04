# Rebuild every printable: python3 escape-room/src/build_all.py   (then: node escape-room/render.js)
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_knives, build_cipher, build_songbook, build_celebs, build_recipes, build_names, build_cards, build_concordance, build_mapping, build_pigpen
for m in (build_knives, build_cipher, build_songbook, build_celebs, build_recipes, build_names, build_cards, build_concordance, build_mapping, build_pigpen):
    m.build()
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subprocess.run(['node', os.path.join(root, 'render.js')], check=True)

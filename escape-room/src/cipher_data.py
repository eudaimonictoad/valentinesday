# Shared definitions for the horological cipher wheel.
import random, string
SYMBOLS = list(string.ascii_uppercase) + list('0123456789')   # 36 slots, 10 degrees each
N = len(SYMBOLS)
SEED = 3330
_r = random.Random(SEED)
OUTER = SYMBOLS[:]; _r.shuffle(OUTER)      # symbols printed on the dial (outer plate), slot k at angle 10k
INNER = SYMBOLS[:]; _r.shuffle(INNER)      # symbols printed on the hands disc (inner plate), slot k at angle 10k in its own frame
SOLUTION_TIME = '3:30'
HOUR_ANGLE, MINUTE_ANGLE = 105, 180        # where the hands must point on the dial at 3:30 (degrees clockwise from 12)
ROT = 200                                   # the inner disc must be turned 200 degrees clockwise to read 3:30
ROT_SLOTS = ROT // 10
# hands are printed on the inner disc at these angles in the disc's own frame
HAND_HOUR = (HOUR_ANGLE - ROT) % 360
HAND_MINUTE = (MINUTE_ANGLE - ROT) % 360

def mapping():
    """Returns dict outer_symbol -> inner_symbol when the wheel is set to SOLUTION_TIME."""
    m = {}
    for k in range(N):
        m[OUTER[(k + ROT_SLOTS) % N]] = INNER[k]
    return m

OUTER_TO_INNER = mapping()
INNER_TO_OUTER = {v: k for k, v in OUTER_TO_INNER.items()}

def encode(plaintext):
    """Plaintext -> cipher text. The cipher text is written in DIAL (outer) symbols.
    To read it, Sarah finds each symbol on the dial and reads the symbol beneath it on the hands disc."""
    out = []
    for ch in plaintext.upper():
        out.append(INNER_TO_OUTER.get(ch, ch))
    return ''.join(out)

def decode(ciphertext):
    return ''.join(OUTER_TO_INNER.get(ch, ch) for ch in ciphertext.upper())

if __name__ == '__main__':
    import sys
    text = ' '.join(sys.argv[1:]) or 'THE KEY IS UNDER THE PLANT 3 30'
    enc = encode(text)
    print('plain :', text.upper())
    print('cipher:', enc)
    assert decode(enc) == text.upper()

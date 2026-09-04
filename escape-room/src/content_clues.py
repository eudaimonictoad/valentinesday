# The six painting-back clues, in one place.
# build_frames.py prints them onto cards; build_mapping.py lists them in the setup
# guide. Both read this, so the printed card and the guide can never disagree.
# `label` is for Ben only and is printed OUTSIDE the cut line, to be trimmed off.
# Labels are plain text (they get upper-cased), so no HTML entities in them.

CLUES = [
    ('Milk Crate',
     'The famous man we always see here, who is not him.'),
    ('Patricia’s',
     'Just the name. Look her up.'),
    ('Hamlet',
     'We saw the film of this play. Whose film was it? Look her up by her first name.'),
    ('Fairy houses',
     'What was the family name of the one who lived here? Look her up.'),
    ('Abyssinia',
     'This country has another name now. Find its colours at sarahs.quest, and turn them over.'),
    ('Gleaners',
     'The caf&eacute; sits in a market named for a country. Its colours are at sarahs.quest too. '
     'You will need this one and Abyssinia both.'),
]

assert len(CLUES) == 6, 'there are six paintings and six clues'

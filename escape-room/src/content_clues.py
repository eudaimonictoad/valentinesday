# The six painting-back clues, in one place.
# build_frames.py prints them onto cards; build_mapping.py lists them in the setup
# guide. Both read this, so the printed card and the guide can never disagree.
# `label` is for Ben only and is printed OUTSIDE the cut line, to be trimmed off.
# Labels are plain text (they get upper-cased), so no HTML entities in them.
#
# The clue text is raw HTML: <span class="url"> makes the address stand out on the
# printed card. Every clue that needs the website says the whole address, because
# she has no reason to guess at it.

URL = '<span class="url">www.sarahs.quest</span>'

CLUES = [
    ('Milk Crate',
     'The famous man we always see here, who is not him.'),

    ('Patricia’s',
     'Just the name. Look her up in the Register of Names.'),

    # Was "Whose film was it?" — too coy for a director she does not know by name.
    ('Hamlet',
     'We saw the film named for this play&rsquo;s son. Who directed it? '
     'Take her first name to the Register of Names.'),

    # Was "the family name of the one who lived here" — she has no way in without
    # the first name to hang it on.
    ('Fairy houses',
     'Her first name was Cardellia. What was her last name? '
     'Take that to the Register of Names.'),

    # Injera is the staple of both Ethiopian and Eritrean cooking, so the coffee
    # settles which one is meant — and no Eritrean flag hangs in the Hall anyway.
    ('Abyssinia',
     'The food here is eaten with your hands, torn from a soft round of injera. '
     'Coffee was born here too. Which country is it? '
     f'Find its colours at {URL} and turn them over.'),

    ('Gleaners',
     'This caf&eacute; stands in a market named after a country. Which one? '
     f'Its colours are at {URL} as well. '
     'You will need this painting and the injera one both.'),
]

assert len(CLUES) == 6, 'there are six paintings and six clues'

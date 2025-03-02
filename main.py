#!/home/biscuit/anaconda3/bin/python

import genanki
import wanikani_api.client as client
import random
import time

def sepStr(meanings):
    ret = ""
    for m in meanings:
        ret += m.meaning + ',\n'
    ret = ret.rstrip(',\n')
    return ret

wk_api = client.Client("77606c85-cacc-4a2d-8774-5d8462d56710")
assignments = wk_api.assignments(subject_types = "vocabulary", 
                                 started = True, burned = False, fetch_all = True)

my_model = genanki.Model(
    1242844797,
    'WaniKani',
    fields = [
        {'name': 'Word'},
        {'name': 'Reading'},
    ],
    templates = [
        {
            'name': 'Card',
            'qfmt': '{{Word}}',
            'afmt': '{{FrontSide}}<hr id="reading">{{Reading}}'
        }
    ]
)

my_deck = genanki.Deck(
    1582307016,
    'WaniKani Reverse'
)
print(len(assignments))

i = 0
for assignment in assignments:
    i += 1
    if (i == 55):
        i = 0
        print("Sleeping")
        time.sleep(62)
    new_note = genanki.Note(
        model = my_model,
        fields = [sepStr(assignment.subject.meanings), assignment.subject.characters]
    )
    my_deck.add_note(new_note)

genanki.Package(my_deck).write_to_file('wanikani.apkg')

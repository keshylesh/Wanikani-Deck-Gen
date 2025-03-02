import genanki
import wanikani_api.client as client
import random
import time

wk_api = client.Client("77606c85-cacc-4a2d-8774-5d8462d56710")
assignments = wk_api.assignments(subject_types = "vocabulary", 
                                 started = True, burned = False, fetch_all = True)

my_model = genanki.Model(
    1252164487,
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
    1938304362,
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
        fields = [assignment.subject.meanings[0].meaning, assignment.subject.characters]
    )
    my_deck.add_note(new_note)

genanki.Package(my_deck).write_to_file('wanikani.apkg')

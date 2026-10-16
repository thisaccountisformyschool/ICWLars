
"""
a function receives two stories (strings)
check for words that are used in both stories
return a tuple with all the mutually used words

------------------------------------
Expansion 1 (new function): return a tuple with only words that are used the exact same amount of times
in both stories.
------------------------------------

"""

# def clean_string(to_be_cleaned):
#     pass

# print(clean_string("iets. met?-, veel()() verschillende...! dingen"))




# deze functie ontvangt twee strings, en returnt alle woorden die
# in beide strings zitten als een tupel.
def verwijder_leestekens(scrungled):
    scrungled = scrungled.replace("-"," ")
    scrungled = scrungled.replace("."," ")
    scrungled = scrungled.replace("?"," ")
    scrungled = scrungled.replace("\""," ")
    scrungled = scrungled.replace(","," ")
    scrungled = scrungled.replace("!"," ")
    scrungled = scrungled.replace(":"," ")
    scrungled = scrungled.replace("—"," ")
    return scrungled

def story_comparison(story1, story2):
    story1 = story1.lower()
    story2 = story2.lower()
    story1 = verwijder_leestekens(story1)
    story2 = verwijder_leestekens(story2)
    story1_words = story1.split()
    story2_words = story2.split()
    story2_words = set(story2_words)
    story1_words = set(story1_words)
    mutual_words = story1_words.intersection(story2_words)
    mutual_words = tuple(mutual_words)
    return mutual_words

def story_compare_good(story1,story2):
    story1 = story1.lower()
    story2 = story2.lower()
    leestekens = ".,!\":;?-\'—"
    for leesteken in leestekens:
        story1 = story1.replace(leesteken," ")
        story2 = story2.replace(leesteken," ")

    woorden1 = story1.split()
    woorden2 = story2.split()
    woorden_set1 = set(woorden1)
    woorden_set2 = set(woorden2)
    gemeenschapelijk = woorden_set1.intersection(woorden_set2)
    return tuple(gemeenschapelijk)

def zoek_woord(story):
    story = story.lower()
    leestekens = ".,!\":;?-\'—"
    for leesteken in leestekens:
        story = story.replace(leesteken," ")

    woorden = story.split()
    return woorden

story1 = "In a small, unremarkable town, a pile of generic, everyday junk sat in a cluttered garage. Old papers, tangled cords, forgotten knickknacks—it all gathered dust, untouched for years. One day, the wind howled through a crack in the door, stirring the mess. A single sheet of paper fluttered free, revealing a note scrawled in faded ink: \"You’ll never find it here.\" The wind settled, and the garage returned to silence. Nothing changed—but the note stayed, a mystery lost in the ordinary."
story2 = "In the depths of the galaxy, on a planet made entirely of crystallized sound, the Time Weavers held council. They weren’t beings of flesh, but currents of color and light that spoke through melodies no human ear could grasp. Their task was unthinkable—repair the fabric of reality itself, which had begun to unravel. The problem started when the Fifth Dimension sneezed, causing time to hiccup across the universe. Past and future collided, creating paradoxes that spiraled out of control. A pirate ship from the 18th century crashed into the thought-space of a sleeping star, while dinosaurs wandered the halls of a Martian shopping mall. The Weavers worked tirelessly, stitching moments back together with threads of stardust and memory. But the damage was too great. In a last, desperate move, they summoned the Forgotten Phoenix, a creature of legend who could burn time to ashes and let it be reborn anew. With a cry that sounded like every sunrise and sunset combined, the Phoenix ignited. The universe flickered, then blinked back into perfect order—except for one lingering echo of the pirate ship, forever sailing across the dreams of the stars."
print(story_comparison(story1, story2))
print(story_compare_good(story1, story2))

# expansion 1: enkel woorden die EXACT EVEN VAAK voorkomen in beide verhalen.
def storyComparisonExpansion1(story1, story2):
    gemeenschappelijk = story_compare_good(story1,story2)
    woorden1 = zoek_woord(story1)
    woorden2 = zoek_woord(story2)

    results = []
    for woord in gemeenschappelijk:
        if woorden1.count(woord) == woorden2.count(woord):
            results.append(woord)
    return results
print(storyComparisonExpansion1(story1, story2))


#

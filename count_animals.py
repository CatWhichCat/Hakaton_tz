from collections import defaultdict
import json
from pprint import pprint

with open('animals.json') as f:
    animal_names = json.load(f.read())
# pprint(len(animal_names))

names_count_first_letter = defaultdict(int)
# цикл который считает по букве в списке животных
for names_animals_amount in animal_names:
    names_count_first_letter[names_animals_amount[0]] += 1
# pprint(names_count_first_letter)

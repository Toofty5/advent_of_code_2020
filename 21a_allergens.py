import re
import itertools as it
from collections import defaultdict



lines = [line.strip() for line in open('input', 'r').readlines()]

all_ingredients = set() # there are 200 ingredients
all_allergens = set() # there are 8 allergens

food_list = [] # list of tuples, (ingredients, allergens)

for line in lines:
    ingredients_str, allergens_str = (re.match(r"(.*)\(contains (.*)\)", line)).group(1,2)

    ingredients = set(ingredients_str.split())
    allergens = set(allergens_str.split(', '))
    #print(ingredients)
    #print(allergens)

    food_list.append((ingredients, allergens))

    all_ingredients.update(ingredients)
    all_allergens.update(allergens)

possible_allergens = defaultdict(list)

for ingredients, allergens in food_list:
    for allergen in allergens:
        possible_allergens[allergen].append(ingredients)

for allergen, ingredients in possible_allergens.items():
    possible_allergens[allergen] = set.intersection(*ingredients)

safe_ingredients = all_ingredients.difference(set.union(*(possible_allergens.values())))


known_allergens = set()

while len(known_allergens) < 8:

    for allergen, ingredients in possible_allergens.items():
        candidates = possible_allergens[allergen] - safe_ingredients
        others = [others for others in possible_allergens.values() if others != candidates]
        candidates = candidates.difference(*others, safe_ingredients)

        if len(candidates) == 1:
            possible_allergens[allergen] = candidates
            known_allergens.update(candidates)
            
allergen_string = ','.join([list(possible_allergens[i]).pop() for i in sorted(possible_allergens.keys())])
    

print(allergen_string)

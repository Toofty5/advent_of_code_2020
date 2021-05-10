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

total=0
for ingredients, allergens in food_list:
    for ingredient in ingredients:
        if ingredient in safe_ingredients:
            total += 1

print(total)


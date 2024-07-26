import json
import random
from collections import defaultdict


# Function to select random cats and group them by clan
def select_and_group_cats(cats, num_cats):
    selected_cats = random.sample(cats, num_cats)

    clans = defaultdict(list)
    for cat in selected_cats:
        clans[cat['clan']].append(f"{cat['name']}, {cat['rank']}")

    for clan, members in clans.items():
        print(f"{clan}:")
        for member in members:
            print(member)
        print()


# Load JSON data from finalbattlelist.json
with open('finalbattlelist.json', 'r') as file:
    cats = json.load(file)

# User input
num_cats = int(input("Enter the number of cats to select: "))

# Select and print cats
select_and_group_cats(cats, num_cats)

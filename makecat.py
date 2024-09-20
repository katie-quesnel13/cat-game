import json
import random

from describecat import describe
from cat_creation_methods import get_prefix, get_suffix, random_genestring


def makecat(genes, cat_id):
    appearance = describe(genes)
    prefix = get_prefix(appearance)
    age = int(input("Enter age for new cat: ").strip())
    suffix = get_suffix(prefix, age)
    rank = input("Enter rank for new cat: ").strip()
    if rank == 'Leader':
        suffix = 'star'
    relationships = {
        'dam': None,
        'sire': None,
        'mentor': None,
        'littermates': [],
        'trainees': [],
        'kittens': [],
        'mate': None
    }
    cat_dict = {
        'id': cat_id,
        'prefix': prefix,
        'suffix': suffix,
        'rank': rank,
        'age': age,
        'gender': 'molly' if 'molly' in appearance.lower() else 'tom',
        'living': True,
        'relationships': relationships,
        'genes': genes,
        'description': appearance
    }
    return cat_dict


def main(json_file_path):
    # Open and read the JSON file
    file_name = 'clan.json'
    existing_data = []

    try:
        with open(file_name, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Determine the next ID to use
    if existing_data:
        max_id = max(item['id'] for item in existing_data if 'id' in item)
        next_id = max_id + 1
    else:
        next_id = 1

    print("Format for genes: if it's 3 letters long, make sure longer gene is first. Numbers refer to eye colour:"
          " refraction is first and pigmentation is second. Blue is determined via white present on the cat")
    genes = input(
        "Enter genetic profile for the new cat (e.g., 'LL XOXO BB DD AA McMc SpSp TaTa CC WsWs 1 1') or leave blank for "
        "a random genetic profile: ").strip()
    if genes == "":
        genes = random_genestring()
    new_cat = makecat(genes, next_id)
    print(f"{new_cat['prefix']}{new_cat['suffix']}: {new_cat['rank']}, {new_cat['description']}, {new_cat['age']}"
          f" moons old")
    existing_data.append(new_cat)
    # Write the updated data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)


if __name__ == "__main__":
    # Define the path to your JSON file
    file_path = 'clan.json'

    # Call the main function
    main(file_path)

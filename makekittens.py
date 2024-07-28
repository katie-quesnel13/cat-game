import random
import json
from describecat import describe
from cat_creation_methods import get_prefix


def parse_genetic_profile(profile_string):
    """Parses a genetic profile string into an array of genes and detects inheritable genes."""
    genes = profile_string.split()
    inheritable_genes = []
    for gene in genes:
        if len(gene) == 2:
            inheritable_genes.append((gene[0], gene[1]))
        elif len(gene) == 3:
            inheritable_genes.append((gene[:2], gene[2]))
        elif len(gene) == 4:
            inheritable_genes.append((gene[:2], gene[2:]))
        elif len(gene) == 1:
            inheritable_genes.append(gene)
    return inheritable_genes


def combine_genes(gene_pair_parent1, gene_pair_parent2):
    # Randomly pick one value from each tuple
    gene_parent1 = random.choice(gene_pair_parent1)
    gene_parent2 = random.choice(gene_pair_parent2)

    if gene_parent1.isnumeric():  # if it's an eye colour gene (number) then handle it as eye colour
        lower = min(int(gene_parent1), int(gene_parent2))
        higher = max(int(gene_parent1), int(gene_parent2))
        return str(random.randint(lower, higher))

    # Ensure the longer gene comes first if they have different lengths
    if len(gene_parent1) != len(gene_parent2):
        if len(gene_parent1) > len(gene_parent2):
            combined_gene = gene_parent1 + gene_parent2
        else:
            combined_gene = gene_parent2 + gene_parent1
    else:
        combined_gene = gene_parent1 + gene_parent2
    return combined_gene


def combine_genetic_profiles(d, s):
    """Combines genetic profiles of two parents to create a single offspring genetic profile."""
    parent1_inheritable = parse_genetic_profile(d)
    parent2_inheritable = parse_genetic_profile(s)
    offspring_profile_genes = []

    min_length = min(len(parent1_inheritable), len(parent2_inheritable))

    # Iterate over the length of the shortest list of inheritable genes
    for i in range(min_length):
        gene_pair_parent1 = parent1_inheritable[i]
        gene_pair_parent2 = parent2_inheritable[i]
        offspring_profile_genes.append(combine_genes(gene_pair_parent1, gene_pair_parent2))

    appearance = describe(" ".join(offspring_profile_genes))
    return get_prefix(appearance), " ".join(offspring_profile_genes), appearance


def determine_number_of_offspring():
    """Determines the number of offspring, with a bias towards 2-4."""
    roll = random.random()
    if roll < 0.75:
        # 75% chance for 4 or fewer offspring
        sub_roll = random.random()
        if sub_roll < 0.30:  # 23%ish
            return 3
        elif sub_roll < 0.65:  # 25.5%ish
            return 4
        elif sub_roll < 0.85:  # 15.5%ish
            return 2
        else:  # 11%ish
            return 1
    else:
        # 25% chance for more than 4 offspring
        sub_roll = random.random()
        if sub_roll < 0.55:  # 13%ish
            return 5
        elif sub_roll < 0.78:  # 5.5%ish
            return 6
        elif sub_roll < 0.94:  # 4%ish
            return 7
        else:  # 1%ish
            return 8


def generate_offspring(d, s):
    """Generates a list of offspring genetic profiles."""
    num_offspring = determine_number_of_offspring()
    return [combine_genetic_profiles(d, s) for _ in range(num_offspring)]


keys = ["prefix", "genes", "description", "dam_id", "sire_id"]


def store_litter(litter, d=None, s=None, start_id=1):
    dict_list = []
    ids = list(range(start_id, start_id + len(litter)))  # List of all new IDs
    for idx, inner_list in enumerate(litter):
        # Creating a dictionary for each inner list
        inner_dict = {keys[i]: inner_list[i] for i in range(len(inner_list))}
        inner_dict['suffix'] = 'kit'
        inner_dict['rank'] = 'Kit'
        inner_dict['id'] = start_id + idx
        inner_dict['age'] = 0
        description = inner_list[2]
        inner_dict['gender'] = 'molly' if 'molly' in description.lower() else 'tom'
        inner_dict['living'] = True
        sibling_ids = [id_ for id_ in ids if id_ != ids[idx]]  # Exclude current ID from sibling IDs
        inner_dict['relationships'] = {
            'dam': d,
            'sire': s,
            'mentor': None,
            'littermates': sibling_ids,
            'trainees': [],
            'kittens': [],
            'mate': None
        }
        ordered_dict = {
            'id': inner_dict['id'],
            'prefix': inner_dict['prefix'],
            'suffix': inner_dict['suffix'],
            'rank': inner_dict['rank'],
            'age': inner_dict['age'],
            'gender': inner_dict['gender'],
            'living': inner_dict['living'],
            'relationships': inner_dict['relationships'],
            'genes': inner_dict['genes'],
            'description': inner_dict['description']
        }
        dict_list.append(ordered_dict)
    if d is None:
        d = -1
    if s is None:
        s = -1
    for item in existing_data:
        if int(item['id']) == int(d) or int(item['id']) == int(s):
            for kitten in dict_list:
                if int(item['id']) == int(d):
                    item['relationships']['kittens'].append(kitten['id'])
                if int(item['id']) == int(s):
                    item['relationships']['kittens'].append(kitten['id'])
    return dict_list


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
    next_id = int(max_id) + 1
else:
    next_id = 1

print("Format for genes: if it's 3 letters long, make sure longer gene is first. Numbers refer to eye colour:"
      " refraction is first and pigmentation is second. Blue is determined via white present on the cat. You can instead"
      " use the id of a cat in the clan in place of genetics")
dam = input("Enter genetic profile for dam (e.g., 'LL XOXO BB DD AA McMc SpSp TaTa CC WsWs 1 1'): ").strip()
if dam.isdigit():
    dam_id = int(dam)
    matching_item1 = next((item for item in existing_data if item['id'] == dam_id), None)
    if matching_item1:
        parent1 = matching_item1.get('genes', 'No genes data found.')
    else:
        print(f"No matching ID {dam} found. Program ending.")
        exit()
else:
    parent1 = dam

sire = input("Enter genetic profile for sire (e.g., 'LL XOY BB DD AA McMc SpSp TaTa CC WsWs 1 4'): ").strip()
if sire.isdigit():
    sire_id = int(sire)
    matching_item2 = next((item for item in existing_data if item['id'] == sire_id), None)
    if matching_item2:
        parent2 = matching_item2.get('genes', 'No genes data found.')
    else:
        print(f"No matching ID {sire} found. Program ending.")
        exit()
else:
    parent2 = sire

offspring = generate_offspring(parent1, parent2)
print(f"Number of kittens: {len(offspring)}")
for n, child in enumerate(offspring, start=1):
    child_list = list(child)
    child_list[0] += 'kit'
    child = tuple(child_list)
    print(f"Kitten {n}: {child}")
if dam.isdigit() and sire.isdigit():
    kitten_list = store_litter(offspring, dam, sire, next_id)
elif dam.isdigit() and not sire.isdigit():
    kitten_list = store_litter(offspring, dam, None, next_id)
elif not dam.isdigit() and sire.isdigit():
    kitten_list = store_litter(offspring, None, sire, next_id)
else:
    kitten_list = store_litter(offspring, None, None, next_id)

existing_data.extend(kitten_list)
with open(file_name, 'w') as file:
    json.dump(existing_data, file, indent=4)

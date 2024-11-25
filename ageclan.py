import json
import random
from cat_creation_methods import *


def increment_ages(data):
    new_names = []
    # Check if data is a list
    if isinstance(data, list):
        # Iterate over each record and increment the age
        for record in data:
            if record.get('living', True):
                if 'age' in record and isinstance(record['age'], (int, float)):
                    record['age'] += 1
                    # Update suffix if age is in range 6-11
                    if 6 <= int(record['age']) < 12 and record['rank'] != 'Healer Apprentice':
                        record['suffix'] = 'paw'
                        record["rank"] = 'Apprentice'
                    if int(record['age']) >= 12 and record['suffix'] == 'paw':
                        record['suffix'] = get_suffix(record['prefix'], record['age'])
                        if record['rank'] == 'Apprentice':
                            record['rank'] = 'Warrior'
                            name = record['prefix'] + record['suffix']
                            new_names.append(name)
                        elif record['rank'] == 'Healer Apprentice':
                            record['rank'] = 'Healer Apprentice'
                            name = record['prefix'] + record['suffix']
                            new_names.append(name)
                    # Update rank to Queen if conditions are met
#                    if (any(kitten_id in [cat['id'] for cat in data if cat['age'] <= 5 and cat['living']] for kitten_id
#                            in record['relationships']['kittens']) and record['rank'] == 'Warrior'
#                            and record['gender'] == 'molly'):
#                        record['rank'] = 'Queen'
#                    # Demote from Queen to Warrior if all living kittens are 6 moons or older
#                    if record['rank'] == 'Queen':
#                        all_kittens_old = all(
#                            any(cat['id'] == kitten_id and cat['age'] >= 6 and cat['living'] for cat in data)
#                            for kitten_id in record['relationships']['kittens']
#                        )
#                        if all_kittens_old:
#                            record['rank'] = 'Warrior'
                    if record['rank'] == 'Leader':
                        record['suffix'] = 'star'
                    # for kitten_id in [cat['id'] for cat in data if cat['age'] <= 5 and cat['living']]:
                        # print(kitten_id)
    return data, new_names


def assign_mentor(data):
    apprentices = [cat for cat in data if 6 <= int(cat['age']) <= 12
                   and cat['relationships']['mentor'] is None and cat.get('living', True)]
    # print(apprentices)
    # Function to check if a warrior is eligible
    def is_eligible_mentor(warrior, data):
        trainees = warrior['relationships']['trainees']
        if not trainees:
            return True
        # Check if the mentor is living
        if not warrior.get('living', True):
            return False
        last_trainee = min(
            trainees,
            key=lambda id: next(cat for cat in data if cat['id'] == id)['age']
        )
        last_trainee_cat = next(cat for cat in data if cat['id'] == last_trainee)
        return last_trainee_cat['age'] >= 13

    # Include Leader, Deputy, and Healer in the pool of eligible mentors
    eligible_mentors = [cat for cat in data if
                        cat['rank'] in ['Warrior', 'Leader', 'Deputy', 'Healer'] and is_eligible_mentor(cat, data)]
    new_pairs = []

    for apprentice in apprentices:
        # Filter mentors who are not the sire or dam of the apprentice
        available_mentors = [mentor for mentor in eligible_mentors if
                             mentor['id'] != apprentice['relationships']['dam'] and mentor['id'] !=
                             apprentice['relationships']['sire']]

        if available_mentors:
            mentor = random.choice(available_mentors)
        else:
            # If no available mentors, pick sire or dam if they are warriors
            potential_mentors = [cat for cat in data if cat['id'] in [apprentice['relationships']['dam'],
                                                                      apprentice['relationships']['sire']] and cat[
                                     'rank'] in ['Warrior', 'Leader', 'Deputy', 'Healer']]
            mentor = random.choice(potential_mentors) if potential_mentors else None

        if mentor:
            apprentice['relationships']['mentor'] = mentor['id']
            mentor['relationships']['trainees'].append(apprentice['id'])
            if mentor['rank'] == 'Healer':
                apprentice['rank'] = 'Healer Apprentice'
            new_pairs.append((mentor, apprentice))
            # Recalculate eligible mentors after assigning a mentor
            eligible_mentors = [cat for cat in data if
                                cat['rank'] in ['Warrior', 'Leader', 'Deputy', 'Healer'] and is_eligible_mentor(cat,
                                                                                                                data)]

    return data, new_pairs


def add_leadership(data):
    # Find existing leader, deputy, and healer
    leader = next((cat for cat in data if cat.get('rank') == 'Leader' and cat['living'] is True), None)
    deputy = next((cat for cat in data if cat.get('rank') == 'Deputy' and cat['living'] is True), None)
    healer = next((cat for cat in data if cat.get('rank') == 'Healer' and cat['living'] is True), None)
    healer_apprentice = next((cat for cat in data if cat.get('rank') == 'Healer Apprentice' and cat['living'] is True),
                             None)

    # Helper function to find eligible leaders or deputies
    def eligible_candidates(cats, data):
        eligible = []
        for cat in cats:
            trainees = cat['relationships']['trainees']
            if trainees and next(tc for tc in data if tc['id'] == trainees[0])['age'] >= 12 and cat['living'] is True:
                eligible.append(cat)
        return eligible

    # Get all warriors
    warriors = [cat for cat in data if cat['rank'] == 'Warrior' and cat['living'] is True]
    eligible_leaders = eligible_candidates(warriors, data)

    new_leader = None
    new_deputy = None
    new_healer = None

    if not leader and not deputy:
        if eligible_leaders:
            new_leader = random.choice(eligible_leaders)
            new_leader['rank'] = 'Leader'
            new_leader['suffix'] = 'star'
            eligible_leaders.remove(new_leader)
            if eligible_leaders:
                new_deputy = random.choice(eligible_leaders)
                new_deputy['rank'] = 'Deputy'
        else:
            new_leader = random.choice(warriors)
            new_leader['rank'] = 'Leader'
            new_leader['suffix'] = 'star'
            warriors.remove(new_leader)
            new_deputy = random.choice(warriors)
            new_deputy['rank'] = 'Deputy'
    elif leader and not deputy:
        if eligible_leaders:
            new_deputy = random.choice(eligible_leaders)
            new_deputy['rank'] = 'Deputy'
        else:
            new_deputy = random.choice(warriors)
            new_deputy['rank'] = 'Deputy'
    elif not leader and deputy:
        new_leader = deputy
        new_leader['rank'] = 'Leader'
        new_leader['suffix'] = 'star'
        eligible_leaders = eligible_candidates(warriors, data)
        if eligible_leaders:
            new_deputy = random.choice(eligible_leaders)
            new_deputy['rank'] = 'Deputy'
        else:
            new_deputy = random.choice(warriors)
            new_deputy['rank'] = 'Deputy'
    elif leader and not deputy:
        if eligible_leaders:
            new_deputy = random.choice(eligible_leaders)
            new_deputy['rank'] = 'Deputy'
        else:
            if warriors:
                new_deputy = random.choice(warriors)
                new_deputy['rank'] = 'Deputy'

    if not healer:
        if healer_apprentice:
            healer_apprentice['rank'] = 'Healer'
            new_healer = healer_apprentice
        else:
            eligible_healers = [warrior for warrior in warriors if
                                not warrior['relationships']['trainees'] and not warrior['relationships']['kittens']]
            if eligible_healers:
                new_healer = random.choice(eligible_healers)
                new_healer['rank'] = 'Healer'

    return data, new_leader, new_deputy, new_healer


def apply_retired(data):
    if isinstance(data, list):
        retired_cats = []
        for record in data:
            if record.get('living', True) and record['rank'] in ['Warrior', 'Deputy', 'Healer']:
                age = int(record.get('age', 0))
                if age >= 96:
                    if any(
                            trainee_id in record['relationships']['trainees'] and
                            next(cat for cat in data if cat['id'] == trainee_id)['age'] < 12
                            for trainee_id in record['relationships']['trainees']
                    ):
                        continue

                    retirement_chance = min(age - 95, 100) / 100.0

                    if random.random() < retirement_chance:
                        record['rank'] = 'Elder'
                        retired_cats.append(record)
        return data, retired_cats
    return data, []


def apply_death(data):
    if isinstance(data, list):
        deceased_cats = []
        for record in data:
            if record.get('living', True):
                age = int(record.get('age', 0))
                rank = record.get('rank', '')

                # Base chance of death by rank
                death_chance = 0
                if rank == 'Leader':
                    death_chance = 0.005  # 0.1% chance
                    if age > 120:
                        death_chance = 0.25
                    if age > 168:
                        death_chance = 0.5
                    if age > 200:
                        death_chance = 0.75
                    if age > 216:
                        death_chance = 0.9
                elif rank == 'Deputy':
                    death_chance = 0.004  # 0.4% chance
                elif rank == 'Healer' or rank == 'Healer Apprentice':
                    death_chance = 0.002  # 0.2% chance
                elif rank == 'Elder':
                    # Chance increases with age, capped at 25%
                    death_chance = age / 100.0
                elif rank == 'Warrior':
                    death_chance = 0.004  # 0.4% chance
                    if age > 96:
                        death_chance = age / 100.0
                    if age > 120:
                        death_chance = age + 10 / 100.0
                elif rank == 'Apprentice':
                    death_chance = 0.007  # 0.7% chance
                elif rank == 'Queen':
                    death_chance = 0.002  # 0.2% chance
                elif rank == 'Kit':
                    death_chance = 0.07  # 1% chance

                # Apply death chance
                if random.random() < death_chance:
                    record['living'] = False
                    deceased_cats.append(record)

        return data, deceased_cats
    return data, []


def print_cat(data):
    # Check if data is a list
    if isinstance(data, list):
        # Iterate over each record and print the prefix and new age
        for record in data:
            if record.get('living', True):  # Check if the cat is living
                prefix = record.get('prefix', 'No prefix')
                suffix = record.get('suffix', 'No suffix')
                age = record.get('age', 'No age')
                gender = record.get('gender', 'No gender')
                rank = record.get('rank', 'No rank')
                id = record.get('id', "no id")
                print(f"{prefix}{suffix}: {age} moons old {gender} {rank} {id}")


def main(json_file_path):
    """
    Open the JSON file, load its contents, increment the age value for all records,
    print the prefix and new age for each record, and write the updated data back to the file.

    Args:
    json_file_path (str): Path to the JSON file.
    """
    # Open and read the JSON file
    with open(json_file_path, 'r') as file:
        existing_data = json.load(file)

    # Increment ages
    updated_data, deceased_cats = apply_death(existing_data)

    updated_data, new_names = increment_ages(updated_data)

    updated_data, retired_cats = apply_retired(updated_data)

    # Assign mentors to new apprentices
    updated_data, new_pairs = assign_mentor(updated_data)

    # Add leadership roles
    updated_data, new_leader, new_deputy, new_healer = add_leadership(updated_data)

    print_cat(updated_data)

    if new_leader:
        print(f"New Leader: {new_leader['prefix']}{new_leader['suffix']}")
    if new_deputy:
        print(f"New Deputy: {new_deputy['prefix']}{new_deputy['suffix']}")
    if new_healer:
        print(f"New Healer: {new_healer['prefix']}{new_healer['suffix']}")

    for name in new_names:
        print(f"{name} has completed their training and been given a full name.")

    for mentor, apprentice in new_pairs:
        print(f"{mentor['prefix']}{mentor['suffix']} is now training {apprentice['prefix']}{apprentice['suffix']}")
    for cat in retired_cats:
        print(f"{cat['prefix']}{cat['suffix']} has retired and is now an Elder.")
    # Print death messages
    for cat in deceased_cats:
        print(f"{cat['prefix']}{cat['suffix']}, a {cat['rank']}, has died this moon.")

    # Write the updated data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)


if __name__ == "__main__":
    # Define the path to your JSON file
    file_path = 'clan.json'

    # Call the main function
    main(file_path)

import json
import random
from cat_creation_methods import *


def increment_ages(data):
    # Check if data is a list
    if isinstance(data, list):
        # Iterate over each record and increment the age
        for record in data:
            if 'age' in record and isinstance(record['age'], (int, float)):
                record['age'] += 1
                # Update suffix if age is in range 6-11
                if 6 <= int(record['age']) < 12:
                    record['suffix'] = 'paw'
                    record["rank"] = 'Apprentice'
                if int(record['age']) >= 12 and record['suffix'] == 'paw':
                    record['suffix'] = get_suffix(record['prefix'], record['age'])
                    record['rank'] = 'Warrior'
                if any(kitten_id in [cat['id'] for cat in data if cat['age'] <= 5] for kitten_id in
                        record['relationships']['kittens']) and record['rank'] == 'Warrior':
                    record['rank'] = 'Queen'
                if record['rank'] == 'Queen' and all(
                        kitten_id in [cat['id'] for cat in data if cat['age'] >= 5] for kitten_id in
                        record['relationships']['kittens']):
                    record['rank'] = 'Warrior'
                if record['rank'] == 'Leader':
                    record['suffix'] = 'star'
    return data


def assign_mentor(data):
    apprentices = [cat for cat in data if 6 <= int(cat['age']) <= 12 and cat['relationships']['mentor'] is None]

    # Function to check if a warrior is eligible
    def is_eligible_mentor(warrior, data):
        trainees = warrior['relationships']['trainees']
        if not trainees:
            return True
        last_trainee = min(trainees, key=lambda id: next(cat for cat in data if cat['id'] == id)['age'])
        return next(cat for cat in data if cat['id'] == last_trainee)['age'] >= 13

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
    leader = next((cat for cat in data if cat.get('rank') == 'Leader'), None)
    deputy = next((cat for cat in data if cat.get('rank') == 'Deputy'), None)
    healer = next((cat for cat in data if cat.get('rank') == 'Healer'), None)
    healer_apprentice = next((cat for cat in data if cat.get('rank') == 'Healer Apprentice'), None)

    # Helper function to find eligible leaders or deputies
    def eligible_candidates(cats, data):
        eligible = []
        for cat in cats:
            trainees = cat['relationships']['trainees']
            if trainees and all(
                    next(tc for tc in data if tc['id'] == trainee_id)['age'] >= 12 for trainee_id in trainees):
                eligible.append(cat)
        return eligible

    # Get all warriors
    warriors = [cat for cat in data if cat['rank'] == 'Warrior']
    eligible_leaders = eligible_candidates(warriors, data)

    new_leader = None
    new_deputy = None
    new_healer = None

    if not leader and not deputy:
        if eligible_leaders:
            new_leader = random.choice(eligible_leaders)
            new_leader['rank'] = 'Leader'
            eligible_leaders.remove(new_leader)
            if eligible_leaders:
                new_deputy = random.choice(eligible_leaders)
                new_deputy['rank'] = 'Deputy'
        else:
            new_leader = random.choice(warriors)
            new_leader['rank'] = 'Leader'
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
        eligible_leaders = eligible_candidates(warriors, data)
        if eligible_leaders:
            new_deputy = random.choice(eligible_leaders)
            new_deputy['rank'] = 'Deputy'
        else:
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


def print_cat(data):

    # Check if data is a list
    if isinstance(data, list):
        # Iterate over each record and print the prefix and new age
        for record in data:
            prefix = record.get('prefix', 'No prefix')
            suffix = record.get('suffix', 'No suffix')
            age = record.get('age', 'No age')
            gender = record.get('gender', 'No gender')
            print(f"{prefix}{suffix}: {age} moons old {gender}")


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
    updated_data = increment_ages(existing_data)

    # Assign mentors to new apprentices
    updated_data, new_pairs = assign_mentor(updated_data)

    # Add leadership roles
    updated_data, new_leader, new_deputy, new_healer = add_leadership(updated_data)

    print_cat(updated_data)

    for mentor, apprentice in new_pairs:
        print(f"{mentor['prefix']}{mentor['suffix']} is now training {apprentice['prefix']}{apprentice['suffix']}")

    if new_healer:
        print(f"New Healer: {new_healer['prefix']}{new_healer['suffix']}")

    if new_leader:
        print(f"New Leader: {new_leader['prefix']}{new_leader['suffix']}")
    if new_deputy:
        print(f"New Deputy: {new_deputy['prefix']}{new_deputy['suffix']}")

    # Write the updated data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)


if __name__ == "__main__":
    # Define the path to your JSON file
    file_path = 'clan.json'

    # Call the main function
    main(file_path)

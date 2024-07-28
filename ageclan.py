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

    def is_eligible_mentor(warrior, data):
        trainees = warrior['relationships']['trainees']
        if not trainees:
            return True
        last_trainee = min(trainees, key=lambda id: next(cat for cat in data if cat['id'] == id)['age'])
        return next(cat for cat in data if cat['id'] == last_trainee)['age'] >= 13

    # Create a list of eligible mentors
    eligible_mentors = [warrior for warrior in data if
                        (warrior['rank'] == 'Warrior' or warrior['rank'] == 'Deputy'
                         or warrior['rank'] == 'Leader' or warrior['rank'] == 'Healer') and is_eligible_mentor(warrior, data)]

    for apprentice in apprentices:
        # Filter mentors who are not the sire or dam of the apprentice
        available_mentors = [mentor for mentor in eligible_mentors if
                             mentor['id'] != apprentice['relationships']['dam'] and mentor['id'] !=
                             apprentice['relationships']['sire']]

        if available_mentors:
            mentor = random.choice(available_mentors)
            apprentice['relationships']['mentor'] = mentor['id']
            mentor['relationships']['trainees'].append(apprentice['id'])
            # Recalculate eligible mentors after assigning a mentor
            eligible_mentors = [warrior for warrior in data if
                                warrior['rank'] == 'Warrior' and is_eligible_mentor(warrior, data)]

    return data


def add_leadership(data):
    # Find existing leader and deputy
    leader = next((cat for cat in data if cat.get('rank') == 'Leader'), None)
    deputy = next((cat for cat in data if cat.get('rank') == 'Deputy'), None)

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

    return data, new_leader, new_deputy


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
    updated_data = assign_mentor(updated_data)
    # Add leadership roles
    updated_data, new_leader, new_deputy = add_leadership(updated_data)

    print_cat(updated_data)

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

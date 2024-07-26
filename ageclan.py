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
                # Update suffix if age is 6
                if record['age'] == 6:
                    record['suffix'] = 'paw'
                    record["rank"] = 'Apprentice'
                if record['age'] == 12:
                    record['suffix'] = get_suffix(record['prefix'])
                    record['rank'] = 'Warrior'
    return data


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
    print_cat(updated_data)

    # Write the updated data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)


if __name__ == "__main__":
    # Define the path to your JSON file
    file_path = 'clan.json'

    # Call the main function
    main(file_path)

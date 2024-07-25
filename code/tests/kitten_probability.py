import random

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

# Dictionary to store counts
rolls_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

# Roll 10,000 times and count occurrences
total_rolls = 1000000
for _ in range(total_rolls):
    result = determine_number_of_offspring()
    rolls_count[result] += 1

# Output the results with percentages
for key, value in rolls_count.items():
    percentage = (value / total_rolls) * 100
    print(f"{key}: {value} ({percentage:.2f}%)")

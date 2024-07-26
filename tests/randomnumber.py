import random

def generate_unique_random_numbers(num_numbers, lower_bound, upper_bound):
    if num_numbers > (upper_bound - lower_bound + 1):
        raise ValueError("Number of unique numbers requested exceeds the range of available numbers")

    random_numbers = random.sample(range(lower_bound, upper_bound + 1), num_numbers)
    return random_numbers


numtogen = int(input("How many to generate?"))
lowerbound = int(input("Lower bounding"))
higherbound = int(input("Higher bounding"))

rannum = generate_unique_random_numbers(numtogen, lowerbound, higherbound)
print(rannum)

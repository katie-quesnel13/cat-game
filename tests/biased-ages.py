import random
import matplotlib.pyplot as plt

# Number of random numbers to generate
num_random_numbers = 1000000

# Function to generate a biased random number between 1 and 168
def biased_random_number():
    # Generate a random number between 0 and 1, then scale by squaring it
    return int(random.random() ** 1.5 * 168)

# Generate a list of biased random numbers
random_numbers = [biased_random_number() for _ in range(num_random_numbers)]

# Plot a histogram of the generated numbers
plt.hist(random_numbers, bins=168, range=(1, 168), density=True, color='skyblue', edgecolor='black')
plt.title('Probability Distribution of Biased Random Numbers')
plt.xlabel('Number')
plt.ylabel('Probability Density')
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.show()
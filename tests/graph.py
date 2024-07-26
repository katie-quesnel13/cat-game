import matplotlib.pyplot as plt

# Data
categories = [1, 2, 3, 4, 5, 6, 7, 8]
counts = [112546, 149987, 225227, 262049, 137889, 57270, 39814, 15218]
percentages = [11.25, 15.00, 22.52, 26.20, 13.79, 5.73, 3.98, 1.52]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, percentages, color='skyblue')

# Adding labels and title
plt.xlabel('Number of Offspring')
plt.ylabel('Percentage')
plt.title('Number of Offspring Distribution')
plt.xticks(categories)
plt.yticks(range(0, 31, 5))

# Adding text labels
for i in range(len(categories)):
    plt.text(categories[i], percentages[i], f"{counts[i]} ({percentages[i]}%)", ha='center', va='bottom')

# Displaying the plot
plt.tight_layout()
plt.show()

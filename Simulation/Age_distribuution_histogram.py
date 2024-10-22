

import matplotlib.pyplot as plt
from collections import Counter

# List of ages
ages = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5]

# Count the frequency of each age
age_counts = Counter(ages)

# Plot the histogram
plt.bar(age_counts.keys(), age_counts.values(), color='skyblue')
plt.xlabel('Age in days')
plt.ylabel('Frequency')
plt.title('Age Distribution of Newborn Babies')

plt.show()

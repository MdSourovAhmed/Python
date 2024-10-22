
import pandas as pd
import numpy as np

# Data values
data_values = [3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9, 9, 7, 6, 6, 5, 4, 4, 3, 2]

# Calculate mean and standard deviation
mean = np.mean(data_values)
std = np.std(data_values)

# Calculate z-scores
z_scores = [(x - mean) / std for x in data_values]

# Create DataFrame
df_z_scores = pd.DataFrame({
    "Data": data_values,
    "Z-score": z_scores
})

# Replace None values with calculated Z-scores

print("Updated DataFrame with Z-scores:")
print(df_z_scores)

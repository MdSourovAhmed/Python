#Ans to the Ques no-6
import numpy as np
from scipy.stats import shapiro

# Given data
data_val = [
    67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49, 78, 77,
    83, 47, 67, 63, 33, 69, 53, 51, 49, 78, 77, 83, 47, 53, 51, 49,51
]

stat, p_value=shapiro(data_val)

# Determine if data fits the normal distribution
c_v = 0.24  # Given critical value
if p_value < c_v:
  print("Data doesn't fit in the normal distribution")
else:
  print("Data fits in the normal distribution")


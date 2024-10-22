import math

single_roll_no_double_six = 35 / 36
twenty_four_roll_no_double_six = single_roll_no_double_six ** 24
probability_double_six_in_24 = 1 - twenty_four_roll_no_double_six

print(f"The probability of getting at least one double six in 24 rolls is: {probability_double_six_in_24:.4f}")

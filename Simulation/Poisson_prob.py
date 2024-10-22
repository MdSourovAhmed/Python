import math

def poisson_probability(lmbda, k):

    # :lmbda: The average number of occurrences (lambda).
    # :k: The actual number of occurrences (k).
    # :return: Poisson probability P(X = k).

    # Using the logarithmic form to avoid overflow issues
    log_prob = k * math.log(lmbda) - lmbda - math.lgamma(k + 1)
    return math.exp(log_prob)

# Test cases
cases = [
    (250, 275),
    (300, 350),
    (100, 150)
]

# Calculate and print the results
for i, (lmbda, k) in enumerate(cases, 1):
    probability = poisson_probability(lmbda, k)
    print(f"Case {i}: {lmbda}, {k} {probability:.6f}")

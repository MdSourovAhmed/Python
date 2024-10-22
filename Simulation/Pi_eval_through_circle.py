import random

def _pi(points):
    points_in_circle = 0

    for _ in range(points):
        # Generate random point (x, y) within the square with side length 2
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the circle with radius 1
        if x**2 + y**2 <= 1:
            points_in_circle += 1

    # Estimate pi
    pi_ = 4 * points_in_circle / points
    return pi_

if __name__ == "__main__":
    points = 1000000  # Number of random points to generate
    pi_ = _pi(points)
    print(f"Estimated value of π: {pi_:.6f}")

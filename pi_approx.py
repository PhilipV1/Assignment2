import random as rd
import math


# Calculates the approximation of pi using the relation
# between a circle area and square area pi/4
# That means that out of N points, pi/4 should fall inside the circle
# Hence pi = (4*amount)/N
def main():
    points = []
    n = [100, 10000, 100000]
    radius = 1
    circle_points = 0

    for element in n:
        for i in range(0, element):
            points.append((rd.random(), rd.random()))
        for p in points:
            if (p[0]**2)+(p[1]**2) < radius**2:
                circle_points += 1
        pi_approx = (circle_points*4)/element
        error_margin = math.pi - pi_approx

        print(f"Pi approximate for N = {element}: {pi_approx}")
        print(f"Absolute pi: {math.pi}")
        print(f"The error margin is: {abs(error_margin)}")
        points.clear()
        circle_points = 0


if __name__ == "__main__":
    main()

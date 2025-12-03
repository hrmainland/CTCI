# My solution to p02_robot_grid.py
from random import random, seed

seed(45)

grid = [[0 if random() < 0.8 else 1 for _ in range(10)] for _ in range(10)]

for row in grid:
    print(row)

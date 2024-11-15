#!/usr/bin/env python3

import numpy as np

coords = np.array([
    [2, 3],
    [0, 2],
    [1, 1],
    [1, 4],
    [4, 2],
    [5, 3] 
])

for point1 in coords:
    for point2 in coords:
        dist = np.linalg.norm(point2 - point1)
        print("%.2f" % dist, end=", ")
    print()
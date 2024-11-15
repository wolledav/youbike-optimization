#!/usr/bin/env python3

import hexaly.optimizer
import sys
import math
import json


# Load instance, prepare data structures
path = sys.argv[1]

with open(path, 'r') as file:
    data = json.load(file)

stations_cnt = len(data["stations"])
stations_demands = [station["s_goal"] - station["s_init"] for station in data["stations"]]
vehicles_cnt = data["vehicles"]["count"]
vehicles_capacity = data["vehicles"]["capacity"]
dist_matrix = data["distances"]


# Formulate model
with hexaly.optimizer.HexalyOptimizer() as optimizer:
    model = optimizer.model

    # Sequence of customers visited by each truck
    customers_sequences = [model.list(nb_customers) for _ in range(nb_trucks)]

# TODO hexaly specific structures, exclude depot from distance matrix
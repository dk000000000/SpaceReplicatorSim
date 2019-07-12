from Galaxy import Galaxy
from Probe import Probe
from random import choice
import numpy as np

g = Galaxy()

ACTION_LIST = ["recharge", "move", "stay", "replicate"]

def n_closest_planets_absolute(p, g, N=5):
    # get Systems
    curr_id = p.galaxy_dict[p.current_position]
    distance = np.asarray(g.distanceMatrix[curr_id, :])
    index = np.argsort(distance)[1:(N+1)]
    return index

def decide(p, g):
    a = choice(ACTION_LIST)
    a = "move"
    if a == "move":
        planets = n_closest_planets_absolute(p, g)
        return a, choice(planets)
    else:
        return a, 0

def step(g):
    pl = g.probelist
    actionD = {}
    for k, p in pl.items():
        actionD[k] = decide(p, g)
    print(actionD)
    g.step(actionD)

print(g.probelist)
print(g.probelist['0'].current_position)
step(g)
print(g.probelist)
print(g.probelist['0'].current_position)
step(g)
print(g.probelist)
print(g.probelist['0'].current_position)

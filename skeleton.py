from random import choice

g = Galaxy()

ACTION_LIST = ["recharge", "move", "stay", "replicate"]

def n_closest_planets_absolute(p, g, N):
    # get Systems
    s = g.systemlist
    curr_id = p.current_position
    distance = np.asarray(p.getdistanceMatrix()[curr_id, :])
    index = np.argsort(distance)[1:(n+1)]
    return index

def decide(probe):
    a = random.choice(ACTION_LIST)
    a = "move"
    if a == "move":
        planets = n_closest_planets_absolute(p)
        return a, random.choice(planets).position
    else:
        return a, 0

def step(g):
    pl = g.probelist
    actionD = {}
    for k, p in pl.items():
        actionD[k] = decide(p)
    g.step(actionD)


def __init__(self):
    self.distanceMatrix = 0
        self.planetId = 0



    def greedy_action(self):
        pass


    def random_action(self,n):
        planets = self.n_closest_planets_absolute(n)
        int_random = randrange(n)
        return planets[int_random]



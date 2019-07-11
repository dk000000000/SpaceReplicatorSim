from copy import copy, deepcopy

class Probe(object):
    # dict of n star systems each resource amount and how much the probe belives about the certainty of resource
    self.systemBeliefs = {} #{(0.2,0.2,0.2):[20000,0.8]} (0.2,0.2,0.2) position of the system 20000 is quantity of resource, 0.8 is the certainty of the beliefs

    self.pastPositions = {} # list of position of system represented three number in the cartesian plane they known have been to or other bots have been to

    self.block = 0 # boolean if it is blocked

    self.dead = False # out of charge

    def __init__(self,id,charge=100,position = (0,0,0),degradation = 0.01,recharge_speed=0.2,move_stay_ratio=2):
        self.id = id #id of this probe
        self.charge = charge # charge/Energy Amount -> 0 - 100
        self.position = position # star system index in the universe
        self.degradation = degradation
        self.recharge_speed = recharge_speed
        self.move_stay_ratio = move_stay_ratio

    def _updateCharge(self, act):
        if act == "recharge":
            self.charge += self.charge * self.recharge_speed
        elif act == "move":
            self.charge -= self.move_stay_ratio * self.charge * self.degradation
        elif act == "stay":
            self.charge -= self.charge * self.degradation
        else: #replicate
            self.charge /= 2
        #if charge is less than 0 will set to dead and be kill next time step
        if self.charge <= 0:
            self.dead = True

    def updateChargeBeliefs(self):



    def updateBeliefs(self,beliefs=None):
        if beliefs:#
            self.systemsBeliefs = copy(beliefs)
        else:
            self.systemsBeliefs =


    def _updateposition(self, new_position):
        self.pastPositions.append(new_position)
        self.position = new_position

    def isDead(self):
        return self.dead

    def move(self, new_position):
        self.pastPositions.append(self.position)
        self.position = new_position
        block = 1
        self._updateCharge("move")

    def replicate(self):
        self._updateCharge("replicate")
        ag = copy(self)
        block = 1
        return ag

    def recharge(self):
        self._updateCharge("recharge")

    def stay(self, index):
        self._updateCharge("stay")

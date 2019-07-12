from copy import copy, deepcopy

class Probe(object):

    self.block = 0 # boolean if it is blocked
    self.dead = False # out of charge

    def __init__(self,id,galaxy_positions,system,charge=100,degradation = 0.01,recharge_speed=0.2,move_stay_ratio=2,moving_speed=0.01):
        self.id = id #id of this probe
        # dict of list of position of system represented three number in the cartesian plane they known have been to or other bots have been to
        self.positions = {self.id:[system.position]} #{"1":[(0,0,0)]}
        # dict of n star systems each resource amount and how much the probe belives about the certainty of resource
        self.system_beliefs = {p:[maxcharge*np.random.normal(self._getDistance(p)),0]for p in galaxy_positions} #{(0.2,0.2,0.2):[20000,0.8]} (0.2,0.2,0.2) position of the system 20000 is quantity of resource, 0.8 is the certainty of the beliefs
        self.system_beliefs[system.position]=[system.charge,1]#absolutely sure about current system cahrge

        self.charge = charge # charge/Energy Amount -> 0 - 100
        self.current_position = position # star system index in the universe
        self.degradation = degradation #how fast it use resources
        self.recharge_speed = recharge_speed
        self.move_stay_ratio = move_stay_ratio
        self.moving_speed = moving_speed

    def _getDistance(self,position1,position2=(0,0,0)):
        return np.linalg.norm(np.array(position1)-np.array(position2))

    def _updateCharge(self, act):
        if act == "recharge": #increase the different between recharge and degreadation
            self.charge += self.charge * (self.recharge_speed-self.degradation)
        elif act == "move": #increase
            self.charge -= self.move_stay_ratio * self.charge * self.degradation
        elif act == "stay":
            self.charge -= self.charge * self.degradation
        else: #replicate
            self.charge /= 2
        #if charge is less than 0 will set to dead and be kill next time step
        if self.charge <= 0:
            self.dead = True

        if self.charge > 100:
            self.charge = 100

    def updateBeliefs(self,beliefs=None):
        if beliefs:#
            self.systemsBeliefs = copy(beliefs)
        else:
            self.systemsBeliefs = None


    def _updatePosition(self, new_position):
        self.positions[self.id].append(new_position)
        self.current_position = new_position

    def isDead(self):
        return self.dead

    def move(self, new_position):
        if block ==0:
            self.pastPositions.append(self.position)
            self.position = new_position
            #calculate number of time step to block
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

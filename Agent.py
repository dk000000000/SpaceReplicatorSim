from copy import copy, deepcopy

class Agent(object):

    self.systemsBeliefs = [] # list of n star systems each resource amount

    self.pastPositions = [] # list of index of system they known have been to or other bots have been to

    self.block = 0 # boolean if it is blocked

    self.dead = False # out of charge

    def __init__(self,charge=100,position = 0,degradation = 0.01,recharge_speed=0.2):
        self.charge = charge # charge/Energy Amount -> 0 - 100
        self.position = position # star system index in the universe
        self.degradation = degradation
        self.recharge_speed = recharge_speed

    def _updateCharge(self, ope):

      if ope == 0:

          self.charge += self.charge * self.recharge_speed

      elif ope == 1:

          self.charge *= 2 * self.degradation

      elif ope == 2:

          self.charge *= (1 - self.degradation)

      else:

          self.charge /= 2

      if self.charge == 0:

          self.dead = 1


    def _updateBeliefs(self):

      self.systemsBeliefs = 0


    def _updateposition(self, new_position):

      self.pastPositions.append(new_position)

      self.position = new_position


    def move(self, new_position):

      self.pastPositions.append(self.position)

      self.position = new_position

      block = 1

      self._updateCharge(1)

    def replicate(self):

      self._updateCharge(3)

      ag = copy(self)

      block = 1

      return ag

    def recharge(self):

      self._updateCharge(0)

    def stay(self, index):

      self._updateCharge(2)

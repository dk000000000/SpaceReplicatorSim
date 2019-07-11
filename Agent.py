from copy import copy, deepcopy

class Agent(object):

    systemsBeliefs = [] # list of n star systems each with its coordonates and resource amount

    pastPositions = [] #list of index of system they known have been to or other bots have been to

    charge = 100 #0-100

    position = 0 #star system index in the universe

    block = False #boolean if it is blocked

    beliefMatrix = [] # n*n distance between

    dead = False #out of charge

    degradation = 0.2

    def _updateCharge(self, ope):
      if ope == 0:
          self.charge *= self.degradation
      elif ope == 1:
          self.charge *= self.degradation
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
      self._updateCharge()
      #syst.move((self.systemsBeliefs[new_position])[0])

    def getdistanceMatrix(self):
      return self.distanceMatrix

    def replicate(self):
      self._updateCharge(3)
      ag = copy(self)
      return ag

    def stay(self, index):
      self._updateCharge(0)

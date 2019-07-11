class Agent(object):

  systemsBeliefs = 0 # 0-1M * n number of systems

  pastPositions = 0 #list of index of system they known have been to or other bots have been to

  charge = 0 #0-100

  position = 0 #[int,int,int] position in the universe

  block = 0 #boolean if it is blocked

  distanceMatrix = 0 # n*n distance between

  dead = False

  degradation = 0.2

  def __init__(self,clone):
        self.charge=clone.charge
        self.position=clone.position

  def _updateCharge(self, ope):

      if ope == 0:
          self.charge *= self.degradation
      else:
          self.charge /= 2

  def _updateBeliefs(self):
      self.systemsBeliefs = 0

  def _updateposition(self, new_position):
      self.pastPositions.append(new_position)
      self.position = new_position

  def move(self, new_position):
      self.pastPositions.append(self.position)
      self.position = new_position

  def getdistanceMatrix(self):
      return self.distanceMatrix

  def replicate(self):
      ag = Agent(self)



  def stay(index):
      #degradation

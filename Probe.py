from copy import copy, deepcopy
import math
import numpy as np
from scipy.spatial.distance import euclidean

class Probe(object):
    def __init__(self,id,galaxy_positions,system,maxcharge,galaxy_dict,dist_matrix,charge=100,degradation = 0.01,recharge_speed=0.2,move_stay_ratio=2,moving_speed=0.01):
        self.block = -1 # boolean if it is blocked
        self.blockAction = None

        self.dead = False # out of charge
        self.destination = None
        self.id = id #id of this probe
        # dict of list of position of system represented three number in the cartesian plane they known have been to or other bots have been to
        self.positions = {self.id:[system.position]} #{"1":[(0,0,0)]}
        # dict of n star systems each resource amount and how much the probe belives about the certainty of resource
        self.system_beliefs = {p:[maxcharge*np.random.normal(euclidean(p,(0,0,0))),0] for p in galaxy_positions} #{(0.2,0.2,0.2):[20000,0.8]} (0.2,0.2,0.2) position of the system 20000 is quantity of resource, 0.8 is the certainty of the beliefs
        self.system_beliefs[system.position]=[system.charge,1]#absolutely sure about current system cahrge
        self.galaxy_positions = galaxy_positions
        self.dist_matrix = dist_matrix
        self.charge = charge # charge/Energy Amount -> 0 - 100
        self.current_position = system.position # star system index in the universe
        self.galaxy_dict = galaxy_dict
        self.degradation = degradation #how fast it use resources
        self.recharge_speed = recharge_speed
        self.move_stay_ratio = move_stay_ratio
        self.moving_speed = moving_speed
        self.system = system
        self.system.movein(self.id)


    def _getDirectionVector(self,position2):
        return (np.array(position2)-np.array(self.current_position))/euclidean(self.current_position,position2)

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

    def move(self, id):
        new_position = self.galaxy_positions[id]
        self.positions[self.id].append(self.current_position)
        if self.block ==-1:
            if new_position!=self.current_position:
                self.destination = new_position
                distance = euclidean(self.current_position,self.destination)
                if distance <=self.moving_speed:
                    self._helpMove()
                    return self.current_position
                else:
                    self.block = math.ceil(distance/self.moving_speed)-1
                    self.blockAction = "move"
                    self.current_position = tuple(np.array(self.current_position) + self.moving_speed*self._getDirectionVector(self.destination))
                    self.system.moveout(self.id)
            else:
                self.stay()
        elif self.block == 0:
            self._helpMove()
            return self.current_position
        else:
            distance = euclidean(self.current_position,self.destination)
            if distance <=self.moving_speed:
                self._helpMove()
                return self.current_position
            else:
                self.current_position = tuple(np.array(self.current_position) + self.moving_speed*self._getDirectionVector(self.destination))
                self.block-=1

        self._updateCharge("move")

    def _helpMove(self):
        self.current_position = self.destination
        self.destination =None
        self.block=-1
        self.blockAction = None
        self.system.moveout(self.id)


    def replicate(self):
        if self.block == -1:
            self._updateCharge("replicate")
            self.block = 0
            self.blockAction="replicate"
            return "replicate"
        else:#block=0
            self.block-=1
            self.blockAction = None
            self._updateCharge("stay")
        self.system.replicate(self.id)

    def recharge(self):
        self.system.recharge(self.id)
        self._updateCharge("recharge")

    def stay(self):
        self.system.stay(self.id)
        self._updateCharge("stay")

    def act(self, action):
        if action[0] == "stay":
            self.stay()
        elif action[0] == "move":
            self.move(action[1])
        elif action[0] == "recharge":
            self.recharge()
        elif action[0] == "replicate":
            return self.replicate()

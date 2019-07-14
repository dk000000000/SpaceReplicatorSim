from Replicator import Replicator
from System import System
import logging
import numpy as np
from GalaxyGeneration import generateDiskGalaxy
from scipy.spatial.distance import cdist


class Galaxy(object):
    def __init__(self, Nsystems=1000,timelimit=10000,chargeMax=10**6):#number of systems, timelimit for an episode:
        self.timelimit = timelimit# max numer of time can take
        self.galaxySize = Nsystems
        self.chargeMax = chargeMax
        #dictionary of replicators
        self.replicatorlist = {} # "0":replicator("0")
        self.time = 0 # current time since the start
        self.ends = False
        positions,charges = generateDiskGalaxy(self.galaxySize,self.chargeMax)
        self.systemlist = {i:System(positions[i],charges[i]) for i in range(len(positions)) } #list of system
        self.systemPos = positions
        self.systemDict = {positions[i]:i for i in range(len(positions))}

        self.distanceMatrix = cdist(np.array(self.systemPos),np.array(self.systemPos))
        self._init_sys()
    def _init_sys(self):
        chosen = self.systemlist[0]
        self.replicatorlist["0"]=Replicator("0",self.systemPos,chosen,self.chargeMax,self.systemDict,self.distanceMatrix)
        self.replicatorcount = 0

    def step(self,actionD):
        #dictionary of action increment self.time and will return false self.timelimit is met, check_block() to block replicator to act if it is blocked
        self.replicatorAct(actionD)
        self.sychronize()
        evaluation = self.evaluate()
        self.ifEnds(evaluation)
        return self.replicatorlist,self.ends, evaluation#boolean if is out of time limit
    def evaluate(self):
        return 0
    def ifEnds(self,evaluation):
        return evaluation or self.timelimit == self.time+1
    def replicatorAct(self,actionD):
        for replicatorId,_ in self.replicatorlist.items():
            if replicatorId in actionD or self.replicatorlist[replicatorId].blockAction:
                result = self.replicatorlist[replicatorId].act(actionD[replicatorId])
                if result=="replicate":#replicate
                    replica = deepcopy(self.replicatorlist[replicatorId])
                    replica.id = self.replicatorcount
                    replica.system = self.replicatorlist[replicatorId].system
                    replica.system.movein(replica.id)
                    self.replicatorlist[replica.id] = replica
                    self.replicatorcount+=1
                elif result:#move in another galaxy
                    self.replicatorlist[replicatorId].system = self.systemlist[self.systemDict[result]]
                    self.replicatorlist[replicatorId].system.movein(replicatorId)
            else:
                self.replicatorlist[replicatorId].act(["stay",0])

    def sychronize(self):
        for _,system in self.systemlist.items():
            system.sychronize()

    def reset(self): # reset the galaxy, kill everyone
        self.replicatorlist = {}
        for key,system in self.systemlist:
            system.reset()
        self._init_sys()


    def render(self): #render what is hapenning in galaxy
        pass

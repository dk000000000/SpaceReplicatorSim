from Probe import Probe
from System import System
import logging
import numpy as np
from GalaxyGeneration import generateDiskGalaxy


class Galaxy(object):
    def __init__(self, Nsystems=1000,timelimit=10000,chargeMax=10^6):#number of systems, timelimit for an episode:
        self.timelimit = timelimit# max numer of time can take
        self.galaxySize = Nsystems
        self.chargeMax = chargeMax
        #dictionary of probes
        self.probelist = {} # "0":Probe("0")
        self.time = 0 # current time since the start
        self.ends = False
        self._initSystems()
        self.Probecount = 0

    def _initSystems(self):
        positions,charges = generateDiskGalaxy(self.galaxySize,self.chargeMax)
        self.systemlist = {positions[i]:System(positions[i],charges[i]) for i in range(len(positions)) } #list of system
        chosen = self.systemlist[list(self.systemlist.keys())[0]]
        self.probelist["0"]=Probe("0",list(self.systemlist.keys()),chosen,self.chargeMax)

    def step(self,actionD):
        #dictionary of action increment self.time and will return false self.timelimit is met, check_block() to block probe to act if it is blocked
        self.probeAct(actionD)
        self.sychronize()
        evaluation = self.evaluate()
        self.ifEnds(evaluation)
        return self.probelist,self.ends, evaluation#boolean if is out of time limit
    def evaluate(self):
        return 0
    def ifEnds(self,evaluation):
        return evaluation or self.timelimit == self.time+1
    def probeAct(self,actionD):
        for probeId,action in actionD.items():
            result = self.probelist[probeId].act(actionD[probeId])
            if result:#replicate
                replica = deepcopy(self.probelist[probeId])
                replica.id = self.Probecount
                replica.system = self.probelist[probeId].system
                self.probelist[replica.id] = replica
                self.Probecount+=1
    def sychronize(self):
        for position,system in self.systemlist.items():
            system.sychronize()

    def reset(self): # reset the galaxy, kill everyone
        self.probelist = {}
        for key,system in self.systemlist:
            system.reset()
        chosen = self.systemlist[list(self.systemlist.keys())[0]]
        self.probelist["0"]=Probe("0",list(self.systemlist.keys()),chosen,self.chargeMax)
        self.Probecount+=1


    def render(self): #render what is hapenning in galaxy
        pass

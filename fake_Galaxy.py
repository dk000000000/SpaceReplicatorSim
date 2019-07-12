from GalaxyGeneration import generateDiskGalaxy
import Probe

class Galaxy(object):
    #dictionary of probes
    self.probelist = {} # "0":Probe("0")
    self.time = 0 # current time since the start
    self.ends = False
    def __init__(self, Nsystems=1000,timelimit=10000,chargeMax=10^6):#number of systems, timelimit for an episode:
        self.timelimit = timelimit# max numer of time can take
        self.galaxySize = Nsystems
        self.chargeMax = chargeMax
        self._initSystems()

    def _initSystems(self):
        self.systemlist = {location:System(location,charge) for location,charge in generateDiskGalaxy(self.galaxySize,self.chargeMax)} #list of system

    def step(self,actionD):
        #dictionary of action increment self.time and will return false self.timelimit is met, check_block() to block probe to act if it is blocked
        self.probeAct(actionD)
        evaluation = self.evaluate()
        self.ifEnds(evaluation)
        return self.probelist, self.ends, evaluation#boolean if is out of time limit
    def evaluate(self):
        return 0
    def isEnds(self,evaluation):
        return evaluation or self.timelimit == self.time+1
    def probeAct(self,actionD):
        lucky = np.random.choice(1,len(self.systemlist) )
        system_selecter = 
        probelist[str(len(self.probelist))] = Probe(self.systemlist[])



    def reset(self): # reset the galaxy, kill everyone
        pass
    def check_block(self,probe):
        pass
    def render(self): #render what is hapenning in galaxy
        pass

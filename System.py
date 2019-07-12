class System(object):
    def __init__(self,position,charge,max_system_charge=10^6):
        self.charge= charge #0-1M reourcse
        self.position = position #position in the galaxy
        self.max_system_charge=max_system_charge
        self.agents = [] #index of number of agents inside of the system
        self.agentrecord = {"replicate":0,"death":0,"stay":0,"visit":0,"recharge":0} # replicate counts, death counts, stay counts, visit counts, recharge count

    def sychronize(self):
        #combine all information pick
        #need to finish
        #ProbeBeliefs =[a.system_beliefs for a in self.agents]
        pass
    def moveout(self,agentid):
        self.agents.pop(agentid)
    def movein(self,agentid):
        self.agents.append(agentid)
        self.agentrecord["visit"]+=1
    def replicate(self,agentid):
        self.agentrecord["replicate"]+=1
    def death(self,agentid):
        self.agentrecord["death"]+=1
    def stay(self,agentid):
        self.agentrecord["stay"]+=1
    def recharge(self,agentid):
        self.agentrecord["recharge"]+=1

    def record(self):
        pass

    def reset(self):
        self.agents = []
        self.agentrecord = {}

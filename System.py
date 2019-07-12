class System(object):
    def __init__(self,charge,position,max_system_charge=10^6):
        self.charge= charge #0-1M reourcse
        self.position = position #position in the galaxy
        self.max_system_charge=max_system_charge
        self.agents = [] #index of number of agents inside of the system
        self.agentrecord = {} # replicate counts, death counts, stay counts, move counts, recharge count

    def sychronize(self):
        #combine all information pick
        pass

    def record(self):
        pass

    def reset(self):
        self.agents = []
        self.agentrecord = {}

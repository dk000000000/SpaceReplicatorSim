import Agent
import System
import logging
class Galaxy()
    self.agentlist = {} #dictionary of agents
    self.__init__(Nsystems=1000,Nagent=1,timelimit=10000):#number of systems, number of agents:
        self.timelimit = timelimit# max numer of time can take
        self.systemlist = [System() for _ in range(Nsystems)] #list of system
    self.time # current time since the start


    def step(self,actionD) #dictionary of action increment self.time and will return false self.timelimit is met, check_block() to block agent to act if it is blocked
        return False#boolean if is out of time limit
    def reset(self): # reset the galaxy, kill everyone
        pass
    def check_block(self):
        pass
    def render(self): #render what is hapenning in galaxy
        pass

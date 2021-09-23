import numpy as np

class Topology:

    def __init__(self, list_of_pumps, grid):
        self.pumps = list_of_pumps
        self.grid = grid

    def getPumps(self):
        return len(self.list_of_pumps)
    
    def getActivePumps(self):
        active_pumps = 0 
        for pumps in self.list_of_pumps:
            active_pumps =+ pumps
        return active_pumps

    def updatePumps(pumps_state):
        for (state, pump) in zip(pumps_state, self.list_of_pumps):
            pump.state = state
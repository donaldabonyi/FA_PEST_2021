import optimization as *

class ObjectiveFunction:

    def __init__(self):
        pass

    def evaluate(self, topology):
        pass

class CostObjectiveFunction(ObjectiveFunction):

    def __init__(self, installation_cost):
        self.installation_cost = installation_cost

    def evaluate(self, topology):
        return self.installation_cost * topology.getActivePumps()

import numpy as np

class ObjectiveFunction:

    def __init__(self, installation_cost, operation_cost):
        self.installation_cost = installation_cost
        self.operation_cost = operation_cost

    def eval_OF(self, list_of_pumps):
        return self.installation_cost * list_of_pumps.getNumberPumps()


    


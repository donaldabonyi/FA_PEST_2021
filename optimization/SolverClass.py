import numpy as np

class Solver:

    def __init__(self, convergence_criteria) -> None:

        self.convergence_criteria = convergence_criteria

    def BuildProblem(self, objective_function, list_of_constraints, topology):

        self.objective_function = objective_function
        self.list_of_constraints = list_of_constraints
        self.topology = topology

    def Run(self):

        pass

    def CheckConvergence(self):

        raise(Exception("Convergence check not available. It must be implemented in the child"))


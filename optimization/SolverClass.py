import numpy as np

class Solver:

    def __init__(self, convergence_criteria, max_iterations = 20) -> None:

        self.convergence_criteria = convergence_criteria
        self.max_iterations = max_iterations

    def BuildProblem(self, objective_function, list_of_constraints, topology, initial_metric_value = 10, metric = 'msqe'):

        self.objective_function = objective_function
        self.list_of_constraints = list_of_constraints
        self.topology = topology
        self.metric_value = initial_metric_value
        self.metric = metric

    def RunLoop(self):

        while self.CheckConvergence(self.metric_value) == False:
            results = self.Evaluate()
            self.metric_value = self.CalculateMetric(results)
            

    def Evaluate(self):
        
        raise(Exception("Solver evaluation not available. It must be implemented in the child"))


    def CheckConvergence(self):

        return True

    def CalculateMetric(self, results):

        if self.metric == 'msqe':
            



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

        results_previous = None
        iteration = 0

        if iteration < self.max_iterations:
            while self.CheckConvergence(self.metric_value) == False:
                results = self.Evaluate()
                if results_previous is None:
                    results_previous = np.zeros_like(results)
                self.metric_value = self.CalculateMetric(results, results_previous)
                results_previous = results
            iteration = iteration+1
            

    def Evaluate(self):
        print("WARNING: Evaluate should be defined in the child solver.")


    def CheckConvergence(self):

        return self.convergence_criteria(self.metric_value)

    def CalculateMetric(self, results, results_previous):

        if self.metric == 'msqe':
            value = np.sqrt(sum((results-results_previous)^2) )
            return value



""" This is a Brute Force Solver that tries all the possible pump combinations and gives the best."""

import numpy as np
from itertools import product
import optimization.SolverClass as Optimization

class BruteForceSolver(Optimization.Solver):
    def BuildProblem(self, objective_function, list_of_constraints, topology, initial_metric_value=10, metric='msqe'):
        super().BuildProblem(objective_function, list_of_constraints, topology, initial_metric_value=initial_metric_value, metric=metric)
        self.best_topology = topology
        self.best_topology_objective_function_value = objective_function.eval(topology)

    def RunLoop(self):

        iterations = 2^self.topology.getPumps()
        possible_topologies = list(product([True,False], repeat = self.topology.getPumps()))

        for i_topology in possible_topologies:
            self.topology.updatePumps(i_topology)
            results = self.Evaluate()
            if not isinstance(results, bool):
                if results < self.best_topology_objective_function_value:
                    self.best_topology = self.topology
                    self.best_topology_objective_function_value = results


    def Evaluate(self):
        if not getattr(self.list_of_constraints, 'check')(self.topology).all():
            return False

        return self.objective_function.eval(self.topology)


        

            



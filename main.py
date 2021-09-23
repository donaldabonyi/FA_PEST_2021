""" This is the main script for the optimizer.
From a given case scenario, the optimal location of the pumps is given.

Input: case scenario, optimization parameters, solver
Output: results from optimal pump distribution

Authors: Ferienakademie 2021, Optimization Team"""

from optimization import *
from general_classes import *


# TODO: def Initialize()

def RunOptimizationLoop(solver, convergence_criteria):
    """Runs the optimization loop with a given solver."""

    solver_vtk_flag = False # Run without output

    solver.RunLoop()
     

def Finalize(topology, fluid_solver):
    """Performs all task at the end of the optimization (e.g. updates the topology, runs a simulation for visualization."""
    solver_vtk_flag = True # Run with output

    # TODO if needed: update the topology, depends on how Python behaves

    fluid_solver.RunWithOutput()

if __name__ == "__main__":

    # Optimization parameters (hard coded)
    convergence_criteria = lambda difference: difference < 1e-10

    # Pump initialization (hard coded)
    pump_1_x = 0.0
    pump_1_y = 0.0
    pump_2_x = 0.0
    pump_2_y = 1.0
    pump_3_x = 1.0
    pump_3_y = 0.0
    pump_4_x = 1.0
    pump_4_y = 1.0
    pump_cost = 10

    initial_ground_temperature = 15
    temperature_difference = 5
    initial_output_temperature = initial_ground_temperature- temperature_difference
    mass_flow = 2.0 # Energy demand = 41.8, mass_flow =Energy_demand/(temperature_difference*cp_water)=41.8/()

    pump_1 = Pump([pump_1_x, pump_1_y, 0.0], mass_flow, initial_ground_temperature )
    pump_2 = Pump([pump_2_x, pump_2_y, 0.0], mass_flow, initial_ground_temperature )
    pump_3 = Pump([pump_3_x, pump_3_y, 0.0], mass_flow, initial_ground_temperature )
    pump_4 = Pump([pump_4_x, pump_4_y, 0.0], mass_flow, initial_ground_temperature )

    list_of_pumps = [pump_1, pump_2, pump_3, pump_4]

    #domain initialization
    domain_corner_1 = [-1.0, -1.0]
    domain_corner_2 = [2.0, 2.0]
    domain = ['rectangle', domain_corner_1, domain_corner_2]

    # add pumps to topology

    topology = Topology( list_of_pumps, domain) 
    #we are assuming observation points at pumps only

    # define constraints (as class)
    
    constraint_1 = TemperatureConstraint(11.5 , 129) # Placeholder
    constraint_2 = PumpsConstraint(4,1) # Placeholder
    constraints = [constraint_1, constraint_2]

    # define OF (as class)
    objective_function = CostObjectiveFunction(1000000000000000) # Placeholder

    # initialize solver ( brute force -> OF and constraints, topology)
    solver = BruteForceSolver()
    solver.BuildProblem(objective_function, constraints, topology)
    # create while optimization loop. run flow with no vtk output
        
    RunOptimizationLoop(solver, convergence_criteria)

    # run again best configuration with vtk output

    Finalize(topology, fluid_solver)




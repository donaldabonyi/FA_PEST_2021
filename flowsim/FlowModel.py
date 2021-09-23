from Grid import Grid
from TimeDomain import TimeDomain
from Pump import Pump
from ObservationPoint import ObservationPoint
from InitialCondition import InitialCondition
from BoundaryCondition import BoundaryCondition
class Model:
    #expects (Grid, TimeDomain, List of Pumps, List of ObservationPoints).
    #if you don't want to have any pumps, just give an empty list, e.g. 'list()'
    #to give a permeability field, put an .h5-file named permeability_data.h5 into the folder of all the python files
    def __init__(self, grid, time_domain, pumps, materials, observations, initial_conditions=[InitialCondition()], boundary_conditions=BoundaryCondition.default_BCs()):
        self.grid = grid
        self.time_domain = time_domain
        self.pumps = pumps
        self.materials = materials
        self.observations = observations
        self.initial_conditions = initial_conditions
        self.boundary_conditions = boundary_conditions

    


    def get_observation_quantities(self):
        quantities = {}
        for observation in self.observations:
            quantities.add(observation.quantity)
        quantities = map(lambda x: x.to_pflotran(), quantities)
        return quantities

    def get_simulation_block(self):
        return """
        SIMULATION
            SIMULATION_TYPE SUBSURFACE
            PROCESS_MODELS
                SUBSURFACE_FLOW flow
                MODE TH
                /
            /
        END
        """
    

    def get_numerical_methods_block(self):
        return """
        NUMERICAL_METHODS FLOW 
            NEWTON_SOLVER 
                ANALYTICAL_JACOBIAN 
                ITOL_UPDATE 1.d0 
                RTOL 1.d-3 
            / 
            LINEAR_SOLVER 
                SOLVER ITERATIVE 
            / 
        END
        """
    
    def get_output_file(self):
        return f"""
        OUTPUT
            SNAPSHOT_FILE
                {self.time_domain.snapshot_contrib()}
                FORMAT VTK
                PRINT_COLUMN_IDS
                VARIABLES
                    {self.get_observation_quantities()}
                /
            /
            OBSERVATION_FILE
                {self.time_domain.observation_contrib()}
                VARIABLES
                    {self.get_observation_quantities()}
                /
            /
        END
        """


    def to_pflotran(self):
        return f"""
        {self.get_simulation_block()}
        SUBSURFACE
        REFERENCE_PRESSURE 101325.
        {self.get_numerical_methods_block()}
        {self.grid.to_pflotran()}
        {[material.to_pflotran() for material in self.materials]}
        {self.time_domain.to_pflotran()}
        {self.boundary_conditions.to_pflotran()}
        {self.initial_conditions.to_pflotran()}

        HDF5_READ_GROUP_SIZE 1
        END_SUBSURFACE
                
        """
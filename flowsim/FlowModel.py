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


        self.observations.extend([c for s in map(lambda x: x.observations, pumps) for c in s])

    def get_observation_quantities(self):
        quantities = {}
        for observation in self.observations:
            quantities[observation.quantity] = observation.quantity
        return quantities.keys()

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
                    {"".join([q.to_pflotran() for q in self.get_observation_quantities()])}
                /
            /   
            OBSERVATION_FILE
                {self.time_domain.observation_contrib()}
                VARIABLES
                    {"".join([q.to_pflotran() for q in self.get_observation_quantities()])}
                /
            /
        END
        """


    def to_pflotran(self):
        perm_string = "DATASET permeability_values\nFILENAME permeability_values.h5\nHDF5_DATASET_NAME permeability_values\nEND" if self.materials[0].permeability_from_file else ""
        return f"""
        {self.get_simulation_block()}
        SUBSURFACE
        REFERENCE_PRESSURE 101325.
        {self.get_numerical_methods_block()}
        {self.grid.to_pflotran()}
        FLUID_PROPERTY
            DIFFUSION_COEFFICIENT 1.d-9
        /
        {"".join([material.to_pflotran() for material in self.materials])}
        {self.get_output_file()}
        {perm_string}
        {self.time_domain.to_pflotran()}
        {"".join([ic.to_pflotran() for ic in self.initial_conditions])}
        {"".join([bc.to_pflotran() for bc in self.boundary_conditions])}
        {"".join([obs.to_pflotran() for obs in self.observations])}
        STRATA
            REGION All
            MATERIAL gravel
        END
        {"".join([pump.to_pflotran() for pump in self.pumps])}
        

        HDF5_READ_GROUP_SIZE 1
        END_SUBSURFACE
                
        """

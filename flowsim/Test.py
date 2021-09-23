from FluidSolver import FluidSolver
from Grid import Grid
from Position import Position
from TimeDomain import TimeDomain
from Pump import Pump, PumpState
from ObservationPoint import ObservationPoint, Quantity
from FlowModel import Model
from Material import Material,FluidProperties
from BoundaryCondition import BoundaryCondition
from InitialCondition import InitialCondition

bc = BoundaryCondition()
ic = InitialCondition()
time_domain = TimeDomain(10,1)
timesteps = [i for i in range(10)]
grid = Grid(10,10,1, Position(10,10,10))
pump = Pump("pump_1",extraction_position= Position(1,1,1),injection_position=Position(1,2,1), timesteps=timesteps, mass_flows=[5 for i in range(10)], temperatures=[15 for i in range(10)], state=PumpState.ON )
material = Material(1,"gravel")
fluid_props = FluidProperties()
observation = ObservationPoint("obs_1", Position(5,5,5) , Quantity.Temperature )

model = Model(grid, time_domain=time_domain, pumps=[pump], materials=[material], observations=[observation])

solver = FluidSolver(model=model, num_procs=1)

solver.write_input_file()
from Grid import Grid
from Position import Position
from TimeDomain import TimeDomain
from Pump import Pump, PumpState


#time_domain = TimeDomain(10,1)
timesteps = [i for i in range(10)]
#grid = Grid(10,10,1, Position(10,10,10))
pump = Pump(id="pump_1",extraction_position= Position(1,1,0),injection_position=Position(1,2,0), timesteps=timesteps, mass_flows=[5 for i in range(10)], temperatures=[15 for i in range(10)], state=PumpState.ON)
#pump = Pump("pump_1",Position(1,1,0),Position(1,2,0), timesteps, [5 for i in range(10)], [15 for i in range(10)], PumpState.ON)

print(pump.to_pflotran())

from enum import Enum
from ObservationPoint import ObservationPoint, Quantity
from Position import Position
from Region import Region
import copy
import util.NumberToPflotran as ntp

def unpack(s):
    return " ".join(map(str, s))  # map(), just for kicks

class PumpState(Enum):
    ON = True
    OFF = False

class Pump:
    #note that pumps are numbered after their time of creation (e.g. the first pump's flow condition is called 'fc_pump_1' and its region is called 'region_pump_1')
    def __init__(self, id, extraction_position, injection_position, timesteps, mass_flows, temperatures, state, pump_height=30):
        self.id = id
        self.extraction_position = extraction_position
        self.injection_position = injection_position
        self.timesteps = timesteps
        self.mass_flows = mass_flows
        self.temperatures = temperatures
        self.state = state
        self.pump_height = pump_height

        # also create two observations for the pumps
        self.observations = [ObservationPoint(id=f"obs_injection_{id}",position=injection_position, quantity=Quantity.Temperature), ObservationPoint(id=f"obs_extraction_{id}",position=extraction_position, quantity=Quantity.Temperature)]

        self.injection_region = f"r_injection_{self.id}"
        self.extraction_region = f"r_extraction_{self.id}"
        self.injection_fc=f"fc_injection_{self.id}"
        self.extraction_fc=f"fc_extraction_{self.id}"

        

    def tabify_list(self,lst, num_tabs=1):
        string =""
        for time_step, data in zip(self.timesteps,lst):
            for i in range(num_tabs):
                string+="\t"
            string = string + f"{ntp.ntop(time_step)} {ntp.ntop(data)}\n"
        return string

    def create_source_sink(self):
        return f"""
SOURCE_SINK
    FLOW_CONDITION {self.injection_fc}
    REGION {self.injection_region}
END

SOURCE_SINK
    FLOW_CONDITION {self.extraction_fc}
    REGION {self.extraction_region}
END
        """
    
    def create_regions(self):
        extraction_bottom = copy.deepcopy(self.extraction_position)
        injection_bottom = copy.deepcopy(self.injection_position)
        extraction_bottom.add_height(self.pump_height)
        injection_bottom.add_height(self.pump_height)
        extraction_region = Region(f"extraction_{self.id}",position_start=self.extraction_position, position_end=extraction_bottom)
        injection_region =  Region(f"injection_{self.id}",position_start=self.injection_position, position_end=injection_bottom)
        return list(map(lambda x: x.to_pflotran(), [extraction_region,injection_region]))

    def create_observations(self):
        return list(map(lambda x: x.to_pflotran(), self.observations))

    def create_flow_condition(self):
        return f""" 
FLOW_CONDITION {self.injection_fc}
    TYPE
        RATE SCALED_MASS_RATE VOLUME
        TEMPERATURE DIRICHLET
    /

    RATE LIST
        TIME_UNITS d
        DATA_UNITS kg/s
        INTERPOLATION LINEAR
        #time   #massrate
{self.tabify_list(self.mass_flows, num_tabs=1)}
    /

    TEMPERATURE LIST
        TIME_UNITS d
        DATA_UNITS C
        INTERPOLATION LINEAR
        #time   #temperature
{self.tabify_list(self.temperatures, num_tabs=1)}
    /
END

FLOW_CONDITION {self.extraction_fc}
  TYPE
    RATE SCALED_MASS_RATE VOLUME
    ENERGY_RATE ENERGY_RATE NEIGHBOR_PERM
  /
  RATE LIST 
    TIME_UNITS d 
    DATA_UNITS kg/s
    INTERPOLATION LINEAR
    #time  #massrate
{self.tabify_list(self.mass_flows, num_tabs=1)}
  /
  ENERGY_RATE 0 W
END
        """

    def to_pflotran(self):
        return f"""

{unpack(self.create_regions())}
{self.create_flow_condition()}
{self.create_source_sink()}
        """


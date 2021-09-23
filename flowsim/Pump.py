from enum import Enum
from main.flowsim.ObservationPoint import ObservationPoint, Quantity

from Position import Position

class PumpState(Enum):
    ON = True
    OFF = False

class Pump:
    #note that pumps are numbered after their time of creation (e.g. the first pump's flow condition is called 'fc_pump_1' and its region is called 'region_pump_1')
    def __init__(self, id, extraction_position, injection_position, timesteps, mass_flows, temperatures, state):
        self.id = id
        self.extraction_position = extraction_position
        self.injection_position = injection_position
        self.timesteps = timesteps
        self.mass_flows = mass_flows
        self.temperatures = temperatures
        self.state = state

        # also create two observations for the pumps
        self.observations = [ObservationPoint(id=f"injection_pump_{id}",position=injection_position, quantity=Quantity.Temperature), ObservationPoint(id=f"extraction_pump_{id}",position=extraction_position, quantity=Quantity.Temperature)]

        self.flow_condition_name = f"fc_pump_{self.id}"
        self.region_name = f"region_pump_{self.id}"

        

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
    FLOW_CONDITION {self.flow_condition_name}
    REGION {self.region_name}
END
        """
    
    def create_region(self):
        return f"""
REGION {self.region_name}
    COORDINATE {self.position.to_pflotran()}
END
        """

    def create_flow_condition(self):
        return f""" 
FLOW_CONDITION {self.flow_condition_name}
    TYPE
        RATE SCALED_MASS_RATE VOLUME
        TEMPERATURE DIRICHLET
    /

    RATE LIST
        TIME_UNITS d
        DATA_UNITS kg/s
        INTERPOLATION LINEAR
        #time   #massrate
{self.tabify_list(self.mass_flows, num_tabs=2)}
    /

    TEMPERATURE LIST
        TIME_UNITS d
        DATA_UNITS C
        INTERPOLATION LINEAR
        #time   #temperature
{self.tabify_list(self.temperatures, num_tabs=2)}
    /
END
        """

    def to_pflotran(self):
        return f"""
        {map(lambda x: x.to_pflotran(), self.observations)}
        {self.create_region()}
        {self.create_flow_condition()}
        {self.create_source_sink()}
        """


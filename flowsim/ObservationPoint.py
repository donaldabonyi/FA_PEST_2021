from enum import Enum

from Position import Position

class Quantity(Enum):
    Temperature = 1
    LiquidPressure = 2
    Permeability = 3
    def to_pflotran(self):
        if(self == 1): return "TEMPERATURE"
        if(self == 2): return "LIQUID_PRESSURE"
        if(self == 3): return "PERMEABILITY"

class ObservationPoint:
    #orders PFLOTRAN to put data observed at the specified coordinate into the OBSERVATION_FILE
    def __init__(self, id, position):
        global static_observation_counter
        self.id = id
        self.pos = position

    def to_pflotran(self):
        return f"""
            REGION observation_{self.id}
                COORDINATE {self.pos.to_pflotran()}
            /
            OBSERVATION
                REGION observation{self.id}
                AT_COORDINATE {self.pos.to_pflotran()}
            /
        """
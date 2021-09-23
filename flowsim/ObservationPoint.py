from enum import Enum

from Position import Position

class Quantity(Enum):
    Temperature = 1
    LiquidPressure = 2
    Permeability = 3

    def to_pflotran(self):
        if(self == Quantity.Temperature): return "TEMPERATURE"
        if(self == Quantity.LiquidPressure): return "LIQUID_PRESSURE"
        if(self == Quantity.Permeability): return "PERMEABILITY"

class ObservationPoint:
    #orders PFLOTRAN to put data observed at the specified coordinate into the OBSERVATION_FILE
    def __init__(self, id, position, quantity):
        self.id = id
        self.pos = position
        self.quantity = quantity

        self.region_name = f"observation_region_{self.id}"

    def to_pflotran(self):
        return f"""
REGION {self.region_name}
    COORDINATE {self.pos.to_pflotran()}
/
OBSERVATION
    REGION {self.region_name}
    AT_COORDINATE {self.pos.to_pflotran()}
/
        """
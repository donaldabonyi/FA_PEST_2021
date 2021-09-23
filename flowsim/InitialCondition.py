import NumberToPflotran
from Region import Region
from Position import Position

init_cond_counter = 1

class InitialCondition:
    #give _grad as Position objects
    #if not needed: pressure_type = "", datum = False, pressure_grad = (0,0,0)
    def __init__(self, region=Region("All",Position(0,0,0),Position(600,200,30)), pressure_type = "HYDROSTATIC", temperature_type = "DIRICHLET", datum = Position(0,0,20), pressure = 101325, temperature = 10, pressure_grad = Position(-0.005,0,0), temperature_grad = (0,0,0)):
        global init_cond_counter
        self.pflotran_string = f"""
        FLOW_CONDITION initial{init_cond_counter}
            TYPE
                {"PRESSURE "+pressure_type if pressure_type != "" else ""}
                {"TEMPERATURE "+temperature_type if temperature_type != "" else ""}
            /
            {"DATUM "datum.to_pflotran() if datum != False else ""}
            GRADIENT
                {"PRESSURE "+pressure_grad.to_pflotran() if pressure_grad != (0,0,0) else ""}
                {"TEMPERATURE "+temperature_grad.to_pflotran() if temperature_grad != (0,0,0) else ""}
            /
            {"PRESSURE "+NumberToPflotran.numberToPflotran(pressure) if pressure_type != "" else ""}
            {"TEMPERATURE "+NumberToPflotran.numberToPflotran(temperature) if temperature_type != "" else ""}
        END

        {region.to_pflotran()}

        INITIAL_CONDITION init{init_cond_counter}
            FLOW_CONDITION initial{init_cond_counter}
            REGION {region.name}
        END
        """
        init_cond_counter += 1
    def to_pflotran(self):
        return self.pflotran_string
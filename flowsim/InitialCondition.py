import util.NumberToPflotran as NumberToPflotran

init_cond_counter = 1

class InitialCondition:
    #give _grad as Position objects
    def __init__(self, region, pressure_type = "", temperature_type = "", datum = False, pressure = 0, temperature = 0, pressure_grad = (0,0,0), temperature_grad = (0,0,0)):
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
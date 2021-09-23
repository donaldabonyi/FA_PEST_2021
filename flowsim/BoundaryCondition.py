import util.NumberToPflotran as ntp
class BoundaryCondition:
    #give _grad as Position objects
    def __init__(self, name="inflow", region=Region("west", Position(0,0,0), Position(0, 200, 30)), pressure_type = "HYDROSTATIC", temperature_type = "DIRICHLET", datum = Position(0,0,20), pressure = 101325, temperature = 10, pressure_grad = (-0.005,0,0), temperature_grad = (0,0,0)):
        self.pflotran_string = f"""
        FLOW_CONDITION {name}_flow_cond
            TYPE
                {"PRESSURE "+pressure_type if pressure_type != "" else ""}
                {"TEMPERATURE "+temperature_type if temperature_type != "" else ""}
            /
            {"DATUM "datum.to_pflotran() if datum != False else ""}
            GRADIENT
                {"PRESSURE "+pressure_grad.to_pflotran() if pressure_grad != (0,0,0) else ""}
                {"TEMPERATURE "+temperature_grad.to_pflotran() if temperature_grad != (0,0,0) else ""}
            /
            {"PRESSURE "+ntp.ntop(pressure) if pressure_type != "" else ""}
            {"TEMPERATURE "+ntp.ntop(temperature) if temperature_type != "" else ""}
        END

        {region.to_pflotran()}

        BOUNDARY_CONDITION {name}
            FLOW_CONDITION {name}_flow_cond
            REGION {region.name}
        END
        """
    def to_pflotran(self):
        return self.pflotran_string
    def default_BCs(self):
        l = list()
        l.append(BoundaryCondition())
        l.append(BoundaryCondition(name="outflow", region=Region("east", Position(600,0,0), Position(600,200,30))))
        return l
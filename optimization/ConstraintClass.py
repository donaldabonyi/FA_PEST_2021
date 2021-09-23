import optimization as *
   
class Constraint:
    def __init__(self):

    def check(self,topology):
        pass

class TemperatureConstraint(Constraint):
    def __init__(self, max_temperature, min_temparature):
        self.max_temperature = max_temperature
        self.min_temperature = min_temparature

    def check(self, topology):
        for pump in topology.list_of_pumps:
            if (pump.heating == True):
                if ((pump.extraction_observation_point.temperature  >= self.min_temperature) == False):
                    return False

            else:
                if ((pump.extraction_observation_point.temperature <= self.max_temperature)==False):
                    return False
        return True


class NumberPumpsConstraint(Constraint):
    def __init__(self, max_number_pumps, min_number_pumps):
        self.max_pumps = max_number_pumps
        self.min_pumps = min_number_pumps

    def check(self, topology):
        return topology.getActivePumps() >= self.min_pumps and self.topology.getActivePumps() <= self.max_pumps  

class EnergyConstraint(Constraint):
    def __init__(self, energy_demand):
        self.energy_demand = energy_demand

    def check(self, topology):
        pass
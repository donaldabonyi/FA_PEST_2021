import numpy as np
   
class Constraint:
    def __init__(self, max_temperature, min_temparature, max_number_pumps, min_number_pumps, energy_demand):
        self.max_temperature = max_temperature
        self.min_temperature = min_temparature
        self.max_pumps = max_number_pumps
        self.min_pumps = min_number_pumps
        self.energy_demand = energy_demand

    def checkTemperature(self,topology):
        for pump in topology.list_of_pumps:
            if (pump.heating == True):
                #temperature_constraint = NonlinearConstraint(pump.extraction_observation_point.temperature, self.min_temperature, np.inf)
                if ((pump.extraction_observation_point.temperature  >= self.min_temperature) == False):
                    return False

            else:
                #temperature_constraint = NonlinearConstraint(pump.extraction_observation_point.temperature, -np.inf, self.max_temperature)
                if ((pump.extraction_observation_point.temperature <= self.max_temperature)==False):
                    return False
        return True


    def checkNumberPumps(self, topolgy):
        #return NonlinearConstraint(topology.getNumberPumps(), self.min_pumps, self.max_pumps)
        return topology.getNumberPumps() >= self.min_pumps and topology.getNumberPumps() <= self.max_pumps

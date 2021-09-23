class Pump:
    def __init__(self, injection_observation_point, extraction_observation_point, massflow, state, heating):
        self.injection_observation_point = injection_observation_point
        self.extraction_observation_point = extraction_observation_point
        self.massflow = massflow
        self.state = state
        self.heating = heating
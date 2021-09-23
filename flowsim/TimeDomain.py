import util.NumberToPflotran as ntp

class TimeDomain:
    def __init__(self, days, max_step):
        self.days = days
        self.max_step = max_step

    def to_pflotran(self):
        return f"""
        TIME
            FINAL_TIME {str(self.days)} d
            MAXIMUM_TIMESTEP_SIZE {str(self.max_step)}d0 d
        END
        """
    #assumption periodic time == max time step
    def snapshot_contrib(self):
        return f"""
                PERIODIC TIME {ntp.ntop(self.max_step)} d BETWEEN 0. d AND {ntp.ntop(self.days)} d
        """
    def observation_contrib(self):
        return f"""
                PERIODIC TIME {ntp.ntop(self.max_step)} d BETWEEN 0. d AND {ntp.ntop(self.days)}. d
        """
import util.NumberToPflotran as ntp

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_pflotran(self):
        return ntp.ntop(self.x) + " " + ntp.ntop(self.y) + " " + ntp.ntop(self.z)
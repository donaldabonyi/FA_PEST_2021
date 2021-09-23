
import util.NumberToPflotran as ntp

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add_height(self, height):
        self.z +=height
        
    def to_pflotran(self):
        return ntp.ntop(self.x) + " " + ntp.ntop(self.y) + " " + ntp.ntop(self.z)
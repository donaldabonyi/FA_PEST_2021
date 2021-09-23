<<<<<<< HEAD
import util.NumberToPflotran as ntp
=======
import util.NumberToPflotran as NumberToPflotran
>>>>>>> 6d23870 (Added the required Pump changes:)

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_pflotran(self):
        return ntp.ntop(self.x) + " " + ntp.ntop(self.y) + " " + ntp.ntop(self.z)
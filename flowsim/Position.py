import NumberToPflotran

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_pflotran(self):
        return NumberToPflotran.numberToPflotran(self.x) + " " + NumberToPflotran.numberToPflotran(self.y) + " " + NumberToPflotran.numberToPflotran(self.z)
class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_pflotran(self):
        return f"{str(self.x)}.d0 {str(self.y)}.d0 {str(self.z)}.d0"
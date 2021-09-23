from Position import Position

class Grid:
    #give number of cells in x, y, z-direction and Position (xmax,ymax,zmax) defining the grid box size together with coordinate (0,0,0)
    def __init__(self, cellnumber_x, cellnumber_y, cellnumber_z, bound_position):
        self.cellX = cellnumber_x
        self.cellY = cellnumber_y
        self.cellZ = cellnumber_z
        self.bound_pos = bound_position

    def to_pflotran(self):
        return f"""
        GRID
            TYPE STRUCTURED
            NXYZ {str(self.cellX)} {str(self.cellY)} {str(self.cellZ)}
            BOUNDS
                0.d0 0.d0 0.d0
                {self.bound_pos.to_pflotran()}
            /
        END
        """
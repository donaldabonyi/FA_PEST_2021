import numpy as np

def write_permeability_file(permeability_array, cells_grid):
    iarray = np.arange(1, cells_grid.shape[0] + 1, 1)

    print(cells_grid.shape[0])
    print(iarray)
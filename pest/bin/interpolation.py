import read_input as input
import unstructured_gridh5 as grid
import scipy.interpolate as interpolate
import write_output_h5 as out
import pandas as pd
import numpy as np

# read pilot points from .dat file
pilot_points = input.read_input()

# save data from pilot points in extra lists for the interpolation
x_coord_pp = pilot_points.loc[:,"x_coord"]
y_coord_pp = pilot_points.loc[:,"x_coord"]
permeability_pp = pilot_points.loc[:,"permeability"]

# get grid information
x_grid, y_grid = grid.define_grid()

# call the interpolation Rbf
rbf_function = interpolate.Rbf(x_coord_pp, y_coord_pp, permeability_pp)
interpolated_permeability = rbf_function(x_grid[1], y_grid[1])
print(type(interpolated_permeability))
# save grid as np array
#grid_df = pd.DataFrame([x_grid[1], y_grid[1], interpolated_permeability])
cells_grid = np.array([x_grid[1], y_grid[1]])

out.write_permeability_file(interpolated_permeability, cells_grid)

# testing rbf
# print(x_grid[1][0])
# print(y_grid[1][0])
# print(interpolated_permeability[0])

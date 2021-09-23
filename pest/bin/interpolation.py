import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
import csv
import h5py


def interpolation_main():
    # read pilot points from .dat file
    pilot_points = read_pilot_points()

    # save data from pilot points in extra lists for the interpolation
    x_coord_pp = pilot_points.loc[:, "x_coord"]
    y_coord_pp = pilot_points.loc[:, "x_coord"]
    permeability_pp = pilot_points.loc[:, "permeability"]

    # get grid information
    x_grid, y_grid = read_grid()

    # call the interpolation Rbf
    rbf_function = interpolate.Rbf(x_coord_pp, y_coord_pp, permeability_pp)
    interpolated_permeability = rbf_function(x_grid, y_grid)
    print(type(interpolated_permeability))

    # save grid as np array
    cells_grid = np.array([x_grid, y_grid])

    # writes the permeability file from the guessed permeability on the grid cells
    write_permeability_file(interpolated_permeability, cells_grid)


def read_pilot_points():
    # read pilot points from .dat file
    with open('../Data/permpp.dat') as dat_file, open('../Data/permpp.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        for line in dat_file:
            row = [field.strip() for field in line.split()]
            csv_writer.writerow(row)

    data = pd.read_csv('../Data/permpp.csv', names=["ID", "x_coord", "y_coord", "n", "permeability"])
    return data


def write_permeability_file(permeability_array, cells_grid):
    # writes the permeability input file for PEST
    iarray = np.arange(1, cells_grid.shape[0] + 1, 1)

    print(cells_grid.shape[0])
    print(iarray)


def read_grid():
    # reads grid file in .h5 format
    filename = '../PFLOTRAN/pflotran_boxmodel.h5'

    with h5py.File(filename, "r") as file:
        # List all groups
        a_group_key = list(file.keys())[0]

        # Get the data
        data = list(file[a_group_key])
        dataset = file['Domain']

        list_data_XC = [key for key in dataset['XC']]
        list_data_YC = [key for key in dataset['YC']]
    return list_data_XC, list_data_YC

import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
import csv
import h5py

def interpolation_main():
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

def read_input():
    # read pilot points
    with open('Data/permpp.dat') as dat_file, open('permpp.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        for line in dat_file:
            row = [field.strip() for field in line.split()]
            csv_writer.writerow(row)

    data = pd.read_csv('permpp.csv', names=["ID", "x_coord", "y_coord", "n", "permeability"])
    return data

def write_permeability_file(permeability_array, cells_grid):
    # writes the permeability input file for PEST
    iarray = np.arange(1, cells_grid.shape[0] + 1, 1)

    print(cells_grid.shape[0])
    print(iarray)


def define_grid():
    filename = '../PFLOTRAN/pflotran_boxmodel.h5'

    list_data_XC = ['XC']
    list_data_YC = ['YC']
    with h5py.File(filename, "r") as file:
        # List all groups
        a_group_key = list(file.keys())[0]

        # Get the data
        data = list(file[a_group_key])
        dataset = file['Domain']

        data_xc = [key for key in dataset['XC']]
        list_data_XC.append(data_xc)
        data_yc = [key for key in dataset['YC']]
        list_data_YC.append(data_yc)
    return list_data_XC, list_data_YC
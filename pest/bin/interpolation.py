import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
import csv
import h5py
from io import StringIO

DEBUG = False

def debug_print(s, *args):
    if DEBUG:
        print(s % args)


def interpolation_main():
    # read pilot points from .dat file
    pilot_points = read_pilot_points()
    debug_print('\nPilot_points: \n', pilot_points)

    # save data from pilot points in extra lists for the interpolation
    x_coord_pp = pilot_points.loc[:, "x_coord"]
    y_coord_pp = pilot_points.loc[:, "y_coord"]
    permeability_pp = pilot_points.loc[:, "permeability"]
    debug_print('log permeability_pp: \n', np.log(permeability_pp))

    # log transform the interpolated values
    permeability_pp = np.log10(permeability_pp)
    debug_print(x_coord_pp)

    # get grid information
    x_grid, y_grid = read_grid()

    # call the interpolation Rbf
    rbf_function = interpolate.Rbf(x_coord_pp, y_coord_pp, permeability_pp, function='thin_plate')
    interpolated_permeability = rbf_function(x_grid, y_grid)
    debug_print('transformed interpolated permeability: \n', interpolated_permeability)

    # inv-log transform the interpolated values
    interpolated_permeability = np.exp(interpolated_permeability)
    debug_print('interpolated permeability: \n', interpolated_permeability)

    # save grid as np array
    cells_grid = np.array([x_grid, y_grid])
    debug_print('\ncells_grid: \n', cells_grid)
    # writes the permeability file from the guessed permeability on the grid cells
    write_permeability_file(interpolated_permeability, cells_grid)

    # Print the created h5 file
    filename = "../PFLOTRAN/permeability_values.h5"
    interpolated_points = read_output_file(filename)
    debug_print(interpolated_points)

def read_pilot_points():
    # read pilot points from .dat file
    with open('../Data/permpp.dat') as dat_file, StringIO("") as csv_buffer:
        csv_writer = csv.writer(csv_buffer)

        for line in dat_file:
            row = [field.strip() for field in line.split()]
            csv_writer.writerow(row)
        csv_buffer.seek(0)

        data = pd.read_csv(csv_buffer, names=["ID", "x_coord", "y_coord", "n", "permeability"])
    print(data)
    return data


# writes the permeability input file for PEST
def write_permeability_file(perm_array, cells_grid):
    number_cells = perm_array.shape[0]
    ids = np.arange(1, number_cells + 1)

    assert number_cells == cells_grid.shape[1]

    file = h5py.File("../PFLOTRAN/permeability_values.h5", "w") 
    # NOTE there may be PFLOTRAN problems as the ids are integers now
    cell_ids = file.create_dataset("Cell Ids", data=ids)
    perm_vals = file.create_dataset("Permeability", data=perm_array)

    debug_print('Wrote to permeability_values.h5: Cell Ids: \n', cell_ids[:], "\n")
    debug_print('Wrote to permeability_values.h5: Permeability: \n', perm_vals[:], "\n")



def read_grid():
    # reads grid file in .h5 format
    filename = '../PFLOTRAN/pflotran_boxmodel.h5'

    with h5py.File(filename, "r") as file:

        debug_print('\nGroup keys in input h5 file: \n', list(file.keys())[0])

        dataset = file['Domain']

        list_data_XC = [key for key in dataset['XC']]
        list_data_YC = [key for key in dataset['YC']]
    return list_data_XC, list_data_YC


def read_output_file(filename):
    with h5py.File(filename, "r") as file:

        debug_print('\nGroup keys in created h5 file: \n', list(file.keys()))

        # dataset = file['Permeability']

        list_data_XC = [key for key in file['Cell Ids']]
        list_data_YC = [key for key in file['Permeability']]
    return list_data_XC, list_data_YC    


if __name__ == '__main__':
    interpolation_main()


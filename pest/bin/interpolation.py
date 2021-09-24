import os

import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
import csv
import h5py

PFLOTRAN_DIR = '../PFLOTRAN/'

PFLOTRAN_BOXMODEL = PFLOTRAN_DIR + 'pflotran_boxmodel.h5'
PERMEABILITY_VALUES = PFLOTRAN_DIR + 'permeability_values.h5'

DATA_DIR = '../Data/'

DATA_PERMPP_CSV = DATA_DIR + 'permpp.csv'
DATA_PERMPP_DAT = DATA_DIR + 'permpp.dat'

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
    debug_print('log permeability_pp: \n', np.exp(permeability_pp))

    # log transform the interpolated values
    debug_print(x_coord_pp)

    # get grid information
    x_grid, y_grid = read_grid()

    # call the interpolation Rbf
    rbf_function = interpolate.Rbf(x_coord_pp, y_coord_pp, permeability_pp, function='linear')
    interpolated_permeability = rbf_function(x_grid, y_grid)

    print("min value: " + str(np.min(interpolated_permeability)) + ", max value: " + str(np.max(interpolated_permeability)))
    print('interpolated permeability: \n', interpolated_permeability)

    # save grid as np array
    cells_grid = np.array([x_grid, y_grid])
    debug_print('\ncells_grid: \n', cells_grid)
    # writes the permeability file from the guessed permeability on the grid cells
    write_permeability_file(interpolated_permeability, cells_grid)

    # Print the created h5 file
    filename = PERMEABILITY_VALUES
    interpolated_points = read_output_file(filename)
    debug_print(interpolated_points)

def read_pilot_points():
    if False:
        # read pilot points from .dat file
        if not (os.path.isfile(DATA_PERMPP_DAT) or os.path.isfile(DATA_PERMPP_DAT)):
            print("It appears you do not have at least some of the data files. Please download them from Nextcloud.")
            quit(1)

        with open(DATA_PERMPP_DAT) as dat_file, open(DATA_PERMPP_CSV, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            for line in dat_file:
                row = [field.strip() for field in line.split()]
                csv_writer.writerow(row)

    data = pd.read_csv(DATA_PERMPP_CSV, names=["ID", "x_coord", "y_coord", "n", "permeability"])
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
    with h5py.File(PFLOTRAN_BOXMODEL, "r") as file:
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


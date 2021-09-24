import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
import csv
import h5py


def interpolation_main():
    # read pilot points from .dat file
    pilot_points = read_pilot_points()
    print('\nPilot_points: \n', pilot_points)

    # save data from pilot points in extra lists for the interpolation
    x_coord_pp = pilot_points.loc[:, "x_coord"]
    x_coord_arr = np.zeros((x_coord_pp.shape[0], 1))
    for i in range(x_coord_pp.shape[0]):
        x_coord_arr[i,0] = x_coord_pp[i]
    # x_coord_arr = x_coord_arr.transpose()    
    print('x_coord_arr: \n', x_coord_arr)

    y_coord_pp = pilot_points.loc[:, "y_coord"]
    y_coord_arr = np.zeros((y_coord_pp.shape[0], 1))
    for i in range(y_coord_pp.shape[0]):
        y_coord_arr[i,0] = y_coord_pp[i]
    # x_coord_arr = x_coord_arr.transpose()    
    print('y_coord_arr: \n', y_coord_arr)

    permeability_pp = pilot_points.loc[:, "permeability"]
    permeability_arr = np.zeros((permeability_pp.shape[0], 1))
    for i in range(permeability_pp.shape[0]):
        permeability_arr[i,0] = permeability_pp[i]
    # x_coord_arr = x_coord_arr.transpose()    
    print('permeability_arr: \n', permeability_arr)
    print('log permeability_arr: \n', np.log(permeability_arr))

    # print('x_coordintes:\n ', x_coord_pp)
    # print('x_coordintes:\n ', y_coord_pp)
    # print('permeability values at PPoints: \n', permeability_pp)
    # print(type(permeability_pp))

    # log transform the interpolated values
    permeability_arr = np.log(permeability_arr)

    # get grid information
    x_grid, y_grid = read_grid()

    # call the interpolation Rbf
    rbf_function = interpolate.Rbf(x_coord_arr, y_coord_arr, permeability_arr, function='thin_plate')
    interpolated_permeability = rbf_function(x_grid, y_grid)
    print('transformed interpolated permeability: \n', interpolated_permeability)

    # inv-log transform the interpolated values
    interpolated_permeability = np.exp(interpolated_permeability)
    print('interpolated permeability: \n', interpolated_permeability)

    # save grid as np array
    cells_grid = np.array([x_grid, y_grid])
    print('\ncells_grid: \n', cells_grid)
    # writes the permeability file from the guessed permeability on the grid cells
    write_permeability_file(interpolated_permeability, cells_grid)

    # Print the created h5 file
    filename = "../PFLOTRAN/permeability_values.h5"
    interpolated_points = read_output_file(filename)
    print(interpolated_points)




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
    iarray = np.arange(1, permeability_array.shape[0] + 1, 1)

    if iarray.shape[0] == permeability_array.shape[0] and iarray.shape[0] == cells_grid.shape[1]:
        print("\n[debug] yes: number of cells matches the number od permeability values")
    else:
        print("\n[debug] no: number of cells doesn't matche the number od permeability values")
    print(cells_grid.shape[0])
    # print('\niarray (cell indices) :', iarray)

    file = h5py.File("../PFLOTRAN/permeability_values.h5", "w") #open/create the hdf5 file
    cell_ids = file.create_dataset("Cell Ids", (iarray.shape[0],))
    perm_vals = file.create_dataset("Permeability", (permeability_array.shape[0],))
    for i in range(0,iarray.shape[0]):
        cell_ids[i] = iarray[i]
        perm_vals[i] = permeability_array[i]
    print('\ncell_ids: \n', cell_ids)
    print('\nperm_values: \n', perm_vals)



def read_grid():
    # reads grid file in .h5 format
    filename = '../PFLOTRAN/pflotran_boxmodel.h5'

    with h5py.File(filename, "r") as file:
        
        debug = True
        if debug:
            # List all groups
            a_group_key = list(file.keys())[0]
            print('\nGroup keys in input h5 file: \n', a_group_key )

        dataset = file['Domain']

        list_data_XC = [key for key in dataset['XC']]
        list_data_YC = [key for key in dataset['YC']]
    return list_data_XC, list_data_YC


def read_output_file(filename):
    with h5py.File(filename, "r") as file:
        
        debug = True
        if debug:
            # List all groups [debugging]
            a_group_key = list(file.keys())
            print('\nGroup keys in created h5 file: \n', a_group_key )

        # dataset = file['Permeability']

        list_data_XC = [key for key in file['Cell Ids']]
        list_data_YC = [key for key in file['Permeability']]
    return list_data_XC, list_data_YC    


if __name__ == '__main__':
    interpolation_main()


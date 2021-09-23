import os
import pandas as pd
import csv
import h5py

def define_grid():
    filename = 'Boxmodel/PFLOTRAN/pflotran_boxmodel.h5'

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
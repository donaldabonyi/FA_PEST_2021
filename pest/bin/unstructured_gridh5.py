import os
import pandas as pd
import numpy as np
import h5py
from scipy.interpolate import Rbf
import csv
from pathlib import Path

#ROOT = r"/Users/e1073/PEST_Files_FA2021/test_model"
#RAW_PATH = Path(ROOT,'test_explicit_Domain.h5')
'''
filename = 'pflotran_boxmodel.h5'

list_data_XC = ['XC']
list_data_YC = ['YC']
with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
    a_group_key2 = list(f.keys())[1]

    # Get the data
    data = list(f[a_group_key])

    #print(data)

    dset = f['Domain']
    #print([key for key in dset.keys()])
    #print([value for value in dset.values()])

    x_cord = dset['XC']
    y_cord = dset['YC']
    print(x_cord)

    data_xc = [key for key in x_cord]
    list_data_XC.append(data_xc)
    data_yc = [key for key in y_cord]
    list_data_YC.append(data_yc)
    print(list_data_YC[1][0])
    #print([value for value in x_cord.values()])
'''
with open('permpp.dat') as dat_file, open('file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in dat_file:
        row = [field.strip() for field in line.split()]
        csv_writer.writerow(row)

Cov = pd.read_csv("file.csv", sep='\t', names=["pilot_point", "x_c", "y_c", "n", "permeability"])

print(Cov)

#sub_file = 'file.csv'
#pilot_point_file = pd.read_csv(sub_file)



#data = pd.read_csv('file.dat', sep='|', header=0, skipinitialspace=True)
#data.dropna(inplace=True)

# read flash.dat to a list of lists
#data_pilot = [i.strip().split() for i in open("permpp.dat").readlines()]

# write it as a new CSV file
#with open("flash.csv", "wb") as f:
  #  writer = csv.writer(f)
   # writer.writerows(data_pilot)

#print(data_pilot)





#filename2 = 'test_explicit_Domain.h5'

#with h5py.File(filename2, "r") as f:
    #print("Keys: %s" % f.keys())
    #b_group_key = list(f.keys())[0]
    #b_group_key2 = list(f.keys())[1]

    #data3 = list(f[b_group_key])

    #print(data3)
    #print(data3.shape)
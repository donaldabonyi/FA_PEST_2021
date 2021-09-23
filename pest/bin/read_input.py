import csv
import pandas as pd

def read_input():
    # read pilot points
    with open('Boxmodel/Data/permpp.dat') as dat_file, open('permpp.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        for line in dat_file:
            row = [field.strip() for field in line.split()]
            csv_writer.writerow(row)

    data = pd.read_csv('permpp.csv', names=["ID", "x_coord", "y_coord", "n", "permeability"])
    return data
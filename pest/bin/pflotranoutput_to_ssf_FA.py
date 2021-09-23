# Script to gather PFLOTRAN observation outputs and convert the tecplot format to TSPROC ssf format

import glob
import numpy as np
import datetime

#################
#Set a start date
#################
start_date="11/10/1991 12:00:00"

#################
#Set the timestep interval for time series export
#################
timeStep = 0.001	#unit in days

# get PFLOTRAN observation files
filename = 'pflotran-obs-0.tec'

with open(filename, 'r') as f:
    lines = f.readlines()
    words = lines[2].split("  ")

array = ""
i = 1
for x in words[2:]:
    array += 'obs_'+ str(i) + ' ' + start_date + ' ' + x + '\n'
    i += 1

file_out = open('pflotran_output.ssf', "w")
file_out.write(array)
        
        # --------Writing SSF file --------------  
        
        # File must be written in form
        
        # obs_1 11/10/1991 12:01:26 12.00(=permeability)
        # obs_2 11/10/1991 12:01:26 11.83
        # obs_3 11/10/1991 12:01:26 12.81
        # '''

## Output file with name "pflotran_output.ssf" in PFLOTRAN location

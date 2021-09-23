#!/bin/bash

# pilot points preprocessing
python3 ../bin/interpolation.py

rm ../PFLOTRAN/*.tec # remove old output
mpirun -n 1 pflotran -input_prefix ../PFLOTRAN/pflotran_boxmodel > log.pflotran #on SNG
python3 ../bin/pflotranoutput_to_ssf_FA.py # converter
cd ../PEST
tsproc < ../PEST/tsproc.in # runs tsproc

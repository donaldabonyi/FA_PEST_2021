open simulation_run.sh
simulation_run.sh calls pestpp with pestfile_regul.pst
    
    pestfile_regul.pst
     - loads pilot pilot point positions (4)
     - loads observation points (16)
     - loads observation values (16)
     switches to command line and calls model_command_FA.bat
     
        model_command_FA.bat
        - calls interpolation.py

            interpolation.py
            - reads pilot point positions(x,y) and values(z) from permpp.dat
            - compute rbf(x,y)
            - reads mesh from pflotran_boxmodel.h5 and set up xi,yi
            - evaluate rbf on every (xi,yi) and write it to a matrix: [x y value]
            - write this to permeability.h5

        - remove old pflotran output "*.tec" file
        - runs pflotran with pflotran_boxmodel.* files
        - calls pflotranoutput_to_ssf_FA.py: converts pflotran output to ssf
        - calls tsproc

    switches to input/output mode
    - writes pilot points to permpp.dat
    
    switches to regularization mode  
             


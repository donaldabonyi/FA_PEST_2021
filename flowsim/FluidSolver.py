import os
#import owncloud
#from NextCloudUploader import NextCloudUploader

from FlowModel import Model

class FluidSolver:
    def __init__(self, model, num_procs=1):
        self.model = model
        self.num_procs = num_procs


    #requires variable PFLOTRAN_DIR to be set to the PFLOTRAN installation directory (without '/' at the end)
    def run(self):
        self.write_input_file()
        os.system(f"mpirun -n {self.num_procs} $PFLOTRAN_DIR/src/pflotran/pflotran")
        observation_results = self.parse_observation_results()
        return observation_results
        
    def write_input_file(self):
        with open('pflotran.in', 'w') as pfile:
            pfile.write(self.model.to_pflotran())


    def parse_observation_results(self):
        #somemagic
        return []


    #def upload_to_nextcloud(self, path_to_copy_from, nextcloud_folder, name, username, password):
    #    NextCloudUploader.upload_to_nextcloud(path_to_copy_from, nextcloud_folder, name, username, password)



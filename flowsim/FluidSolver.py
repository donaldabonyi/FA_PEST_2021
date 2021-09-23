from ObservationResult import ObservationResult
from ObservationPoint import ObservationPoint, Quantity
from Position import Position
import os
import owncloud
from NextCloudUploader import NextCloudUploader

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

    #Parses a pflotran observation file with observation results and returns an ObservationResult object
    #note that currently, only observations of one quantity (e.g. pressure) can be parsed, not multiple (e.g. temperature and pressure)
    def parse_observation_results(self, filename):
        with open(filename, 'r') as outputfile:
            data = {}
            for line in outputfile:
                values = line.strip().rsplit(' ')
                if(line.startswith('\"')): #first line of the file: get position, id and quantity from here
                    id = values[3]
                    if('C' in values[2]): quantity = Quantity(1)
                    if('P' in values[2]): quantity = Quantity(2)
                    if('' in values[2]): quantity = Quantity(3) #TODO: insert symbol for permeability here
                    positionX = "".join([char for char in values[4] if char.isdigit()])
                    positionY = "".join([char for char in values[5] if char.isdigit()])
                    positionZ = "".join([char for char in values[6] if char.isdigit()])
                else:
                    data[values[0]] = values[1]

            return ObservationResult(ObservationPoint(id, Position(positionX, positionY, positionZ), quantity), data)


    #Uploads all vtk files in specified path to nextcloud as zip with specified name into specified
    # nextcloudfolder. !! zip_file_name should have .zip ending"
    def upload_to_nextcloud(self, path_to_zip_from, nextcloud_folder_path, zip_file_name):
        NextCloudUploader.upload_to_nextcloud(path_to_zip_from, nextcloud_folder_path, zip_file_name)



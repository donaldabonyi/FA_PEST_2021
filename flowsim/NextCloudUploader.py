import os

import owncloud
from os.path import basename
from zipfile import ZipFile

class NextCloudUploader:
    @staticmethod
    def upload_to_nextcloud( path_to_copy_from, cloud_folder_path, name):

        zip_filename = os.path.join(path_to_copy_from, name)
        with ZipFile(zip_filename, 'w') as zip_object:

            for root, dir, filenames in os.walk(path_to_copy_from):
                for vfile in filenames:
                    if vfile.endswith('.vtk'):
                        filepath = os.path.join(root, vfile)
                        zip_object.write(filepath, basename(filepath))


        oc = owncloud.Client.from_public_link("https://nextcloud.fa/apps/files/?dir=/FlowSimData")

        oc.login("up_test", "up_test123")

        oc.put_file(cloud_folder_path +"/" + name, zip_filename)


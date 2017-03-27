import os
import zipfile
from os.path import basename
from FilePaths import in_download, in_models, in_root


def append_file(fd_to, file_path):
    with open(file_path, 'r') as fd:
        for line in fd:
            fd_to.write(line)
    os.remove(file_path)


def zip_objects():
    with zipfile.ZipFile(in_download('objects.zip'), 'w') as zip_fd:
        # zip_fd.write(in_models('model.mesh'), basename('model.mesh'))
        zip_fd.write(in_models('model.obj'), basename("model.obj"))


def remove_temps():
    try:
        os.remove(in_models('texture_temp.obj'))
    except (FileExistsError, FileNotFoundError):
        print('Failed attempt to remove texture temp')
    try:
        os.remove(in_models('normal_temp.obj'))
    except (FileExistsError, FileNotFoundError):
        print('Failed attempt to remove normal temp')
    try:
        os.remove(in_models('face_temp.obj'))
    except (FileExistsError, FileNotFoundError):
        print('Failed attempt to remove face temp')

# The following are not in use


# TODO: use subprocess
def convert_mesh():
    os.system("start /wait cmd /c OgreXMLConverter {}".format(in_models("model.mesh.xml")))
import os
import zipfile
from os.path import basename
from FilePaths import in_download, in_models, in_root


# TODO: use subprocess
def convert_mesh():
    os.system("start /wait cmd /c OgreXMLConverter {}".format(in_models("model.mesh.xml")))


def zip_objects():
    with zipfile.ZipFile(in_download('objects.zip'), 'w') as zip_fd:
        zip_fd.write(in_models('model.mesh'), basename('model.mesh'))
        zip_fd.write(in_models('model.obj'), basename("model.obj"))

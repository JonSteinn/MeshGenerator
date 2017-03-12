import os
import zipfile
from os.path import basename

# TODO: remove abs path
def zip_objects():
    with zipfile.ZipFile('/Users/Jonni/Desktop/mesh/static/models/download/objects.zip', 'w') as zip_fd:
        zip_fd.write('/Users/Jonni/Desktop/mesh/static/models/model.obj', basename("model.obj"))
        zip_fd.close()
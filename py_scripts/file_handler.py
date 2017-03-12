import zipfile
from os.path import basename

from FilePaths import in_download, in_models


def zip_objects():
    with zipfile.ZipFile(in_download('objects.zip'), 'w') as zip_fd:
        zip_fd.write(in_models('model.obj'), basename("model.obj"))
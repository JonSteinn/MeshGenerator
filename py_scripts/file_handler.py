import zipfile
from os.path import basename

from FilePaths import inDownload


def zip_objects():
    with zipfile.ZipFile(inDownload('objects.zip'), 'w') as zip_fd:
        zip_fd.write(inDownload('model.obj'), basename("model.obj"))
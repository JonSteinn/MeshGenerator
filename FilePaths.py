import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
MODELS_ROOT = os.path.join(STATIC_ROOT, 'models')
DOWNLOAD_ROOT = os.path.join(MODELS_ROOT, 'download')


def in_download(filename):
    return os.path.join(DOWNLOAD_ROOT, filename)


def in_models(filename):
    return os.path.join(MODELS_ROOT, filename)


def in_root(filename):
    return os.path.join(APP_ROOT, filename)
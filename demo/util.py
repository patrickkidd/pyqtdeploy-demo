from PyQt5.QtCore import QFileInfo

# Qt file-io prefix for loading resources in the project dir
# that works both for dev and in the bundle.
QRC = QFileInfo(__file__).absolutePath() + '/resources/'

def resource_path(relative_path):
    """ Load a resource relative to the demo source dir. """
    return f"{QRC}{relative_path}"
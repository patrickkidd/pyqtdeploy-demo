import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication

from . import util, demo

def main():
    """ Entry point called by A) pyqtdeploy bundle, and B) main.py for local dev. """
    
    app = QApplication(sys.argv)

    # Ensure resources can be loaded from the source dir
    assert not QPixmap(util.resource_path('delete-button.png')).isNull()

    mainWidget = demo.MainWidget()
    mainWidget.show()
    app.exec()
    

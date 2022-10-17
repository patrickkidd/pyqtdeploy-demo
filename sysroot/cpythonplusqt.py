import os, sys, shutil
from pyqtdeploy import Component, ComponentOption, ExtensionModule


class CPythonPlusQtComponent(Component):
    """ The vedana module component. """

    must_install_from_source = False
    preinstalls = ['SIP']
    provides = {
        '_cpythonplusqt': ExtensionModule(
            source=[
                "../../../cpythonplusqt/_cpythonplusqt.cpp",
            ]
        )
    }

    def get_archive_name(self):
        return ''

    def install(self):
        pass

import os, sys, shutil
from pyqtdeploy import Component, ComponentOption, ExtensionModule


class CPythonOnlyComponent(Component):
    """ The vedana module component. """

    must_install_from_source = False
    preinstalls = ['SIP']
    provides = {
        '_cpythononly': ExtensionModule(
            source=[
                "../../../cpythononly/_cpythononly.cpp",
            ]
        )
    }

    def get_archive_name(self):
        return ''

    def install(self):
        pass

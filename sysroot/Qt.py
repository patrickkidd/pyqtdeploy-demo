import os.path
from pyqtdeploy.sysroot.plugins.Qt import QtComponent

class DemoQtComponent(QtComponent):

    def run(self, *args, capture=False):
        """ Run a command, optionally capturing stdout. """
        if args[0] == self.host_make:
            self.verbose('Adding args for concurrent build.')
            _args = args + ('-j16',)
        else:
            _args = args
        return super().run(*_args, capture=capture)

    def unpack_archive(self, archive, chdir=True):
        """ Override to patch 5.15+ on macos
        """
        archive_root = super().unpack_archive(archive, chdir)

        # Patch Qt-5.15+ on macOS.

        if self.target_platform_name == 'macos':
            self.patch_file(
                'qtbase/src/plugins/platforms/cocoa/qiosurfacegraphicsbuffer.h',
                self._patch_qiosurfacegraphicsbuffer
            )

        return archive_root

    @staticmethod
    def _patch_qiosurfacegraphicsbuffer(line, patch_file):
        """ Qt-5.15 does not build on at least macOS Monterey.
        """

        patch_file.write(
            line.replace(
                '#include <qpa/qplatformgraphicsbuffer.h>',
                '#include <CoreGraphics/CoreGraphics.h>\n#include <qpa/qplatformgraphicsbuffer.h>'
            )
        )

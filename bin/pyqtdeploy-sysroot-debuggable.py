""" Useful as a debug target for pyqtdeploy-sysroot. """

import os, os.path, sys
from pyqtdeploy import pyqtdeploysysroot_main

# path = os.path.abspath(os.path.join(__file__, '..', '..', 'vendor'))
# os.chdir(path)

sys.argv += [ "--verbose", "sysroot.toml" ]

pyqtdeploysysroot_main.main()

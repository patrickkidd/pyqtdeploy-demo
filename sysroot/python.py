from pyqtdeploy.sysroot.plugins.Python import PythonComponent

class DemoPythonComponent(PythonComponent):

    def run(self, *args, capture=False):
        """ Add multiprocessing to make. """
        if args[0] == self.host_make:
            self.verbose('Adding args for concurrent build.')
            _args = args + ('-j16',)
        else:
            _args = args
        return super().run(*_args, capture=capture)


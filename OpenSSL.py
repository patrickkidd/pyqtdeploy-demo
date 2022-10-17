from pyqtdeploy.sysroot.plugins.OpenSSL import OpenSSLComponent

class DemoOpenSSLComponent(OpenSSLComponent):

    def run(self, *args, capture=False):
        """ Add multiprocessing to make. """
        if args[0] == self.host_make:
            self.verbose('Adding args for concurrent build.')
            _args = args + ('-j16',)
        else:
            _args = args
        return super().run(*_args, capture=capture)


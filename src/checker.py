import os
import glob

class Checker():

    def __init__(self, configuration):
        self.configuration = configuration

    def run(self):
        try:
            self.configuration.validate()
        except OSError:
            print(self.configuration.NO_CONFIG_FILE_WARNING)

        self.check()

    def check(self):
        self.get_checks()

    def get_checks(self):
        check_files = []
        built_in_checks = glob.glob('./checks/**/*', recursive = True)

        if self.configuration.has_custom_checks(self.configuration.get_configuration_directory()):
            custom_checks = glob.glob(
                self.configuration.get_configuration_directory() + '/**/*',
                recursive = True
            )

            check_files += custom_checks

        check_files += built_in_checks
        print (check_files)

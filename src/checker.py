import os
import glob

class Checker():

    def __init__(self, configuration):
        self.configuration = configuration

    def run(self):
        self.configuration.validate()
        self.check()

    def check(self):
        self.get_checks()
        print('check here')

    def get_checks(self):
        check_files = []
        built_in_checks = glob.glob('./checks/**/*.sh', recursive=True)

        if self.configuration.has_custom_checks(self.configuration.get_configuration_directory()):
            custom_checks = glob.glob(self.configuration.get_configuration_directory() + '/**/*')

        check_files += built_in_checks
        print (check_files)

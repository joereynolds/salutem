import os
import glob
import importlib

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
        checks = self.get_checks()
        # print(checks)
        self.run_checks(checks)

    def get_checks(self):
        check_files = []
        built_in_checks = glob.glob('./checks/**/*.py', recursive = True)

        if self.configuration.has_custom_checks(self.configuration.get_configuration_directory()):
            custom_checks = glob.glob(
                self.configuration.get_configuration_directory() + '/**/*.py',
                recursive = True
            )

            check_files += custom_checks

        check_files += built_in_checks

        return check_files

    def run_checks(self, checks):
        for check in checks:
            formatted_check = self.convert_path_to_import(check)
            module = importlib.import_module(formatted_check)
            module.check()

    def convert_path_to_import(self, file_path):
        if file_path.startswith('./'):
            file_path = file_path[2:]

        file_path = file_path.replace('/', '.')
        file_path = file_path.replace('.py', '')

        return file_path




import os
import glob
import importlib
import subprocess


class Checker():


    def __init__(self, configuration, printer):
        self.configuration = configuration
        self.printer = printer

    def run(self):
        try:
            self.configuration.validate()
        except OSError:
            print(self.configuration.NO_CONFIG_FILE_WARNING)

        self.check()

    def check(self):
        checks = self.get_checks()
        self.run_checks(checks)

    def get_checks(self):
        check_files = glob.glob('./checks/**/*', recursive = True)

        if self.configuration.has_custom_checks(self.configuration.get_configuration_directory()):
            custom_checks = glob.glob(
                self.configuration.get_configuration_directory() + '/**/*',
                recursive = True
            )

            check_files += custom_checks

        return check_files

    def run_checks(self, checks):
        for check in checks:
            formatted_check = self.convert_path_to_import(check)

            _, extension = os.path.splitext(check)

            if extension == '.py':
                module = importlib.import_module(formatted_check)
                try:
                    module.check()
                    self.printer.print_success(check)
                    continue
                except Exception as err:
                    self.printer.print_failure(check, err)


    def convert_path_to_import(self, file_path):
        if file_path.startswith('./'):
            file_path = file_path[2:]

        file_path = file_path.replace('/', '.')
        file_path = file_path.replace('.py', '')

        return file_path

import os
import glob
import importlib
import subprocess

from src.check import Check


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
        checks_before_run = self.get_checks()
        checks_after_run = self.run_checks(checks_before_run)
        self.print_checks_after_run(checks_after_run)

    def get_checks(self):
        """Returns all of our custom checks to run"""
        check_files = glob.glob('./checks/**/*', recursive = True)

        if self.configuration.has_custom_checks(self.configuration.get_configuration_directory()):
            custom_checks = glob.glob(
                self.configuration.get_configuration_directory() + '/**/*',
                recursive = True
            )

            check_files += custom_checks

        return check_files

    def run_checks(self, checks):
        """Returns a list of all checks, including
        whether they succeeded or failed and if they failed,
        the error message."""

        check_statuses = []

        for check_path in checks:
            check = Check(check_path)
            check.run()
            check_statuses.append(check)

        return check_statuses

    def print_checks_after_run(self, checks_after_run):
        for check in checks_after_run:
            if check.extension == '.py':
                if check.status == check.SUCCEEDED:
                    self.printer.print_success(check.path)
                if check.status == check.FAILED:
                    self.printer.print_failure(
                        check.path,
                        check.message
                    )

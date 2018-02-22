import argparse

class Salutem():

    def __init__(self, checker):
        self.checker = checker

    def run(self):
        self.add_help_options()
        self.checker.run()

    def add_help_options(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--colored',
            '-c',
            action='store_true',
            help='Show ANSI color codes for a checks status.'
        )

        parser.add_argument(
            '--stop-on-failure',
            '-s',
            action='store_true',
            help='Stop checking on the first failed check encountered.'
        )

        parser.add_argument(
            '--only-show-failures',
            '-o',
            action='store_true',
            help='Only show failed checks.'
        )

        parser.add_argument(
            '--get-checks',
            '-l',
            action='store_true',
            help='Show all checks in use'
        )

        args = parser.parse_args()

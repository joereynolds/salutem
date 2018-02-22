import os

class Configuration():

    NO_CONFIG_FILE_WARNING = """
        No custom check directory found.
        You can create one under the default
        ~/.config/salutem/checks
        or create your own and edit the
        configuration file.
    """

    def __init__(self, check_directory):
        self.config = check_directory

    def validate(self):
        if not self.has_custom_checks(self.config):
            print(Configuration.NO_CONFIG_FILE_WARNING)

    def has_custom_checks(self, check_directory):
        return os.path.isdir(check_directory)

    def get_configuration_directory(self):
        return self.config

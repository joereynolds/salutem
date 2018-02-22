import os

class Configuration():

    NO_CONFIG_FILE_WARNING = """
        No custom check directory found.
        You can create one under the default
        ~/.config/salutem/checks
        or create your own and edit the
        configuration file.
    """

    def __init__(self, directory):
        self.directory = directory

    def validate(self):
        if not self.has_custom_checks(self.directory):
            raise OSError('File ' + self.directory + ' does not exist')

    def has_custom_checks(self, directory):
        return os.path.isdir(directory)

    def get_configuration_directory(self):
        return self.directory

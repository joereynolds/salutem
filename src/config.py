import os

class Configuration():

    NO_CONFIG_FILE_WARNING = """
        No custom check directory found.
        You can create one under
        ~/.config/salutem/checks
    """

    def __init__(
            self,
            directory,
            stop_on_failure = False,
            only_show_failures = False
        ):

        self.directory = directory
        self.stop_on_failure = stop_on_failure
        self.only_show_failures = only_show_failures

    def validate(self):
        if not self.has_custom_checks(self.directory):
            raise OSError('File ' + self.directory + ' does not exist')

    def has_custom_checks(self, directory):
        return os.path.isdir(directory)

    def get_configuration_directory(self):
        return self.directory

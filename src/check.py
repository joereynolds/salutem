import os
import importlib


class Check():

    FAILED = 'failed'
    SUCCEEDED = 'succeeded'
    EXTENSION = '.py'

    def __init__(self, path):
        self.path = path
        self.import_path = self.get_import_path(self.path)
        self.extension = self.get_extension(self.path)
        self.status = ''
        self.message = ''
        self.name = self.get_friendly_name()

    def get_friendly_name(self):
        if self.extension == self.EXTENSION:
            module = importlib.import_module(self.import_path)
            try:
                return module.name
            except AttributeError:
                return ''

    def get_extension(self, path):
        _, extension = os.path.splitext(path)
        return extension

    def get_import_path(self, path):
        if path.startswith('./'):
            path = path[2:]

        path = path.replace('/', '.')
        path = path.replace(self.EXTENSION, '')

        return path

    def run(self):
        if self.extension == self.EXTENSION:
            module = importlib.import_module(self.import_path)
            try:
                module.check()
                self.status = self.SUCCEEDED
            # TODO dont obliterate Exception,
            # create a custom exception
            except Exception as err:
                self.status = self.FAILED
                self.message = err

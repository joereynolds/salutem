import unittest
from src.config import Configuration


class TestConfiguration(unittest.TestCase):

    def setUp(self):
        self.configuration = Configuration('/non/existent/directory')

    def test_configuration_is_instantiable(self):
        self.assertIsInstance(self.configuration, Configuration)

    def test_configuration_throws_a_warning_if_no_config_directory_found(self):
        self.assertRaises(OSError, self.configuration.validate)


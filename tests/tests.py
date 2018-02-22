import unittest
from salutem.src import Checker
from src import Checker
# from src import Configuration

class TestChecker(unittest.TestCase):

    def test_check_is_instantiable():
        check = Checker(Configuration('~/.config/salutem/checks'))
        pass


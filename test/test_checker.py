import unittest
from src.checker import Checker
from src.config import Configuration

class TestChecker(unittest.TestCase):

    def test_check_is_instantiable(self):
        check = Checker(Configuration('~/.config/salutem/checks'))
        self.assertIsInstance(check, Checker)


if __name__ == '__main__':
    unittest.main()

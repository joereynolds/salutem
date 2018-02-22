from src.checker import Checker
from src.config import Configuration
from src.salutem import Salutem

if __name__ == '__main__':
    salutem = Salutem(Checker(Configuration('/home/joe/.config/salutem/checks')))
    salutem.run()

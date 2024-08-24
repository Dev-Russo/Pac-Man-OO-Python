from character import *

class Ghost(Character):
    def __init__(self) -> None:
        super().__init__()
        self.__eaten = False

    def getEaten(self):
        return self.__eaten

    def setEaten(self, value):
        self.__eaten = value
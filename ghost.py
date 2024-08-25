from character import *
from player import *

class Ghost(Character):
    def __init__(self) -> None:
        super().__init__()
        self.__eaten = False
        self.__targets = None
        self.__dead = False
        self.__inthebox = False

    def getEaten(self):
        return self.__eaten

    def setEaten(self, value):
        self.__eaten = value
    
    def getTarget(self):
        return self.__targets

    def setTarget(self, value):
        self.__targets = value

    def getDead(self):
        return self.__dead

    def setDead(self, value):
        self.__dead = value

    def getInthebox(self):
        return self.__inthebox

    def setInthebox(self, value):
        self.__inthebox = value
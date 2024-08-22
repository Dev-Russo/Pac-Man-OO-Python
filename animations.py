from settings import *

class Animation:
    def __init__(self) -> None:
       self.__flink = False
       self.__counter = 0  

    def setFlink(self, value):
        self.__flink = value
    
    def getFlink(self):
        return self.__flink

    def getCounter(self):
        return self.__counter
    
    def setCounter(self, value):
        self.__counter = value

    def up_counter(self):
        if self.getCounter() < 19:
            self.setCounter(self.getCounter() + 1)
            if self.getCounter() > 3:
                self.setFlink(False)
        else:
            self.setCounter(0)
            self.setFlink(True)
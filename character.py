import pygame
from settings import *

class Character:
    def __init__(self, character_x, character_y, character_speed) -> None:
        self.__character_x = character_x
        self.__character_y = character_y
        self.__center_x = character_x
        self.__center_y = character_y 
        self.__character_speed = character_speed
        self.__direction = 0
        self.__direction_comand = None  # Inicializa o comando de direção
        self.__turns_allowed = [False, False, False, False]
        self.__startup_counter = 0
        self.__moving = False

    
    def getStartup_counter(self):
        return self.__startup_counter
    
    def setStartup_counter(self, value):
        self.__startup_counter = value

    def getMoving(self):
        return self.__moving
    
    def setMoving(self, value):
        self.__moving = value

    def getTurns_allowed(self):
        return self.__turns_allowed
    
    def setTurns_allowed(self, value):
        self.__turns_allowed = value

    def getCharacter_speed(self):
        return self.__character_speed
    
    def setCharacter_speed(self, value):
        self.__character_speed = value

    def getCenter_x(self):
        return self.__center_x

    def getCenter_y(self):
        return self.__center_y

    def setCenter_x(self, value):
        self.__center_x = value
    
    def setCenter_y(self, value):
        self.__center_y = value

    def getCharacter_x(self):
        return self.__character_x
    
    def getCharacter_y(self):
        return self.__character_y
    
    def setCharacter_x(self, value):
        self.__character_x = value
    
    def setCharacter_y(self, value):
        self.__character_y = value

    def getDirection(self):
        return self.__direction
    
    def setDirection(self, value):
        self.__direction = value

    def getDirection_comand(self):
        return self.__direction_comand
    
    def setDirection_comand(self, value):
        self.__direction_comand = value

    def move(self, characterx, charactery):
        if self.getDirection() == 0 and self.getTurns_allowed()[0]:
            self.setCharacter_x(characterx + self.getCharacter_speed())
        elif self.getDirection() == 1 and self.getTurns_allowed()[1]:
            self.setCharacter_x(characterx - self.getCharacter_speed())
        elif self.getDirection() == 2 and self.getTurns_allowed()[2]:
            self.setCharacter_y(charactery + self.getCharacter_speed())
        elif self.getDirection() == 3 and self.getTurns_allowed()[3]:
            self.setCharacter_y(charactery - self.getCharacter_speed())

        self.setCenter_x(self.getCharacter_x() + 23)
        self.setCenter_y(self.getCharacter_y() + 24)

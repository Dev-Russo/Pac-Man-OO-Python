import pygame
from settings import *

class Character:
    def __init__(self, character_x, character_y) -> None:
        self.__character_x = character_x
        self.__character_y = character_y


    def getCharacter_x(self):
        return self.__character_x
    
    def getCharacter_y(self):
        return self.__character_y
    
    def setCharacter_x(self, value):
        self.__character_x = value
    
    def setCharacter_y(self, value):
        self.__character_y = value
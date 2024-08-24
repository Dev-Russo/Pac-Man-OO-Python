import pygame
from settings import *

class ScoreManager:
    def __init__(self) -> None:
        self.__score = 0

    def setScore(self, value):
        self.__score = value

    def getScore(self):
        return self.__score
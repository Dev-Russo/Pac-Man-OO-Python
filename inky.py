import pygame
from settings import *
from ghost import *
from character import *

class Inky(Ghost):
    def __init__(self) -> None:
        super().__init__(character_x=440, character_y=438, character_speed=2)
        self.setDirection(2)
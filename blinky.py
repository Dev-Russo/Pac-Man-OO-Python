import pygame
from settings import *
from ghost import *
from character import *

class Blinky(Ghost):
    def __init__(self) -> None:
        super().__init__(character_x = 56, character_y = 58, character_speed = 2)
        
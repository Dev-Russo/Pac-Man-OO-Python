import pygame
from settings import *
from ghost import *
from character import *

class Pinky(Ghost):
    def __init__(self) -> None:
        super().__init__(character_x=440, character_y=438, character_speed=2, img=pinky_img)
        self.setDirection(2)

    def draw(self, screen, player):
        return super().draw(screen, player)
    
    def check_collision(self, tile):
        return super().check_collision(tile)
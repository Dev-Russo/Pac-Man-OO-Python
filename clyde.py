import pygame
from settings import *
from ghost import *
from character import *

class Clyde(Ghost):
    def __init__(self) -> None:
        super().__init__(character_x=440, character_y=438, character_speed=2, img=clyde_img)
        self.setDirection(2)
        self.update_center()

    def draw(self, screen, player):
        return super().draw(screen, player)
    
    def check_collision(self, tile, centerx, centery):
        #print(centerx)
        return super().check_collision(tile, centerx, centery)
    
    def move_ghost(self):
        return super().move_ghost()

    def update_target(self, player):
        return_target = (380, 400)
        if player.getPowerup():
            if not self.getDead() and not self.getEaten():
                self.setTarget([450, 450])
            elif not self.getDead() and self.getEaten():
                if 340 < self.getCharacter_x() < 560 and 340 < self.getCharacter_y() < 500:
                    self.setTarget([400, 100])
                else:
                    self.setTarget([player.getCharacter_x(), player.getCharacter_y()])
            else:
                self.setTarget(return_target)
        else:
            if not self.getDead():
                if 340 < self.getCharacter_x() < 560 and 340 < self.getCharacter_y() < 500:
                    self.setTarget([400, 100])
                else:
                    self.setTarget([player.getCharacter_x(), player.getCharacter_y()])
            else:
                self.setTarget(return_target)
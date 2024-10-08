import pygame
from settings import *
from ghost import *
from character import *

class Inky(Ghost):
    def __init__(self) -> None:
        super().__init__(character_x=440, character_y=388, character_speed=2, img = inky_img)
        self.update_center()



    def draw(self, screen, player):
        return super().draw(screen, player)
    
    def move_ghost(self, turn_pattern):
        if turn_pattern:
            return super().move_ghost()
        else:
            if self.getDirection() == 0:
                if self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                    self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif not self.getTurns_allowed()[0]:
                    if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                elif self.getTurns_allowed()[0]:
                    if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    if self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    else:
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())

            elif self.getDirection() == 1:
                if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                    self.setDirection(3)
                elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                    self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                elif not self.getTurns_allowed()[1]:
                    if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                    elif self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif self.getTurns_allowed()[1]:
                    if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    if self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    else:
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())

            elif self.getDirection() == 2:
                if self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                    self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                elif not self.getTurns_allowed()[2]:
                    if self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                    elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                    elif self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[3]:
                        self.setDirection(3)
                        self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                    elif self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif self.getTurns_allowed()[2]:
                    self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())

            elif self.getDirection() == 3:
                if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                    self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
                elif not self.getTurns_allowed()[3]:
                    if self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                    elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                    elif self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[2]:
                        self.setDirection(2)
                        self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[1]:
                        self.setDirection(1)
                        self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                    elif self.getTurns_allowed()[0]:
                        self.setDirection(0)
                        self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif self.getTurns_allowed()[3]:
                    self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())

            if self.getCharacter_x() < -30:
                self.setCharacter_x(900)
            elif self.getCharacter_x() > 900:
                self.setCharacter_x(-30)


            self.update_center()
            
            return self.getCharacter_x(), self.getCharacter_y(), self.getDirection()


    
    def check_collision(self, tile, centerx, centery):
        #print(centerx)
        return super().check_collision(tile, centerx, centery)
    
    def update_target(self, player):
        if player.getCharacter_x() < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        return_target = (380, 400)
        if player.getPowerup():
            if not self.getDead() and not self.getEaten():
                self.setTarget([runaway_x, player.getCharacter_y()])
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
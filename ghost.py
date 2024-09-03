from character import *
from player import *

class Ghost(Character):
    def __init__(self, character_x, character_y, character_speed, img) -> None:
        super().__init__(character_x, character_y, character_speed)
        self.__eaten = False
        self.__targets = None
        self.__dead = False
        self.__inthebox = False
        self.__img = img
        self.__inthebox = self.check_collision()
        self.setTurns_allowed(self.check_collision())
        self.__rect = pygame.rect.Rect((self.getCenter_x() - 18, self.getCenter_y() - 18), (36, 36))
    
    def getRect(self):
        return self.__rect
     
    def setRect(self, val):
        self.__rect = val

    def getImage(self):
        return self.__img
    
    def setImage(self, val):
        self.__img = val
    
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

    def draw(self, screen, player):
        if (not player.getPowerup() and not self.getDead()) or (self.getEaten() and player.getPowerup() and not self.getDead()):
            screen.blit(self.getImage(), (self.getCharacter_x(), self.getCenter_y()))
        elif player.getPowerup() and not self.getDead() and not self.getEaten():
            screen.blit(spooked_img, (self.getCharacter_x(), self.getCenter_y()))
        else:
            screen.blit(dead_img, (self.getCharacter_x(), self.getCenter_y()))
        
        self.setRect(pygame.rect.Rect((self.getCenter_x() - 18, self.getCenter_y() - 18), (36 , 36))) 
    
    def check_collision(self):
        return self.getTurns_allowed(), self.getInthebox()


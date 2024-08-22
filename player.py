from settings import *
from character import *
import pygame

class Player(Character):
    def __init__(self, screencharacter) -> None:
        super().__init__(character_x = 450, character_y= 663)
        self.__screencharacter = screencharacter
        self.__direction = 0
        self.__counter = 0
    
    def getScreencharacter(self):
        return self.__screencharacter


    def getDirection(self):
        return self.__direction
    
  
    def getCounter(self):
        return self.__counter
    


            
    def draw_player(self, player_images):
        # 0-Direita, 1-Esquerda, 2-Cima, 3-Baixo
        if self.getDirection() == 0:
            self.getScreencharacter().blit(player_images[self.getCounter() // 5], (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 1:
            #Da um flip na imagem horizontalmente
            flipped_image = pygame.transform.flip(player_images[self.getCounter() // 5], True, False)
            self.getScreencharacter().blit(flipped_image, (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 2:
            rotated_image = pygame.transform.rotate(player_images[self.getCounter() // 5], 90)
            self.getScreencharacter().blit(rotated_image, (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 3:
            rotated_image = pygame.transform.rotate(player_images[self.getCounter() // 5], 270)
            self.getScreencharacter().blit(rotated_image, (self.getCharacter_x(), self.getCharacter_y()))
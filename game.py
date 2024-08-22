import pygame
from tile import *
from settings import *
from player import *

pygame.init()

class Game:
    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode((LARGURA, ALTURA))
        self.__timer = pygame.time.Clock()
        self.__run = True
        self.tile = Tile(self.__screen)


    def getScreen(self):
        return self.__screen
    
    def getTimer(self):
        return self.__timer
    
    def getRun(self):
        return self.__run
    
    def setRun(self, value):
        self.__run = value

    
    def rodar(self):
        while self.getRun():
            self.getTimer().tick(FPS)
            self.getScreen().fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.setRun(False)

            self.tile.draw_board()
            player = Player(self.getScreen())
            player.draw_player(PLAYER_IMAGES)
        
            pygame.display.flip()
        
        pygame.quit()

game = Game()
game.rodar()
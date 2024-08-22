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
        self.player = Player(self.__screen)


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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.setDirection(0)
                    elif event.key == pygame.K_LEFT:
                        self.player.setDirection(1)
                    elif event.key == pygame.K_UP:
                        self.player.setDirection(2)
                    elif event.key == pygame.K_DOWN:
                        self.player.setDirection(3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.setRun(False)

            self.tile.draw_board()
            self.player.draw_player(PLAYER_IMAGES)
        
            pygame.display.flip()
        
        pygame.quit()

game = Game()
game.rodar()
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
        self.font = pygame.font.SysFont(None, 36)

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
            self.tile.draw_board()
            self.player.draw_player(PLAYER_IMAGES)
            self.player.setTurns_allowed(self.player.check_position(self.player.getCenter_x(), self.player.getCenter_y()))
            self.player.move(self.player.getCharacter_x(), self.player.getCharacter_y())
            self.player.check_colision()
            self.player.scoreManager.draw_misc(self.getScreen(), self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.setRun(False)
                self.player.check_keyboard(event)
            self.player.change_direction()
        
            pygame.display.flip()
        
        pygame.quit()

# Inicializar e rodar o jogo
game = Game()
game.rodar()

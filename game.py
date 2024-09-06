import pygame
from tile import *
from settings import *
from player import *
from ghost import *
from blinky import *
from pinky import *
from inky import *
from clyde import *

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode((LARGURA, ALTURA))
        self.__timer = pygame.time.Clock()
        self.__run = True
        self.tile = Tile(self.__screen)
        self.player = Player(self.__screen)
        self.font = pygame.font.SysFont(None, 36)
        self.clyde = Clyde()
        self.inky = Inky()
        self.blinky = Blinky()
        self.pinky = Pinky()

        
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
            original_map = copy.deepcopy(gamemap)
            self.getTimer().tick(FPS)
            self.getScreen().fill('black')
            self.tile.draw_board()
            
            self.blinky.speed_varation(self.player)
            self.inky.speed_varation(self.player)
            self.pinky.speed_varation(self.player)
            self.clyde.speed_varation(self.player)
            
            self.clyde.draw(self.getScreen(), self.player)
            self.pinky.draw(self.getScreen(), self.player)
            self.inky.draw(self.getScreen(), self.player)
            self.blinky.draw(self.getScreen(), self.player)
             
            player_circle = pygame.draw.circle(self.getScreen(), 'black', (self.player.getCenter_x(), self.player.getCenter_y()), 16, 2)
            self.player.draw_player(PLAYER_IMAGES)  
            
            self.player.scoreManager.draw_misc(self.getScreen(), self.font, self.player)     
            
            self.clyde.update_target(self.player)
            self.pinky.update_target(self.player)
            self.inky.update_target(self.player)
            self.blinky.update_target(self.player)
        
            self.player.setTurns_allowed(self.player.check_position(self.player.getCenter_x(), self.player.getCenter_y()))
            
            self.clyde.check_collision(self.tile, self.clyde.getCenter_x(), self.clyde.getCenter_y())
            self.pinky.check_collision(self.tile, self.pinky.getCenter_x(), self.pinky.getCenter_y())
            self.inky.check_collision(self.tile, self.inky.getCenter_x(), self.inky.getCenter_y())
            self.blinky.check_collision(self.tile, self.blinky.getCenter_x(), self.blinky.getCenter_y())
            

            if self.player.getMoving():
                self.player.move(self.player.getCharacter_x(), self.player.getCharacter_y())
                self.clyde.move_ghost()
                
                if not self.pinky.getDead() and not self.pinky.getInthebox():
                    self.pinky.move_ghost(False)
                else:
                    self.pinky.move_ghost(True)
                
                if not self.inky.getDead() and not self.inky.getInthebox():
                    self.inky.move_ghost(False)
                else:
                    self.inky.move_ghost(True)
                    
                if not self.blinky.getDead() and not self.blinky.getInthebox():
                    self.blinky.move_ghost(False)
                else:
                    self.blinky.move_ghost(True)
            
            self.player.check_colision(self.tile)
            self.player.powerup_up_and_start_game()
            
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player.player_game_over:
                        self.player.game_won = False
                        self.player.player_game_over = False
                        self.player.__collision_detected = False
                        self.player.setStartup_counter(0)
                        self.player.setPowerup(False)
                        self.player.setPower_count(0)
                        self.player.setCharacter_x(450)
                        self.player.setCharacter_y(663)
                        self.player.setDirection(0)
                        self.player.setDirection_comand(0)
                        
                        # Reseta os fantasmas
                        self.blinky.setCharacter_x(56)
                        self.blinky.setCharacter_y(58)
                        self.blinky.setDirection(0)
                        self.inky.setCharacter_x(440)
                        self.inky.setCharacter_y(388)
                        self.inky.setDirection(2)
                        self.pinky.setCharacter_x(440)
                        self.pinky.setCharacter_y(438)
                        self.pinky.setDirection(2)
                        self.clyde.setCharacter_x(440)
                        self.clyde.setCharacter_y(438)
                        self.clyde.setDirection(2)
                        
                        # Reseta os estados dos fantasmas
                        self.blinky.setEaten(False)
                        self.inky.setEaten(False)
                        self.pinky.setEaten(False)
                        self.clyde.setEaten(False)
                        self.blinky.setDead(False)
                        self.inky.setDead(False)
                        self.pinky.setDead(False)
                        self.clyde.setDead(False)
                        
                        # Reseta a pontuação e vidas
                        self.player.scoreManager.setScore(0)
                        self.player.setLives(4)
                        self.tile.setLevel(copy.deepcopy(original_map))  # Reinicializa o mapa
                        print("Game reiniciado")
                if event.type == pygame.QUIT:
                    self.setRun(False)
                self.player.check_keyboard(event, self.blinky, self.inky, self.pinky, self.clyde)
            self.player.change_direction()
            
            self.player.player_and_ghost_collision(self.blinky, self.inky, self.pinky, self.clyde, player_circle)
                       
            self.blinky.no_longer_dead(self.player)
            self.inky.no_longer_dead(self.player)
            self.pinky.no_longer_dead(self.player)
            self.clyde.no_longer_dead(self.player)
                 
            pygame.display.flip()
        
        pygame.quit()

# Inicializar e rodar o jogo
game = Game()
game.rodar()

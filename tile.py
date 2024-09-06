import pygame
import copy
from settings import *
from gamemap import *
from animations import *

class Tile:
    def __init__(self, screentile) -> None:
        self.__level = copy.deepcopy(gamemap)
        self.__screentile = screentile
        ##Dividido por 32 porque é a quantidade de linhas que o pacman precisa
        self.__num1 = ((ALTURA - 50 ) // 32)
        ##Dividido por 30 pois é a quantidade de colunas que são necessarias
        self.__num2 = (LARGURA // 30)
        self.animation = Animation()
   
    def getNum1(self):
        return self.__num1
    
    def getNum2(self):
        return self.__num2
    
    def getLevel(self):
        return self.__level
    
    def setLevel(self, val):
        self.__level = val
    
    def getScreentile(self):
        return self.__screentile
    
    def setScreentile(self, value):
        self.__screentile = value
        
    def update_tile(self, player, i, j, new_value):
        # Atualiza o tile no mapa da classe Tile
        self.__level[i][j] = new_value
        # Atualiza o tile no mapa da classe Player
        player.tile.getLevel()[i][j] = new_value

    def draw_board(self):
        self.getNum1()
        self.getNum2()
        self.animation.up_counter()
        print(self.getLevel())
        for i in range(len(self.getLevel())):
            for j in range(len(self.getLevel()[i])):
                tile_value = self.getLevel()[i][j]

                if tile_value == 0:
                    # Desenha um retângulo preto para tiles vazios
                    pygame.draw.rect(self.getScreentile(), 'black', pygame.Rect(j * self.getNum2(), i * self.getNum1(), self.getNum2(), self.getNum1()))
                elif tile_value == 1:
                    pygame.draw.circle(self.getScreentile(), WHITE, (j * self.getNum2() + (0.5 * self.getNum2()), i * self.getNum1() + (0.5 * self.getNum1())), 4) 
                elif tile_value == 2 and not self.animation.getFlink():
                    pygame.draw.circle(self.getScreentile(), WHITE, (j * self.getNum2() + (0.5 * self.getNum2()), i * self.getNum1() + (0.5 * self.getNum1())), 10)
                elif tile_value == 3:
                    pygame.draw.line(self.getScreentile(), BLUE, (j * self.getNum2() + (0.5 * self.getNum2()), i * self.getNum1()), (j * self.getNum2() + (0.5 * self.getNum2()), i * self.getNum1() + self.getNum1()), 3)
                elif tile_value == 4:
                    pygame.draw.line(self.getScreentile(), BLUE, (j * self.getNum2(), (0.5 * self.getNum1()) + i * self.getNum1()), (j * self.getNum2() + self.getNum2(), i * self.getNum1() + (0.5 * self.getNum1())), 3)
                elif tile_value == 5:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j * self.getNum2() - (0.4 * self.getNum2()) - 2), (i * self.getNum1() + (0.5 * self.getNum1())), self.getNum2(), self.getNum1()], 0, PI / 2, 3)
                elif tile_value == 6:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j * self.getNum2() + (0.5 * self.getNum2())), (i * self.getNum1() + (0.5 * self.getNum1())), self.getNum2(), self.getNum1()], PI / 2, PI, 3)
                elif tile_value == 7:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j * self.getNum2() + (0.5 * self.getNum2())), (i * self.getNum1() - (0.5 * self.getNum1())), self.getNum2(), self.getNum1()], PI, 3 * PI / 2, 3)
                elif tile_value == 8:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j * self.getNum2() - (0.4 * self.getNum2()) - 2), (i * self.getNum1() - (0.4 * self.getNum1())), self.getNum2(), self.getNum1()], 3 * PI / 2, 2 * PI, 3)
                elif tile_value == 9:
                    pygame.draw.line(self.getScreentile(), WHITE, (j * self.getNum2(), (0.5 * self.getNum1()) + i * self.getNum1()), (j * self.getNum2() + self.getNum2(), i * self.getNum1() + (0.5 * self.getNum1())), 3)
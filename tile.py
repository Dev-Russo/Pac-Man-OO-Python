import pygame
from settings import *
from gamemap import *

class Tile:
    def __init__(self, screentile) -> None:
        self.__level = gamemap
        self.__screentile = screentile
        ##Dividido por 32 porque é a quantidade de linhas que o pacman precisa
        self.__num1 = ((ALTURA - 50 ) // 32)
        ##Dividido por 30 pois é a quantidade de colunas que são necessarias
        self.__num2 = (LARGURA // 30)
   
    def getNum1(self):
        return self.__num1
    
    def getNum2(self):
        return self.__num2
    
    def getLevel(self):
        return self.__level
    
    def getScreentile(self):
        return self.__screentile
    
    def setScreentile(self, value):
        self.__screentile = value

    def draw_board(self):
        self.getNum1()
        self.getNum2()
        ##loop para cada linha
        for i in range(len(self.getLevel())):
            ##loop para cada coluna dentro da linha especifica
            for j in range(len(self.getLevel()[i])):
                ##A conta faz o ponto ficar no meio da tela
                if self.getLevel()[i][j] == 1:
                    pygame.draw.circle(self.getScreentile(), WHITE, (j*self.getNum2() + (0.5*self.getNum2()), i*self.getNum1() + (0.5*self.getNum1())), 4) 
                if self.getLevel()[i][j] == 2:
                    pygame.draw.circle(self.getScreentile(), WHITE, (j*self.getNum2() + (0.5*self.getNum2()), i*self.getNum1() + (0.5*self.getNum1())), 10)
                ##A conta faz com que o risco vertical fique no meio da tela e desça de cima para baixo na outra é horizontal da esquerda para direita
                if self.getLevel()[i][j] == 3:
                    pygame.draw.line(self.getScreentile(), BLUE, (j*self.getNum2() + (0.5*self.getNum2()),i*self.getNum1()), (j*self.getNum2() + (0.5*self.getNum2()), i*self.getNum1() + self.getNum1()), 3)
                if self.getLevel()[i][j] == 4:
                    pygame.draw.line(self.getScreentile(), BLUE, (j*self.getNum2(), (0.5*self.getNum1()) + i*self.getNum1()), (j*self.getNum2() + self.getNum2(), i*self.getNum1() + (0.5*self.getNum1())), 3)
                ##5, 6, 7 e 8 são cordenadas x,y expessura e começo e termino do arco do circulo dentro do retangulo
                if self.getLevel()[i][j] == 5:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j*self.getNum2() - (0.4*self.getNum2()) - 2), (i*self.getNum1() + (0.5*self.getNum1())), self.getNum2(), self.getNum1()], 0, PI/2, 3)
                if self.getLevel()[i][j] == 6:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j*self.getNum2() + (0.5*self.getNum2())), (i*self.getNum1() + (0.5*self.getNum1())), self.getNum2(), self.getNum1()], PI/2, PI, 3)
                if self.getLevel()[i][j] == 7:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j*self.getNum2() + (0.5*self.getNum2())), (i*self.getNum1() - (0.5*self.getNum1())), self.getNum2(), self.getNum1()], PI, 3*PI/2, 3)
                if self.getLevel()[i][j] == 8:
                    pygame.draw.arc(self.getScreentile(), BLUE, [(j*self.getNum2() - (0.4*self.getNum2()) - 2), (i*self.getNum1() - (0.4*self.getNum1())), self.getNum2(), self.getNum1()], 3*PI/2, 2*PI, 3)
                if self.getLevel()[i][j] == 9:
                    pygame.draw.line(self.getScreentile(), WHITE, (j*self.getNum2(), (0.5*self.getNum1()) + i*self.getNum1()), (j*self.getNum2() + self.getNum2(), i*self.getNum1() + (0.5*self.getNum1())), 3)
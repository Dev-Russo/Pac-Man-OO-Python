from character import *
from player import *
from settings import *
from tile import *
class Ghost(Character):
    def __init__(self, character_x, character_y, character_speed, img) -> None:
        super().__init__(character_x, character_y, character_speed)
        self.setCenter_x(self.getCharacter_x() + 5)
        self.setCenter_y(self.getCharacter_y() + 5)
        self.__eaten = False
        self.__targets = None
        self.__dead = False
        self.__inthebox = False
        self.__img = img
        self.__inthebox = True
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
            screen.blit(self.getImage(), (self.getCharacter_x(), self.getCharacter_y()))
        elif player.getPowerup() and not self.getDead() and not self.getEaten():
            screen.blit(spooked_img, (self.getCharacter_x(), self.getCharacter_y()))
        else:
            screen.blit(dead_img, (self.getCharacter_x(), self.getCharacter_y()))
        
        self.setRect(pygame.rect.Rect((self.getCenter_x() - 18, self.getCenter_y() - 18), (36 , 36))) 
    
    def check_collision(self, tile):
        num1 = ((ALTURA - 50) // 32)
        num2 = (LARGURA // 30)
        num3 = 15
        turns = [False, False, False, False]
    
    # Se a posição do fantasma estiver dentro dos limites do mapa
        if 0 < self.getCenter_x() // 30 < 29:
            # Verificar movimento para cima
            if tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] < 3 \
                or (tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[2] = True
        
            # Verificar movimento para baixo
            if tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] < 3 \
                or (tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[3] = True
        
            # Verificar movimento para a esquerda
            if tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() - num3) // num2] < 3 \
                or (tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() - num3) // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[1] = True
        
            # Verificar movimento para a direita
            if tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() + num3) // num2] < 3 \
                or (tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() + num3) // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[0] = True

            # Correção para movimentação vertical se a direção for para cima ou para baixo
            if self.getDirection() in [2, 3]:  # Cima ou Baixo
                if 12 <= self.getCenter_x() % num2 <= 18:
                    if tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[3] = True
                    if tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[2] = True

                if 12 <= self.getCenter_y() % num1 <= 18:
                    if tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() - num2) // num2] < 3 \
                        or (tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() - num2) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[1] = True
                    if tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() + num2) // num2] < 3 \
                        or (tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() + num2) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[0] = True

            # Correção para movimentação horizontal se a direção for para esquerda ou direita
            if self.getDirection() in [0, 1]:  # Esquerda ou Direita
                if 12 <= self.getCenter_x() % num2 <= 18:
                    if tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() + num3) // num1][self.getCenter_x() // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[3] = True
                    if tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() - num3) // num1][self.getCenter_x() // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[2] = True

                if 12 <= self.getCenter_y() % num1 <= 18:
                    if tile.getLevel()[self.getCenter_y() // num1][(self.getCenter_x() - num3) // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() + num3) // num1][(self.getCenter_x() - num3) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[1] = True
                    if tile.getLevel()[(self.getCenter_y() - num3) // num1][(self.getCenter_x() + num3) // num2] < 3 \
                        or (tile.getLevel()[(self.getCenter_y() - num3) // num1][(self.getCenter_x() + num3) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[0] = True

        # Se o fantasma estiver fora dos limites, permite movimento para esquerda e direita
        else:
            turns[0] = True
            turns[1] = True

        # Verifica se o fantasma está na "caixa"
        if 350 < self.getCharacter_x() < 550 and 370 < self.getCharacter_y() < 490:
            self.setInthebox(True)
        else:
            self.setInthebox(False)

        self.setTurns_allowed(turns)



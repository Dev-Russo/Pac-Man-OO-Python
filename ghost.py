from character import *
from player import *
from settings import *
from tile import *
class Ghost(Character):
    def __init__(self, character_x, character_y, character_speed, img) -> None:
        super().__init__(character_x, character_y, character_speed)
        self.__eaten = False
        self.__targets = None
        self.__dead = False
        self.__img = img
        self.setCenter_x(self.getCharacter_x() + 22)
        self.setCenter_y(self.getCharacter_y() + 22)
        self.__inthebox = True
        self.__rect = pygame.rect.Rect((self.getCenter_x() - 18, self.getCenter_y() - 18), (36, 36))
        self.count = 0
    
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
        
    def move_ghost(self):
        if self.getDirection() == 0:  # Direita
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
        elif self.getDirection() == 1:  # Esquerda
            if self.getTarget()[1] > self.getCharacter_y() and self.getTurns_allowed()[3]:
                self.setDirection(3)
                self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
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
        elif self.getDirection() == 2:  # Cima
            if self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                self.setDirection(1)
                self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
            elif self.getTarget()[1] < self.getCharacter_y() and self.getTurns_allowed()[2]:
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
                if self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                    self.setDirection(0)
                    self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                    self.setDirection(1)
                    self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                else:
                    self.setCharacter_y(self.getCharacter_y() - self.getCharacter_speed())
        elif self.getDirection() == 3:  # Baixo
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
                if self.getTarget()[0] > self.getCharacter_x() and self.getTurns_allowed()[0]:
                    self.setDirection(0)
                    self.setCharacter_x(self.getCharacter_x() + self.getCharacter_speed())
                elif self.getTarget()[0] < self.getCharacter_x() and self.getTurns_allowed()[1]:
                    self.setDirection(1)
                    self.setCharacter_x(self.getCharacter_x() - self.getCharacter_speed())
                else:
                    self.setCharacter_y(self.getCharacter_y() + self.getCharacter_speed())
        
        # Verificar limites do mapa
        if self.getCharacter_x() < -30:
            self.setCharacter_x(900)
        elif self.getCharacter_x() > 900:
            self.setCharacter_x(-30)
            
        self.update_center()

        return self.getCharacter_x(), self.getCharacter_y(), self.getDirection()

    def update_target(self, player):
        if player.getCharacter_x() < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if player.getCharacter_y() < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if player.getPowerup():
            if not self.getDead() and not self.getEaten():
                self.setTarget([runaway_x, runaway_y])
            elif not self.getDead() and self.getEaten():
                if 340 < self.getCharacter_x() < 560 and 340 < self.getCharacter_y() < 500:
                    self.setTarget([400, 100])
                else:
                    self.setTarget([player.getCharacter_x(), player.getCharacter_y()])
        else:
            if not self.getDead():
                if 340 < self.getCharacter_x() < 560 and 340 < self.getCharacter_y() < 500:
                    self.setTarget([400, 100])
                else:
                    self.setTarget([player.getCharacter_x(), player.getCharacter_y()])
            else:
                self.setTarget(return_target)           
    
    def draw(self, screen, player):
        if (not player.getPowerup() and not self.getDead()) or (self.getEaten() and player.getPowerup() and not self.getDead()):
            screen.blit(self.getImage(), (self.getCharacter_x(), self.getCharacter_y()))
        elif player.getPowerup() and not self.getDead() and not self.getEaten():
            screen.blit(spooked_img, (self.getCharacter_x(), self.getCharacter_y()))
        else:
            screen.blit(dead_img, (self.getCharacter_x(), self.getCharacter_y()))
        
        self.setRect(pygame.rect.Rect((self.getCenter_x() - 18, self.getCenter_y() - 18), (36 , 36))) 

    def update_center(self):
        self.setCenter_x(self.getCharacter_x() + 15)
        self.setCenter_y(self.getCharacter_y() + 15)
        
    def check_collision(self, tile, centerx , centery):
        num1 = ((ALTURA - 50) // 32)
        num2 = (LARGURA // 30)
        num3 = 15
        turns = [False, False, False, False]
    
        if 0 < centerx // 30 < 29:
            if tile.getLevel()[(centery - num3) // num1][centerx // num2] == 9:
                turns[2] = True
            # Verificar movimento para cima
            if tile.getLevel()[(centery - num3) // num1][centerx // num2] < 3 \
                or (tile.getLevel()[(centery - num3) // num1][centerx // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[2] = True
        
            # Verificar movimento para baixo
            if tile.getLevel()[(centery + num3) // num1][centerx // num2] < 3 \
                or (tile.getLevel()[(centery + num3) // num1][centerx // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[3] = True
        
            # Verificar movimento para a esquerda
            if tile.getLevel()[centery // num1][(centerx - num3) // num2] < 3 \
                or (tile.getLevel()[centery // num1][(centerx - num3) // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[1] = True
        
            # Verificar movimento para a direita
            if tile.getLevel()[centery // num1][(centerx + num3) // num2] < 3 \
                or (tile.getLevel()[centery // num1][(centerx + num3) // num2] == 9 and (
                    self.getInthebox() or self.getDead())):
                turns[0] = True

            # Correção para movimentação vertical se a direção for para cima ou para baixo
            if self.getDirection() in [2, 3]:  # Cima ou Baixo
                if 12 <= centerx % num2 <= 18:
                    if tile.getLevel()[(centery + num3) // num1][centerx // num2] < 3 \
                        or (tile.getLevel()[(centery + num3) // num1][centerx // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[3] = True
                    if tile.getLevel()[(centery - num3) // num1][centerx // num2] < 3 \
                        or (tile.getLevel()[(centery - num3) // num1][centerx // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[2] = True

                if 12 <= centery % num1 <= 18:
                    if tile.getLevel()[centery // num1][(centerx - num2) // num2] < 3 \
                        or (tile.getLevel()[centery // num1][(centerx - num2) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[1] = True
                    if tile.getLevel()[centery // num1][(centerx + num2) // num2] < 3 \
                        or (tile.getLevel()[centery // num1][(centerx + num2) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[0] = True

            # Correção para movimentação horizontal se a direção for para esquerda ou direita
            if self.getDirection() in [0, 1]:  # Esquerda ou Direita
                if 12 <= centerx % num2 <= 18:
                    if tile.getLevel()[(centery + num3) // num1][centerx // num2] < 3 \
                        or (tile.getLevel()[(centery + num3) // num1][centerx // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[3] = True
                    if tile.getLevel()[(centery - num3) // num1][centerx // num2] < 3 \
                        or (tile.getLevel()[(centery - num3) // num1][centerx // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[2] = True

                if 12 <= centery % num1 <= 18:
                    if tile.getLevel()[centery // num1][(centerx - num3) // num2] < 3 \
                        or (tile.getLevel()[(centery + num3) // num1][(centerx - num3) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[1] = True
                    if tile.getLevel()[(centery - num3) // num1][(centerx + num3) // num2] < 3 \
                        or (tile.getLevel()[(centery - num3) // num1][(centerx + num3) // num2] == 9 and (
                            self.getInthebox() or self.getDead())):
                        turns[0] = True

        # Se o fantasma estiver fora dos limites, permite movimento para esquerda e direita
        else:
            turns[0] = True
            turns[1] = True

        # Verifica se o fantasma está na "caixa"
        if 350 < self.getCharacter_x() < 550 and 370 < self.getCharacter_y() < 480:
            self.setInthebox(True)
        else:
            self.setInthebox(False)

        self.setTurns_allowed(turns)
        
    def no_longer_dead(self, player):
        if self.getInthebox() and self.getDead():
            self.setDead(False)
        if not player.getPowerup():
            self.setEaten(False)
            
    def speed_varation(self, player):
        if player.getPowerup():
           self.setCharacter_speed(1)
        else:
            self.setCharacter_speed(2) 
        if self.getDead():
            self.setCharacter_speed(4)
            
    def sum(self):
        if self.getEaten():
            self.count += 1
        return self.count
        
import pygame
from animations import *
from settings import *
from character import *
from tile import *
from scoremanager import *

class Player(Character):
    def __init__(self, screencharacter) -> None:
        super().__init__(character_x=450, character_y=663, character_speed=2)
        self.__screencharacter = screencharacter
        self.animation = Animation()
        self.setCenter_x(self.getCharacter_x() + 23)
        self.setCenter_y(self.getCharacter_y() + 24)
        self.tile = Tile(self.__screencharacter)
        self.scoreManager = ScoreManager() 

    def getScreencharacter(self):
        return self.__screencharacter

    def check_keyboard(self, event):
    # Verifica se o evento é um evento de teclado antes de acessar 'key'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.setDirection_comand(0)  # Direita
            elif event.key == pygame.K_LEFT:
                self.setDirection_comand(1)  # Esquerda
            elif event.key == pygame.K_DOWN:
                self.setDirection_comand(2)  # Baixo
            elif event.key == pygame.K_UP:
                self.setDirection_comand(3)  # Cima
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and self.getDirection_comand() == 0:
                self.setDirection_comand(self.getDirection())
            elif event.key == pygame.K_LEFT and self.getDirection_comand() == 1:
                self.setDirection_comand(self.getDirection())
            elif event.key == pygame.K_DOWN and self.getDirection_comand() == 2:
                self.setDirection_comand(self.getDirection())
            elif event.key == pygame.K_UP and self.getDirection_comand() == 3:
                self.setDirection_comand(self.getDirection())


    def change_direction(self):
        # Atualiza a direção do jogador com base no comando de direção
        for i in range(4):
            if self.getDirection_comand() == i and self.getTurns_allowed()[i]:
                self.setDirection(i)

        # Verificação de borda (teletransporte para o outro lado da tela)
        if self.getCharacter_x() > 900:
            self.setCharacter_x(-47)
        elif self.getCharacter_x() < -50:
            self.setCharacter_x(897)

    def move(self, characterx, charactery):
        super().move(characterx, charactery)

    def draw_player(self, player_images):
        if self.getDirection() == 0:
            self.getScreencharacter().blit(player_images[self.animation.getCounter() // 5], (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 1:
            flipped_image = pygame.transform.flip(player_images[self.animation.getCounter() // 5], True, False)
            self.getScreencharacter().blit(flipped_image, (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 2:
            rotated_image = pygame.transform.rotate(player_images[self.animation.getCounter() // 5], 270)
            self.getScreencharacter().blit(rotated_image, (self.getCharacter_x(), self.getCharacter_y()))
        elif self.getDirection() == 3:
            rotated_image = pygame.transform.rotate(player_images[self.animation.getCounter() // 5], 90)
            self.getScreencharacter().blit(rotated_image, (self.getCharacter_x(), self.getCharacter_y()))
        self.animation.up_counter()

    def check_position(self, centerx, centery):
        turns = [False, False, False, False]
        num3 = 15

        if centerx // 30 < 29:
            if self.getDirection() == 0:  # Direita
                if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx + num3) // self.tile.getNum2()] < 3:
                    turns[0] = True
            if self.getDirection() == 1:  # Esquerda
                if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx - num3) // self.tile.getNum2()] < 3:
                    turns[1] = True
            if self.getDirection() == 2:  # Baixo
                if self.tile.getLevel()[(centery + num3) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                    turns[2] = True
            if self.getDirection() == 3:  # Cima
                if self.tile.getLevel()[(centery - num3) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                    turns[3] = True

        # Ajuste para movimentos diagonais ou alinhamentos imperfeitos
            if self.getDirection() in [2, 3]:  # Movimentação vertical
                if 12 <= centerx % self.tile.getNum2() <= 18:
                    if self.tile.getLevel()[(centery + num3) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                        turns[2] = True
                    if self.tile.getLevel()[(centery - num3) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                        turns[3] = True
                if 12 <= centery % self.tile.getNum1() <= 18:
                    if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx - self.tile.getNum2()) // self.tile.getNum2()] < 3:
                        turns[1] = True
                    if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx + self.tile.getNum2()) // self.tile.getNum2()] < 3:
                        turns[0] = True
            if self.getDirection() in [0, 1]:  # Movimentação horizontal
                if 12 <= centerx % self.tile.getNum2() <= 18:
                    if self.tile.getLevel()[(centery + self.tile.getNum1()) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                        turns[2] = True
                    if self.tile.getLevel()[(centery - self.tile.getNum1()) // self.tile.getNum1()][centerx // self.tile.getNum2()] < 3:
                        turns[3] = True
                if 12 <= centery % self.tile.getNum1() <= 18:
                    if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx - num3) // self.tile.getNum2()] < 3:
                        turns[1] = True
                    if self.tile.getLevel()[centery // self.tile.getNum1()][(centerx + num3) // self.tile.getNum2()] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns

    def check_colision(self):
        if 0 < self.getCharacter_x() < 870:
            if self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] == 1:
                self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] = 0
                self.scoreManager.setScore(self.scoreManager.getScore() + 10)
            if self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] == 2:
                self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] = 0
                self.scoreManager.setScore(self.scoreManager.getScore() + 50)
            print(self.scoreManager.getScore())
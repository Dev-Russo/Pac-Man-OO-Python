import pygame
from animations import *
from settings import *
from character import *
from tile import *
from scoremanager import *
from ghost import *
from gamemap import *

class Player(Character):
    def __init__(self, screencharacter) -> None:
        super().__init__(character_x=450, character_y=663, character_speed=2)
        self.__screencharacter = screencharacter
        self.setCenter_x(self.getCharacter_x() + 23)
        self.setCenter_y(self.getCharacter_y() + 24)
        self.__powerup = False
        self.__power_count = 0
        self.__lives = 0
        self.tile = Tile(self.__screencharacter)
        self.scoreManager = ScoreManager() 
        self.animation = Animation()
        self.__collision_detected = False
        self.player_game_over = False
        self.game_won = False

    def reset_collision(self):
        self.__collision_detected = False

    def getPlayer_circle(self):
        return self.__player_circle
    
    def getScreencharacter(self):
        return self.__screencharacter
    
    def getLives(self):
        return self.__lives
    
    def setLives(self, value):
        self.__lives = value
        
    def getPowerup(self):
        return self.__powerup
    
    def setPowerup(self, value):
        self.__powerup = value
    
    def getPower_count(self):
        return self.__power_count
    
    def setPower_count(self, value):
        self.__power_count = value

    def powerup_up_and_start_game(self):
        if self.getPowerup() and self.getPower_count() < 600:
            self.setPower_count(self.getPower_count() + 1)
            siren.play()
        elif self.getPowerup() and self.getPower_count() >= 600:
            self.setPowerup(False)
            self.setPower_count(0)
            #ghost.setEaten(False)    
        if self.getStartup_counter() < 180 and not self.player_game_over and not self.game_won:
            self.setMoving(False)
            self.setStartup_counter(self.getStartup_counter() + 1)
        else:
            self.setMoving(True)           
    
    def update_game_ovver(self):
        self.player_game_over = False
    
    def check_keyboard(self, event, blink, ink, pink, clyde):
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
            if event.key == pygame.K_SPACE and (self.game_won or self.player_game_over):
                    
                    print(self.player_game_over)
                    self.game_won = False
                    self.setStartup_counter(0)
                    self.setPowerup(False)
                    self.setPower_count(0)
                    self.setCharacter_x(450)
                    self.setCharacter_y(663)
                    self.setDirection(0)
                    self.setDirection_comand(0)
                    blink.setCharacter_x(56)
                    blink.setCharacter_y(58)
                    blink.setDirection(0)
                    ink.setCharacter_x(440)
                    ink.setCharacter_y(388)
                    ink.setDirection(2)
                    pink.setCharacter_x(440)
                    pink.setCharacter_y(438)
                    pink.setDirection(2)
                    clyde.setCharacter_x(440)
                    clyde.setCharacter_y(438)
                    clyde.setDirection(2)
                    blink.setEaten(False)
                    ink.setEaten(False)
                    pink.setEaten(False)
                    clyde.setEaten(False)
                    blink.setDead(False)
                    ink.setDead(False)
                    pink.setDead(False)
                    clyde.setDead(False)
                    self.scoreManager.setScore(0)
                    self.setLives(3)
                    self.tile.setLevel(gamemap)
                    self.update_game_ovver()
                    self.player_game_over = False
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
        #print(centerx)
        return turns
    #Passar ghost como parametro
    def check_colision(self, ): 
        if 0 < self.getCharacter_x() < 870:
            if self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] == 1:
                self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] = 0
                self.scoreManager.setScore(self.scoreManager.getScore() + 10)
                credit.play()
            if self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] == 2:
                self.tile.getLevel()[self.getCenter_y() // self.tile.getNum1()][self.getCenter_x() // self.tile.getNum2()] = 0
                self.scoreManager.setScore(self.scoreManager.getScore() + 50)
                self.setPowerup(True)
                self.setPower_count(0)
                #ghost.setEaten(False)  
       
    def count_eated_ghosts(self, blink, ink, pink, clyde):
    # Inicializa o contador de fantasmas comidos
        ghosts_eaten_count = 0
        
        # Verifica se o power-up está ativo
        if self.getPowerup():
            # Verifica se cada fantasma foi comido e atualiza o contador
            if blink.getEaten():  # Se o fantasma blink foi comido
                ghosts_eaten_count += 1
            
            if ink.getEaten():  # Se o fantasma ink foi comido
                ghosts_eaten_count += 1  # Reseta o estado "comido" do ink
            
            if pink.getEaten():  # Se o fantasma pink foi comido
                ghosts_eaten_count += 1 
            
            if clyde.getEaten():  # Se o fantasma clyde foi comido
                ghosts_eaten_count += 1  

        # Se o power-up acabou, o contador de fantasmas comidos permanece como zero
        else:
            ghosts_eaten_count = 0

        return ghosts_eaten_count

    def player_and_ghost_collision(self, blink, ink, pink, clyde, playerhitbox):
        if not self.__collision_detected:
            if not self.getPowerup():
                if playerhitbox.colliderect(blink.getRect()) and not blink.getDead() or\
                    playerhitbox.colliderect(ink.getRect()) and not ink.getDead() or\
                    playerhitbox.colliderect(pink.getRect()) and not pink.getDead or\
                    playerhitbox.colliderect(clyde.getRect()) and not clyde.getDead():
                    if self.getLives() > 0:
                        self.setLives(self.getLives() - 1)
                        self.setStartup_counter(0)
                        self.setPowerup(False)
                        self.setPower_count(0)
                        self.setCharacter_x(450)
                        self.setCharacter_y(663)
                        self.setDirection(0)
                        self.setDirection_comand(0)
                        blink.setCharacter_x(56)
                        blink.setCharacter_y(58)
                        blink.setDirection(0)
                        ink.setCharacter_x(440)
                        ink.setCharacter_y(388)
                        ink.setDirection(2)
                        pink.setCharacter_x(440)
                        pink.setCharacter_y(438)
                        pink.setDirection(2)
                        clyde.setCharacter_x(440)
                        clyde.setCharacter_y(438)
                        clyde.setDirection(2)
                        blink.setEaten(False)
                        ink.setEaten(False)
                        pink.setEaten(False)
                        clyde.setEaten(False)
                        blink.setDead(False)
                        ink.setDead(False)
                        pink.setDead(False)
                        clyde.setDead(False)
                        self.__collision_detected = True
                    else:
                        self.player_game_over = True
                        self.setMoving(False)
                        self.setStartup_counter(0)
            if self.getPowerup() and playerhitbox.colliderect(blink.getRect()) and blink.getEaten() and not blink.getDead():
                if self.getLives() > 0:
                        self.setStartup_counter(0)
                        self.setLives(self.getLives() - 1)
                        self.setPowerup(False)
                        self.setPower_count(0)
                        self.setCharacter_x(450)
                        self.setCharacter_y(663)
                        self.setDirection(0)
                        self.setDirection_comand(0)
                        blink.setCharacter_x(56)
                        blink.setCharacter_y(58)
                        blink.setDirection(0)
                        ink.setCharacter_x(440)
                        ink.setCharacter_y(388)
                        ink.setDirection(2)
                        pink.setCharacter_x(440)
                        pink.setCharacter_y(438)
                        pink.setDirection(2)
                        clyde.setCharacter_x(440)
                        clyde.setCharacter_y(438)
                        clyde.setDirection(2)
                        blink.setEaten(False)
                        ink.setEaten(False)
                        pink.setEaten(False)
                        clyde.setEaten(False)
                        blink.setDead(False)
                        ink.setDead(False)
                        pink.setDead(False)
                        clyde.setDead(False)
                        self.__collision_detected = True
                else:
                        self.player_game_over = True
                        self.setMoving(False)
                        self.setStartup_counter(0)
            if self.getPowerup() and playerhitbox.colliderect(ink.getRect()) and ink.getEaten() and not ink.getDead():
                if self.getLives() > 0:
                        self.setStartup_counter(0)
                        self.setLives(self.getLives() - 1)
                        self.setPowerup(False)
                        self.setPower_count(0)
                        self.setCharacter_x(450)
                        self.setCharacter_y(663)
                        self.setDirection(0)
                        self.setDirection_comand(0)
                        blink.setCharacter_x(56)
                        blink.setCharacter_y(58)
                        blink.setDirection(0)
                        ink.setCharacter_x(440)
                        ink.setCharacter_y(388)
                        ink.setDirection(2)
                        pink.setCharacter_x(440)
                        pink.setCharacter_y(438)
                        pink.setDirection(2)
                        clyde.setCharacter_x(440)
                        clyde.setCharacter_y(438)
                        clyde.setDirection(2)
                        blink.setEaten(False)
                        ink.setEaten(False)
                        pink.setEaten(False)
                        clyde.setEaten(False)
                        blink.setDead(False)
                        ink.setDead(False)
                        pink.setDead(False)
                        clyde.setDead(False)
                        self.__collision_detected = True
                else:
                        self.player_game_over = True
                        self.setMoving(False)
                        self.setStartup_counter(0)
            if self.getPowerup() and playerhitbox.colliderect(pink.getRect()) and pink.getEaten() and not pink.getDead():
                if self.getLives() > 0:
                        self.setStartup_counter(0)
                        self.setLives(self.getLives() - 1)
                        self.setPowerup(False)
                        self.setPower_count(0)
                        self.setCharacter_x(450)
                        self.setCharacter_y(663)
                        self.setDirection(0)
                        self.setDirection_comand(0)
                        blink.setCharacter_x(56)
                        blink.setCharacter_y(58)
                        blink.setDirection(0)
                        ink.setCharacter_x(440)
                        ink.setCharacter_y(388)
                        ink.setDirection(2)
                        pink.setCharacter_x(440)
                        pink.setCharacter_y(438)
                        pink.setDirection(2)
                        clyde.setCharacter_x(440)
                        clyde.setCharacter_y(438)
                        clyde.setDirection(2)
                        blink.setEaten(False)
                        ink.setEaten(False)
                        pink.setEaten(False)
                        clyde.setEaten(False)
                        blink.setDead(False)
                        ink.setDead(False)
                        pink.setDead(False)
                        clyde.setDead(False)
                        self.__collision_detected = True
                else:
                        self.player_game_over = True
                        self.setMoving(False)
                        self.setStartup_counter(0)
            if self.getPowerup() and playerhitbox.colliderect(clyde.getRect()) and clyde.getEaten() and not clyde.getDead():
                if self.getLives() > 0:
                        self.setStartup_counter(0)
                        self.setLives(self.getLives() - 1)
                        self.setPowerup(False)
                        self.setPower_count(0)
                        self.setCharacter_x(450)
                        self.setCharacter_y(663)
                        self.setDirection(0)
                        self.setDirection_comand(0)
                        blink.setCharacter_x(56)
                        blink.setCharacter_y(58)
                        blink.setDirection(0)
                        ink.setCharacter_x(440)
                        ink.setCharacter_y(388)
                        ink.setDirection(2)
                        pink.setCharacter_x(440)
                        pink.setCharacter_y(438)
                        pink.setDirection(2)
                        clyde.setCharacter_x(440)
                        clyde.setCharacter_y(438)
                        clyde.setDirection(2)
                        blink.setEaten(False)
                        ink.setEaten(False)
                        pink.setEaten(False)
                        clyde.setEaten(False)
                        blink.setDead(False)
                        ink.setDead(False)
                        pink.setDead(False)
                        clyde.setDead(False)
                        self.__collision_detected = True
                else:
                        self.player_game_over = True
                        self.setMoving(False)
                        self.setStartup_counter(0)
            if self.getPowerup() and playerhitbox.colliderect(blink.getRect()) and not blink.getDead() and not blink.getEaten():
                blink.setDead(True)
                blink.setEaten(True)
                pontuacao = ((2 ** self.count_eated_ghosts(blink, ink, pink, clyde)) * 100)
                self.scoreManager.setScore(self.scoreManager.getScore() + pontuacao)
                print(pontuacao)
                eat_ghost.play()
            if self.getPowerup() and playerhitbox.colliderect(ink.getRect()) and not ink.getDead() and not ink.getEaten():
                ink.setDead(True)
                ink.setEaten(True)
                pontuacao = ((2 ** self.count_eated_ghosts(blink, ink, pink, clyde)) * 100)
                self.scoreManager.setScore(self.scoreManager.getScore() + pontuacao)
                print(pontuacao)
                eat_ghost.play()
            if self.getPowerup() and playerhitbox.colliderect(pink.getRect()) and not pink.getDead() and not pink.getEaten():
                pink.setDead(True)
                pink.setEaten(True)
                pontuacao = ((2 ** self.count_eated_ghosts(blink, ink, pink, clyde)) * 100)
                self.scoreManager.setScore(self.scoreManager.getScore() + pontuacao)
                print(pontuacao)
                eat_ghost.play()
            if self.getPowerup() and playerhitbox.colliderect(clyde.getRect()) and not clyde.getDead() and not clyde.getEaten():
                clyde.setDead(True)
                clyde.setEaten(True)
                pontuacao = ((2 ** self.count_eated_ghosts(blink, ink, pink, clyde)) * 100)
                self.scoreManager.setScore(self.scoreManager.getScore() + pontuacao)
                print(pontuacao)
                eat_ghost.play()
        else:
            self.reset_collision()
        

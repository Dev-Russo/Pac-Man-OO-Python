from settings import *
import pygame

class ScoreManager:
    def __init__(self) -> None:
        self.__score = 0

    def setScore(self, value):
        self.__score = value

    def getScore(self):
        return self.__score
    
    def draw_misc(self, screen, font, player):
        score_text = font.render(f'Score: {self.getScore()}', True, 'white')
        screen.blit(score_text, (10, 920))
        if player.getPowerup():
            pygame.draw.circle(screen, 'blue', (180, 930), 15)
        for i in range(player.getLives()):
            screen.blit(pygame.transform.scale(PLAYER_IMAGES[0], (30, 30)), (650 + i * 40, 915))
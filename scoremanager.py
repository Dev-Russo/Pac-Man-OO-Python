from settings import *
import pygame

class ScoreManager:
    def __init__(self) -> None:
        self.__score = 0

    def setScore(self, value):
        self.__score = value

    def getScore(self):
        return self.__score
    
    def draw_misc(self, screen, font):
        score_text = font.render(f'Score: {self.getScore()}', True, 'white')
        screen.blit(score_text, (10, 920))
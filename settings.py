import pygame
import math

LARGURA = 900
ALTURA = 950
FPS = 60
WHITE = 'white'
BLUE = 'red'
PI = math.pi
#Lista da imagens de player
PLAYER_IMAGES = []

#Carrega as imagens, escalona e adiciona a lista
for i in range(1, 5):
    PLAYER_IMAGES.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
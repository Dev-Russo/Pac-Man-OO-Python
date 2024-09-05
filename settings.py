import pygame
import math

LARGURA = 900
ALTURA = 950
FPS = 60
WHITE = 'white'
BLUE = 'blue'
PI = math.pi
#Lista da imagens de player
PLAYER_IMAGES = []

#Carrega as imagens, escalona e adiciona a lista
for i in range(1, 5):
    PLAYER_IMAGES.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))

#Ghost Images
blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
pinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45))
inky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
clyde_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))

pygame.mixer.init()
#Sounds
credit = pygame.mixer.Sound('assets/pacmansounds/eat_dot_0.wav')
eat_ghost = pygame.mixer.Sound('assets/pacmansounds/eat_ghost.wav')
start = pygame.mixer.Sound('assets/pacmansounds/start.wav')
siren = pygame.mixer.Sound('assets/pacmansounds/siren1.wav')
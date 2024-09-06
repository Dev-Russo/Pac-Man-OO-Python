from settings import *
import pygame

class ScoreManager:
    def __init__(self) -> None:
        self.__score = 0

    def setScore(self, value):
        self.__score = value

    def getScore(self):
        return self.__score
    
    def draw_misc(self, screen, font, player, tres_maiores):
        """"player.setMoving(False)
        screen_width, screen_height = LARGURA, ALTURA
        pygame.draw.rect(screen, 'white', [0, 0, screen_width, screen_height], 0)
        text = "Digite seu nome:"
        text_surface = font.render(text, True, (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        text_x = (screen_width - text_width) // 2
        text_y = (screen_height // 2) - 100  
        screen.blit(text_surface, (text_x, text_y))
        input_rect_width = 400
        input_rect_height = 50
        input_rect_x = (screen_width - input_rect_width) // 2
        input_rect_y = text_y + 70    
        pygame.draw.rect(screen, (0, 0, 0), (input_rect_x, input_rect_y, input_rect_width, input_rect_height), 2)
        input_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(input_surface, (input_rect_x + 10, input_rect_y + (input_rect_height - input_surface.get_height()) // 2))  """        
        score_text = font.render(f'Score: {self.getScore()}', True, 'white')
        screen.blit(score_text, (10, 920))
        if player.getPowerup():
            pygame.draw.circle(screen, 'blue', (180, 930), 15)
        for i in range(player.getLives()):
            screen.blit(pygame.transform.scale(PLAYER_IMAGES[0], (30, 30)), (650 + i * 40, 915))
        
        
        if player.showing_ranking and player.showing_ranking:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'darkgray', [70, 220, 760, 260],0, 10)
            ranking = font.render('Ranking! Aperte espaço para continuar', True, 'black')
            first = font.render(f'Primeiro Lugar: {tres_maiores[0]}', True, 'black')
            seccond = font.render(f'Segundo Lugar: {tres_maiores[1]}', True, 'black')
            third = font.render(f'Terceiro Lugar: {tres_maiores[2]}', True, 'black')
            screen.blit(ranking, (100, 300))
            screen.blit(first, (100, 330))
            screen.blit(seccond, (100, 360))
            screen.blit(third, (100, 390))        
        
        
        if player.player_game_over and not player.showing_ranking:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'darkgray', [70, 220, 760, 260],0, 10)
            gameover_text = font.render('Game over! Aperte espaço para continuar', True, 'red')
            screen.blit(gameover_text, (100, 300))
        
        if player.game_won:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'darkgray', [70, 220, 760, 260],0, 10)
            gameover_text = font.render('Victory! Aperte espaço para continuar', True, 'green')
            screen.blit(gameover_text, (100, 300))
        
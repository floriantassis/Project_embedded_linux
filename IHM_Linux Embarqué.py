import pygame, sys
 

Clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Ordinateur de bord amélioré')
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), pygame.SCALED)




font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    

    while True:
 
        screen.fill((0,0,50))


        draw_text('MENU', font, (255, 255, 255), screen, pygame.display.Info().current_w/2-50, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(pygame.display.Info().current_w/2-100, 300, 50, 50)
        draw_text('Recuperation des informations moteur', font, (255, 255, 255), screen, pygame.display.Info().current_w/2, 325)
        button_2 = pygame.Rect(pygame.display.Info().current_w/2-100, 500, 50, 50)
        draw_text('Controle du telephone a distance', font, (255, 255, 255), screen, pygame.display.Info().current_w/2, 525)

        if button_1.collidepoint((mx, my)):
            if click:
                rec_moteur()
        if button_2.collidepoint((mx, my)):
            if click:
                cont_tel()
       

        pygame.draw.rect(screen, (128,128,128), button_1)
        pygame.draw.rect(screen, (128,128,128), button_2)
        
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        Clock.tick(60)
 
def rec_moteur():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Recuperation des informations moteur', font, (255, 255, 255), screen, pygame.display.Info().current_w/2-100, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        Clock.tick(60)
 
def cont_tel():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Controle du telephone a distance', font, (255, 255, 255), screen, pygame.display.Info().current_w/2-100, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        Clock.tick(60)

        
main_menu()
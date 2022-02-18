import pygame, sys
from pygame.locals import *
from particule_player import Player1
from particule_player import Player2
from particule_player import Player3


pygame.init()
window = pygame.display.set_mode((1380, 700))

#colors
white = (255, 255, 255)
black = (0, 225, 0)
red = (255, 0, 0)
blue = ( 43, 255, 230)
orange = ( 255, 170, 0)

#load the player
player1 = Player1("quark down", red)
player2 = Player2("quark up", blue)
player3 = Player3("quark bottom", orange)

run = True
moving1 = False
moving2 = False
moving3 = False

group1 = pygame.sprite.Group()
group1.add(player1, player2, player3)

while run:
    #window.blit(background, (0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("Goodbye!")
            sys.exit()

        #mouse play
        if event.type == MOUSEBUTTONDOWN:
            if player1.rect.collidepoint(event.pos):
                moving1 = True
            if player2.rect.collidepoint(event.pos):
                moving2 = True
            if player3.rect.collidepoint(event.pos):
                moving3 = True

        elif event.type == MOUSEBUTTONUP:
              moving1 = False
              moving2 = False
              moving3 = False

        elif event.type == MOUSEMOTION and moving1:
             player1.rect.move_ip(event.rel)
        elif event.type == MOUSEMOTION and moving2:
             player2.rect.move_ip(event.rel)
        elif event.type == MOUSEMOTION and moving3:
             player3.rect.move_ip(event.rel)

    #collision
    collision = pygame.sprite.collide_rect(player1, player2)
    collision = pygame.sprite.collide_rect(player3, player2)
    if collision == True:
        group1.remove(player1,player2,player3)
        startend = True
        #group1.add(nouvelle particule)
        group1.update()

    #aspect of the window
    window.fill(white)
    group1.draw(window)

    pygame.display.update()


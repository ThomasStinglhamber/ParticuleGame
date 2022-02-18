import pygame as pg
from pygame.locals import *
import sys
from particule_player import Player1
from particule_player import Player2
from particule_player import Player3
pg.init()


#generate window
pg.display.set_caption("Particle game")
screen = pg.display.set_mode((1380,700))

#background
background = pg.image.load("asset/fond-gris.png")


#load the player
player1 = Player1("quark down")
player2 = Player2("quark up")
player3 = Player3("quark bottom")

running = True
moving1 = False
moving2 = False
moving3 = False

#loop: while the running is true, the window is open
while running:
    #background
    screen.blit(background, (0,0))
    #player
    part1 = screen.blit(player1.image, player1.rect)
    part2  = screen.blit(player2.image, player2.rect)
    part3  = screen.blit(player3.image, player3.rect)
    #maj of the screen
    pg.display.flip()
    #if the player closes the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            pg.quit()
            print("Goodbye!")
            sys.exit()

        #part1
        elif event.type == MOUSEBUTTONDOWN:
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

    hitbox1 = (player1.rect[0] + 20, player1.rect[1], 28, 60)
    hitbox2 = (player2.rect[0] + 20, player2.rect[1], 28, 60)
    hitbox3 = (player3.rect[0] + 20, player3.rect[1], 28, 60)
    pg.sprite.spritecollide(player1, player2, True)

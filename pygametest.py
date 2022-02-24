import pygame, sys
from pygame.locals import *
from particule_player import Player


pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((1380, 700))

#colors
white = (255, 255, 255)
green = (0, 225, 0)
red = (255, 0, 0)
blue = ( 43, 255, 230)
orange = ( 255, 170, 0)

run = True
#load the player
players=[]

player1 = Player("quark down", red, 200, 100)
player2 = Player("quark up", blue, 800, 200)
player3 = Player("quark bottom", orange, 500, 100)
player4 = Player("proton", green, 1380/2,700/2) #arriver à mettre la position de collision des 3 particules

players=[player1,player2,player3]
#print(players)
movings=[]
moving1 = False
moving2 = False
moving3 = False
moving4 = False
movings=[moving1,moving2,moving3]


group1 = pygame.sprite.Group()
for i in range(len(players)):
    group1.add(players[i])


while run:
    #print(movings)
    #window.blit(background, (0,0))
    #print(len(players))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("Goodbye!")
            sys.exit()

        #mouse play
        for i in range(len(players)):
            if event.type == MOUSEBUTTONDOWN:
    
                if players[i].rect.collidepoint(event.pos):
                    movings[i] = True
                    
    
            elif event.type == MOUSEBUTTONUP:
                movings[i] = False
    
            elif event.type == MOUSEMOTION and movings[i]:
                 players[i].rect.move_ip(event.rel)

    #collision
            for j in range(len(players)):
                for k in range(len(players)):
                    if len(players)>=3:
                        if i != j and i != k and j != k:
                            collision1 = pygame.sprite.collide_rect(players[i], players[j])
                            collision2 = pygame.sprite.collide_rect(players[i], players[k])
                            #print(collision1,collision2)
                            if collision1 == True and collision2 == True:
                                once =True
                                if once ==True:
                                    once=False
                                    players.append(player4)
                                    movings.append(False)
                                    group1.remove(players[i],players[j],players[k])
                                    #print(i,j,k)
                                    players.pop(j)
                                    movings.pop(j)
                                    players.pop(i)
                                    movings.pop(i)
                                    #players.pop(k)
                                    #movings.pop(k)
                                    collision1=False
                                    collision2=False
                                    
                                    
                                    group1.add(player4)
                                    
                                    group1.update()
                                    #clock.tick(15)
        #aspect of the window
    window.fill(white)
    group1.draw(window)

    pygame.display.update()



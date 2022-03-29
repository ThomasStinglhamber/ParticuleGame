import pygame

from pygame.locals import *
from particule_player import Player
import buttonn
from affichage_parti import *
import random
from conversionchiffre_parti import *
from color_particule import *
from main import * 
from conversionSTR_DEF import *
from Paliers import *
#from tableau_periodique import *
#from tableau_periodique import tableau

pygame.init()
clock = pygame.time.Clock()
clock.tick(2)
display_width = 1500
display_height = 910
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,204)
bright_blue =(51,51,255)
bright_red=(100,0,0)
bright_green =(0,100,0)
block_color = (53,115,255)



SCREEN_WIDTH = 1260
SCREEN_HEIGHT = 900
LOWER_MARGIN = 0
SIDE_MARGIN = 360
largeur=300
#define game variables
ROWS = 20
MAX_COLS = 6
TILE_SIZE = 45
TILE_TYPES = 42
level = 0

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
screen=gameDisplay
display_width=SCREEN_WIDTH + SIDE_MARGIN
display_height=SCREEN_HEIGHT + LOWER_MARGIN
#gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Particule Game')
clock = pygame.time.Clock()
 
world_data = []
for row in range(ROWS):
	r = [-1] * MAX_COLS
	world_data.append(r)


interaction=[]

 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects_white(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def button_white(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects_white(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("arial",115)
        TextSurf, TextRect = text_objects("Particule Game", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",display_width/3,display_height*2/3,100,50,green,bright_green,mode)
        button("Quit",display_width*2/3,display_height*2/3,100,50,red,bright_red,pygame.quit)

        pygame.display.update()
       # clock.tick(15)
       
def affich_point():
    punnttos=checkpoint_noprint()
    smallText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = text_objects("Points : "+str(punnttos), smallText)
    TextRect.center = ((display_width*25/40),(display_height/25))
    gameDisplay.blit(TextSurf, TextRect)
    return punnttos


    
def affich_derniere_decouv(decouvertee):
    punnttos=checkpoint_noprint()
    smallText = pygame.font.SysFont("comicsansms",20)
    TextSurf, TextRect = text_objects("Derniere decouverte : "+str(decouvertee), smallText)
    TextRect.center = ((display_width*25/40),(display_height/58))
    gameDisplay.blit(TextSurf, TextRect)
                 
        
def mode():

    mode = True
    #intro=False
    while mode:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Mode de jeu", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        
        button_white("Combinaison",(display_width-largeur)/2,display_height*3/5,largeur,50,blue,bright_blue,game_loop)
        button_white("Désintégration",(display_width-largeur)/2,display_height*2/3,largeur,50,blue,bright_blue,PasImplementer)
        button_white("Mendeleïev",(display_width-largeur)/2,display_height*11/15,largeur,50,blue,bright_blue,PasImplementer)
        button_white("Back",(display_width-largeur)/2,display_height*4/5,largeur,50,black,black,game_intro)

        pygame.display.update()
        #clock.tick(15)

def periodique():
    tableau()
    
def draw_grid():
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, black, (SCREEN_WIDTH+(c * TILE_SIZE ), 0), (SCREEN_WIDTH+(c * TILE_SIZE ), SCREEN_HEIGHT))
	#horizontal lines
	for c in range(ROWS + 1):
		pygame.draw.line(screen, black, (SCREEN_WIDTH, c * TILE_SIZE), (SCREEN_WIDTH+SIDE_MARGIN, c * TILE_SIZE))


def tile_cote():
    img_list = []
    for x in range(TILE_TYPES):
        	img = pygame.image.load(f'img/tile/{x}.png').convert_alpha()
        	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        	img_list.append(img)
        
    
    img1 = pygame.image.load(f'img/background.png').convert_alpha()
    img2 = pygame.transform.scale(img1, (TILE_SIZE, TILE_SIZE))
    #make a button list
    button_list = []
    button_col = 0
    button_row = 0
    liste_decouv=[]
    nom_list = []
    file4 = open('ListeParticule.txt', 'r')
    parti=file4.read().splitlines()
    file4.close()
    
    #print(parti)
    for i in parti:
        chif=affichage_particule(i)
        liste_decouv.append(chif)
        
    #print(liste_decouv)
    nexlist=[]
    for k in range(TILE_TYPES):
        nexlist.append(k)
        
    
    for i in nexlist:#sorted(liste_decouv):# img_list
        if i in sorted(liste_decouv):
            tile_button = buttonn.Button( SCREEN_WIDTH+( 90*button_col+20),  65*button_row, img_list[i], 1)
            button_list.append(tile_button)
          
            button_col += 1
            if button_col == 4:
            		button_row += 1
            		button_col = 0
        if i not in sorted(liste_decouv): 
            tile_button = buttonn.Button( SCREEN_WIDTH+( 90*button_col+20),  65*button_row,img2, 1)
            button_list.append(tile_button)
            button_col += 1
            if button_col == 4:
            		button_row += 1
            		button_col = 0

    return button_list,liste_decouv

def nom_tile():
    #button_list = []
    button_col2 = 0
    button_row2 = 0
    liste_decouv=[]
    nom_list = []
    file4 = open('ListeParticule.txt', 'r')
    parti=file4.read().splitlines()
    file4.close()
    
    #print(parti)
    for i in parti:
        chif=affichage_particule(i)
        liste_decouv.append(chif)
        
    nexlist=[]
    for k in range(TILE_TYPES):
        nexlist.append(k)
        
    
    for j in nexlist:#sorted(liste_decouv):# img_list
        if j in sorted(liste_decouv):
            nomm=name_parti(j)
            #print(i,nomm)
            smallText2 = pygame.font.SysFont("comicsansms",10)
            TextSurf2, TextRect2 = text_objects(str(nomm), smallText2)
            TextRect2.center = ((SCREEN_WIDTH+( 90*button_col2+22+20),  65*button_row2+55))
            gameDisplay.blit(TextSurf2, TextRect2)
            nom_list.append(nomm)
            button_col2 += 1
            if button_col2 == 4:
            		button_row2 += 1
            		button_col2 = 0
                
        if j not in sorted(liste_decouv):
            nom_list.append(nomm)
            button_col2 += 1
            if button_col2 == 4:
            		button_row2 += 1
            		button_col2 = 0
                


def game_loop():
    gameExit = False

    white = (255, 255, 255)
    green = (0, 225, 0)
    red = (255, 0, 0)
    blue = ( 43, 255, 230)
    orange = ( 255, 170, 0)
    gray=(156,156,156)
    
    current_tile = 0
    #punnttos=checkpoint_noprint()

 
    #draw_grid()
    
    button_list,liste_decouv =tile_cote()
    #print(liste_decouv)
    #trie_button_list =sorted(button_list)
    players=[]
    NOM=[]
    movings=[]
    newone ='Nothing'
    group1 = pygame.sprite.Group()
    newlist=[]
    #print(len(button_list))
    for k in range(TILE_TYPES):
        newlist.append(k)

    while not gameExit:
        #gameDisplay.blit(TextSurf2, TextRect2)
        punnttos=affich_point()
        nom_tile()
        Palier1(punnttos)
        Palier2(punnttos)
        Palier3(punnttos)
        clock.tick(20)
        intera=[]
        button_count=0
        for button_count,i in zip(sorted(newlist),button_list):#enumerate(button_list): #
            #print('premier')
            #print(button_count,i)
            #if 
            if i.draw(screen) :
                if button_count in liste_decouv:
                    current_tile =button_count
                    name = name_parti(current_tile)
                    color = color_parti(name)
                    lastplayer=Player(name, color, random.randrange(1000), random.randrange(700))
                    test = Player.nom(name)
                    #print(test)
                    players.append(lastplayer)
                    movings.append(False)
                    NOM.append(test)
                    group1.add(players[-1])
                    group1.update()
                    #print(lastplayer)
                if button_count not in newlist:
                    current_tile =button_count
                    name = name_parti(current_tile)
                    group1.update()
                    
        group1.draw(gameDisplay)
        #newlist =button_list
        #print(newlist)
        #test=[None,None,None,None,None]
        #newlist =newlist + test
        
        pygame.draw.rect(screen, red, button_list[current_tile].rect, 3)
        trash = pygame.draw.rect(screen, red, (0,SCREEN_HEIGHT-100, 100, SCREEN_HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if len(players)>=1:
                for i in range(len(players)):
                    if len(players)>=1 and event.type == MOUSEBUTTONDOWN:
            
                        if len(players)>=1 and players[i].rect.collidepoint(event.pos):
                            movings[i] = True
                            
            
                    elif len(players)>=1 and event.type == MOUSEBUTTONUP:
                        movings[i] = False
            
                    elif len(players)>=1 and event.type == MOUSEMOTION and movings[i]:
                         players[i].rect.move_ip(event.rel)
        
                    #trashcan = pygame.sprite.collide_rect(players[i], trash)
                    if len(players)>=1 and players[i].rect.colliderect(trash) :
                        players.clear()
                        NOM.clear()
                        movings.clear()
                        group1.empty()
                        time.sleep(1)
                    for j in range(len(players)):
                            for k in range(len(players)):
                                if len(players)>=3:
                                    #gameDisplay.blit(TextSurf2, TextRect2)
                                    if i != j and i != k and j != k:
                                        collision1 = pygame.sprite.collide_rect(players[i], players[j])
                                        collision2 = pygame.sprite.collide_rect(players[i], players[k])
                                        
                                        if collision1 == True and collision2 == False:
                                            interaction=[NOM[i],NOM[j]]
                                            
                                            decouv=Principal(interaction)
                                            newone =decouv
                                            
                                            if decouv !='':
                                                 del players[0:len(players)]
                                                 del NOM[0:len(NOM)]
                                                 del movings[0:len(movings)]
                                                 group1.empty()
                                                 time.sleep(1)
                                                 button_list,liste_decouv=tile_cote()
                                                 nom_tile()
                                                 #gameDisplay.blit(TextSurf2, TextRect2)

                                                 #break
                                        #print(collision1,collision2)
                                        if collision1 == True and collision2 == True:
                                            interaction=[NOM[i],NOM[j],NOM[k]]
                                           
                                            decouv=Principal(interaction)
                                            newone =decouv
                                            
                                            if decouv !='':
                                                 players.clear()
                                                 NOM.clear()
                                                 movings.clear()
                                                 group1.empty()
                                                 time.sleep(1)
                                                 button_list,liste_decouv =tile_cote()
                                                 nom_tile()
                                                 #gameDisplay.blit(TextSurf2, TextRect2)

                                                 #break
                                            #time.sleep(3)
            affich_derniere_decouv(newone)
            pygame.display.update()
        gameDisplay.fill(white)
        
        pygame.draw.rect(screen, gray, (SCREEN_WIDTH,0, SIDE_MARGIN, SCREEN_HEIGHT))
        nom_tile()
        button_white("Menu",(display_width-largeur-200),display_height*17/19,100,50,black,black,mode)
            
    return interaction
        
            
        
    
    
def PasImplementer():

    PasImplementer = True
    #intro=False
    while mode:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Pas encore implementé", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
        largeur=300
        button_white("Back",(display_width-largeur)/2,display_height*4/5,largeur,50,black,black,mode)

        pygame.display.update()
        clock.tick(15)
        


game_intro()
mode()
INTERACTION=game_loop()
PasImplementer()
#print(INTERACTION)

pygame.quit()
quit()

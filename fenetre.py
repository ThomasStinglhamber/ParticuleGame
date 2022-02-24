import pygame

from pygame.locals import *
from particule_player import Player
import buttonn

pygame.init()
 
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



SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 900
LOWER_MARGIN = 0
SIDE_MARGIN = 270
#define game variables
ROWS = 20
MAX_COLS = 6
TILE_SIZE = 45
TILE_TYPES = 21
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
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Particule Game", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",display_width/3,display_height*2/3,100,50,green,bright_green,mode)
        button("Quit",display_width*2/3,display_height*2/3,100,50,red,bright_red,pygame.quit)

        pygame.display.update()
       # clock.tick(15)
        
        
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
        largeur=300
        button_white("Combinaison",(display_width-largeur)/2,display_height*3/5,largeur,50,blue,bright_blue,game_loop)
        button_white("Désintégration",(display_width-largeur)/2,display_height*2/3,largeur,50,blue,bright_blue,PasImplementer)
        button_white("Mendeleïev",(display_width-largeur)/2,display_height*11/15,largeur,50,blue,bright_blue,PasImplementer)
        button_white("Back",(display_width-largeur)/2,display_height*4/5,largeur,50,black,black,game_intro)

        pygame.display.update()
        clock.tick(15)
    
def draw_grid():
	#vertical lines
	for c in range(MAX_COLS + 1):
		pygame.draw.line(screen, black, (SCREEN_WIDTH+(c * TILE_SIZE ), 0), (SCREEN_WIDTH+(c * TILE_SIZE ), SCREEN_HEIGHT))
	#horizontal lines
	for c in range(ROWS + 1):
		pygame.draw.line(screen, black, (SCREEN_WIDTH, c * TILE_SIZE), (SCREEN_WIDTH+SIDE_MARGIN, c * TILE_SIZE))

    
def game_loop():

    white = (255, 255, 255)
    green = (0, 225, 0)
    red = (255, 0, 0)
    blue = ( 43, 255, 230)
    orange = ( 255, 170, 0)
    current_tile = 0
    #load the player
    player1 = Player("quark down", red, 200, 100)
    player2 = Player("quark up", blue, 800, 200)
    player3 = Player("quark bottom", orange, 500, 100)
    player4 = Player("proton", green, 1380/2,700/2) #arriver à mettre la position de collision des 3 particules
    
    gameExit = False
    moving1 = False
    moving2 = False
    moving3 = False
    
    group1 = pygame.sprite.Group()
    group1.add(player1, player2, player3)
    
    img_list = []
    for x in range(TILE_TYPES):
        	img = pygame.image.load(f'img/tile/{x}.png').convert_alpha()
        	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        	img_list.append(img)
    #make a button list
    button_list = []
    button_col = 0
    button_row = 0
    for i in range(len(img_list)):
        	tile_button = buttonn.Button( SCREEN_WIDTH+( 45*button_col),  45*button_row , img_list[i], 1)
        	button_list.append(tile_button)
        	button_col += 1
        	if button_col == 4:
        		button_row += 1
        		button_col = 0
 
    while not gameExit:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
    
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
            collision1 = pygame.sprite.collide_rect(player1, player2)
            collision2 = pygame.sprite.collide_rect(player3, player2)
            if collision1 == True and collision2 == True:
                group1.remove(player1,player2,player3)
                startend = True
                group1.add(player4)
                group1.update()
        
        
            pygame.display.update()
            
        gameDisplay.fill(white)
        group1.draw(gameDisplay)
            
        pygame.draw.rect(screen, green, (SCREEN_WIDTH,0, SIDE_MARGIN, SCREEN_HEIGHT))
        draw_grid()
        
        
        button_count=0
        for button_count,i in enumerate(button_list):
            if i.draw(screen):
                current_tile =button_count
                print(current_tile)
                group1.add(player4)
                group1.update()
                
        pygame.draw.rect(screen, red, button_list[current_tile].rect, 3)
        
        
        
    
    
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
game_loop()
PasImplementer()



pygame.quit()
quit()

liveszkg = 1
import sys,pygame,random,time
from pygame.locals import *

def print_text(font,x,y,text,color=(255,255,255)):
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb catching game")
font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220,50,50
yellow = 230,230,50
black = 0,0,0

lives = liveszkg
score = 0
game_over = True
mouse_x = mouse_y = 0
pos_x = 300
pos_y = 460
bomb_x = random.randint(0,500)
bomb_y = -50
vel_y = 0.7

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION :
            mouse_x,mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = liveszkg
                score = 0
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
    screen.fill((0,0,100))
    
    if game_over:
        print_text(font1,100,200,"<CLICK TO PLAY>")
    else:
        bomb_y += vel_y
        
        if bomb_y > 500:
            bomb_x = random.randint(0,500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        
        elif bomb_y > pos_y:
            if bomb_x > pos_x < pos_x + 120:
                score += 10
                bomb_x = random.randint(0,500)
                bomb_y = -50
        
        pygame.draw.circle(screen,black,(bomb_x-4,int(bomb_y)-4),30,0)
        pygame.draw.circle(screen,yellow,(bomb_x,int(bomb_y)),30,0)
        
        pos_x = mouse_x
        if pos_x < 0:
        	pos_x=0
        elif pos_x > 500:
        	pos_x=500
        
        pygame.draw.rect(screen,black,(pos_x-4,pos_y-4,120,40),0)
        pygame.draw.rect(screen,red,(pos_x,pos_y,120,40),0)

    print_text(font1,0,0,"LIVES:" + str(lives))

    print_text(font1,500,0,"SCORE:" + str(score))
    
    print_text(font1,0,20,"SPEED:" + str(vel_y))
    
    vel_y = 0.7 + score / 1000
    
    pygame.event.set_grab(True)

    pygame.display.update()


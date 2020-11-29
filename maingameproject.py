#In this chapter we will learn about the following about game development
#we will learn 
#player movements 
#Automatic non player movements 
#collision detection 
#And finally Displaying the images on the screen
#lets create our basic pygame settings 
import pygame ,sys
from pygame.locals import *


pygame.init()

#setting up the main screen 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Bricks game')
fps = pygame.time.Clock()

background = pygame.Color(100,149,237)

#bat init
bat = pygame.image.load('bat.png')
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (0,playerY)
#ball init 
ball = pygame.image.load('ball.png')
ballstartY = 300
ballspeed = 3
ballServed = False
ballRect = ball.get_rect()
bx,by  = (24,ballstartY)
sx,sy = (ballspeed, ballspeed)

ballRect.topleft = (bx,by)

#brick init



#now creating main game loop
while True:
    screen.fill(background)
    screen.blit(bat,batRect)
    screen.blit(ball,ballRect) #wrinting the ball on the screen
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos #this is position method finds out the mouse movement position and assigns it to the mousex,y
            if (mousex < 800-55):
                batRect.topleft = (mousex,playerY) # this if statement binds the bat rect with variables mousex and mousey
            else:
                batRect.topleft = (800-55,playerY) #if mouse is at 745 then also it will move the bat

    #main game logic
    bx += sx #here iam adding 3px distance for ball on each frame so by d=sxt ball 180px horizontally on each frame 
    by += sy #so the ball gets added  3px x and y coordinate so that it moves horizontally
    ballRect.topleft = (bx,by)
    if (by < 0): #now giving the main logic of colliding the walls  if the ball is at 0px or out side of screen
        by = 0   #then it must come to the 0 pixel 
        sy *=-1  #then the ball speed get negatived and it moves in opposite direction 
    if (by >= 600-8):#this is the same logic for all the four sides this is down wall
        by = 600 -8 
        sy *= -1
    if (bx < 0): #this is for the left wall
        bx = 0
        sx *= -1
    if (bx >= 800-8):#And finally this for the right wall
        bx = 800 - 8
        sx *= -1
    pygame.display.update()
    fps.tick(60)


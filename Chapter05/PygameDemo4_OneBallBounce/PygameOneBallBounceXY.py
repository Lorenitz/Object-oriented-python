# pygame demo 4(a) - one image, bounce around the window using (x,y) coord

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3


# 3 initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc

ballimage = pygame.image.load('images/ball.png')

# 5 - Initialize variables

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_WEIGHT = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_WEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Loop forever

while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        #clicked the close button? Quit game and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed #reverse X direction
 
    if (ballY < 0) or (ballY >= MAX_WIDTH):
        ySpeed = -ySpeed #reverse Y direction           
        
    # Update the b all's location, usgin the speed in two directions
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed    
        
    # 9 Clear the window

    window.fill(BLACK)                
    
    # 10 - draw all window elements
    
    window.blit(ballimage, (ballX, ballY)) # draw the ball
    
    # 11 - Update the window
    pygame.display.update()
    
    #Slow things down a bit
    clock.tick(FRAMES_PER_SECOND) #make pygame wait
    
    
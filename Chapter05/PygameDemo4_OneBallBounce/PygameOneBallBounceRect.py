#Pygame demo 4(b) - one image, bounce around the window using rects

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
N_PIXELS_PER_FRAME = 3


# 3 initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc

ballimage = pygame.image.load('images/ball.png')

# 5 - Initialize variables
ballRect = ballimage.get_rect() # To get the bounding rectangle of image
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_WEIGHT = WINDOW_WIDTH - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_WEIGHT)
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
            
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed        
        
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        
    # Update the ball's rectangle ujsing the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    
    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    window.blit(ballimage, ballRect)
    
    # 11 - update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)             
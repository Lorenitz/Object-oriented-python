# pygame demo 2 - one image, click and move

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 1
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_WEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# 3 initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc

ballimage = pygame.image.load('images/ball.png')

# 5 - Initialize variables

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_WEIGHT)

ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6 - Loop forever

while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        #clicked the close button? Quit game and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # see if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            # mousex, mouseY = event.pos # Could do this if we needed it
            # Check if the click was in the rect of the ball
            # If so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_WEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 Do any per frame action

    # 9 Click the window

    window.fill(BLACK)                
    
    # 10 - draw all window elements
    # Draw the ball at the randomized location
    
    window.blit(ballimage, (ballX, ballY))
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)
    
    
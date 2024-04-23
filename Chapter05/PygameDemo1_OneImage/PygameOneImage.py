# pygame demo 1 - draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 1

# 3 initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc

ballimage = pygame.image.load('images/ball.png')

# 5 initialize variables

# 10 draw all windows elements
# draw ball at position 100 accross (x) and 200 down (y)

window.blit(ballimage, (100,200))

# 11 update the window

pygame.display.update()

# 12 slow things down a bit

clock.tick(FRAMES_PER_SECOND) #make pygame wait

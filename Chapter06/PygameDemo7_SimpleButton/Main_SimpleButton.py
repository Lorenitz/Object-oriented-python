# pygame demo 7  SimpleButton test

# 1 - Import packages
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
# Create an instance of a SimpleButton

oButton = SimpleButton(window, (150,30), 'images/buttonUp.png',
                       'images/buttonDown.png')

# 6 - Loop forever:

while True:
    # 7 - Check for and handle events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
            
        # Pass the event to the button, see if it has ben clicked on
        if oButton.handleEvent(event):
            print('User has clicked the button')
    
    # 8 - Do any per frame actions
    
    # 9 - Clear the window
    window.fill(GRAY)
    
    oButton.draw() #Draw the button
    
    # 11 - Update the window
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)      
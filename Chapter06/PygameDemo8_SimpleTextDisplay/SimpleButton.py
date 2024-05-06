# Simple button class

# Uses a "state machine" approach

import pygame
from pygame.locals import *


class SimpleButton():
    # Used to track the state of the button
    STATE_IDLE = 'idle' # button is up, mouse not over button
    STATE_ARMED = 'armed' # button is down, mouse over button
    STATE_DISARMED = 'disarmed' # Clicked down on button, rolled off
    
    # constructor method
    # self: A reference to the current instance of the class, used to access variables and methods.
    # window: A parameter representing the window in which the button will be displayed.
    # loc:  A parameter representing the location (coordinates) of the button.
    def __init__(self, window, loc, up, down):
        self.window = window # This line assigns the window parameter to the window attribute of the instance. This attribute is used to keep a reference to the window in which the button is displayed.
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down) # Similarly, this line loads the image for the button's "down" 
        # state from the file specified by the down parameter and assigns it to the surfaceDown attribute of the instance.
        
        # Get the rect of the button (used to see if the mouse is over the button)
        # This line gets the rectangle object that has the dimensions of the surfaceUp image and assigns it to the rect attribute of the instance. 
        # The rectangle object is used to determine the position and size of the button.
        self.rect = self.surfaceUp.get_rect()
        # These lines set the position of the button's rectangle to the location specified by the loc parameter.
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]
        
        self.state = SimpleButton.STATE_IDLE # This line initializes the button's state to STATE_IDLE, indicating that the button is up and the mouse is not over it.
        
    def handleEvent(self, eventObj):
        #This method will return true if the user clicks the button
        #Normally returns false
        
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False
        
        eventPointinButtonRect = self.rect.collidepoint(eventObj.pos)
        
        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointinButtonRect:
                self.state = SimpleButton.STATE_ARMED
                
        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointinButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True # Clicked!
        
            if (eventObj.type == MOUSEMOTION) and (not eventPointinButtonRect):
                self.state = SimpleButton.STATE_DISARMED
        
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointinButtonRect:
                self.state = SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE
        return False        
    
    #This method uses the state of the object's instance variable self.state to decide which image (up or down) to draw.
    # The draw method in the SimpleButton class is responsible for rendering the button's appearance on the screen. 
    # It uses the blit method from Pygame, which is a fundamental function for drawing surfaces onto a screen.
    def draw(self):
        # Draw the button's current appearance to the window
        # This line checks if the button's current state is STATE_ARMED, which means the button is pressed and the mouse is over it.
        
        # If the button is in the STATE_ARMED state, this line uses the blit method to draw the button's "down" image (self.surfaceDown) onto the window at the button's location (self.loc). 
        # The blit method is used to draw one image onto another, making it essential for rendering graphics in Pygame
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        # In the else block, this line uses the blit method to draw the button's "up" image (self.surfaceUp) onto the window at the button's location (self.loc).
        # This is the button's appearance when it is not pressed or when the mouse is not over it.
        else: #IDLE or disarmed
            self.window.blit(self.surfaceUp, self.loc)
                
        
                                
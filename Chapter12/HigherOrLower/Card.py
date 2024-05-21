# Card Class

import pygame
import pygwidgets

class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOCard.png')
    
    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value
        fileName = 'images/' + self.cardName + '.png'
        # Set some starting location; use setLoc below to change
        self.images = pygwidgets.ImageCollection(window, (0,0),
                                                 {'font': fileName,
                                                  'back': Card.BACK_OF_CARD_IMAGE}, 'back')
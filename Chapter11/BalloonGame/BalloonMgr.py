#  Balloon manager

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from Balloon import *

# Balloon manages a list of Balloon objects
class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        
    def start(self):
        self.balloonList = [] 
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0
        
        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice((BalloonSmall,
                                                                    BalloonMedium,
                                                                    BalloonLarge))
            
            oBallon = randomBalloonClass(self.window, self.maxWidth, self.maxHeight, balloonNum)        
            
            #add each balloon object into the list
            self.balloonList.append(oBallon)
            
    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # go reversed so top most balloon gets popped
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0: #remove this balloon
                        self.balloonList.remove(oBalloon)
                        self.nPopped = self.nPopped + 1
                        self.score = self.score + nPoints
                    return # no need to check others
                
    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                # balloon went off the top, remove it
                self.balloonList.remove(oBalloon)
                self.nMissed = self.nMissed + 1
    
    def getScore(self):
        return self.score

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()            
                
                
                                
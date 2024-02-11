# DimmerSwitch class with test code

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        
    def turnOn(self):
        self.switchIsOn = True
        
    def turnOff(self):
        self.switchIsOn = False
        
    def raiselevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
            
    def lowerlevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
            
    #extra method for debugging:
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Bright is:', self.brightness)                
                    
# Main code

oDimmer = DimmerSwitch()

# Turn switch on, and raise the level 5 times

oDimmer.turnOn()

oDimmer.raiselevel()                    
oDimmer.raiselevel()
oDimmer.raiselevel()             
oDimmer.raiselevel()
oDimmer.raiselevel()
oDimmer.show()

#Lower the level 2 times, and turn switch  off

oDimmer.lowerlevel()
oDimmer.lowerlevel()
oDimmer.turnOff()
oDimmer.show()

oDimmer.turnOn()
oDimmer.raiselevel()
oDimmer.raiselevel()
oDimmer.raiselevel()
oDimmer.show()


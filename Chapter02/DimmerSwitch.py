class DimmerSwitch():
    def __init__(self):
        # initialize the object as false
        self.switchIsOn = False
        self.brightness = 0
        
    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True
        
    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False        
    
    def raiselevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    
    
    def lowerlevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
    
    #Extra method for debugging:    
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)
        
        
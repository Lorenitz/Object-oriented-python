# DimmerSwitch class with test code

class DimmerSwitch():
    def __init__(self, label):
        self.label = label
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
        print('Label:', self.label)
        print('Light is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)   
        
#Create two DimmerSwitch objects
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer2 = DimmerSwitch('Dimmer2')

#Tell oDimmer1 to raise its level
oDimmer1.raiselevel()

#Tell oDimmer2 to raise its level
oDimmer2.raiselevel()
        
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
                    
#Create first DimmerSwitch, turn it on, and raise the level twice

oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiselevel()
oDimmer1.raiselevel()

oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiselevel()
oDimmer2.raiselevel()
oDimmer2.raiselevel()

oDimmer3 = DimmerSwitch('Dimmer3')

oDimmer1.show()
oDimmer2.show()
oDimmer3.show()

                  
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
                    
#Create 3 dimmerswitch objects

oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()


oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
                  
oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
print()
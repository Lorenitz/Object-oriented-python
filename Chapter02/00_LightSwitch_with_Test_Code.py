class LightSwitch():
    def _init_(self):
        # initialize the object as false
        self.switchIsOn = False
        
    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True
        
    def turnOff(self):
        # turn the switch off
        self.switchIsOff = False        
        
    def show(self): #added for testing
        print(self.switchIsOn)
        
        
# Main code

oLightSwitch = LightSwitch() #create a LightSwitch object

#Calls to method:

oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()            
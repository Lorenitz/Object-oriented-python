# Procedural light switch

def turnOn():
    global switchIsOn
    #turn the light on
    switchIsOn = True
    
def turnOff():
    global switchIsOn    
    switchIsOn = False
    
#Main code

switchIsOn = False # a global Boolean variable

# Test Code:

print(switchIsOn)
turnOn()

print(switchIsOn)
turnOff()

print(switchIsOn)
turnOn()

print(switchIsOn)
    
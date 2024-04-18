import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows #save away
        self.nCols = nCols #save away
        self.myRow = random.randrange(self.nRows) #chooses a random row
        self.myCol = random.randrange(self.nCols) #chooses a random col
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed, +1) #chooses an X Speed
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed, +1) #chooses an Y Speed
        
    def move(self):
        self.myRow = (self.myRow + self.mySpeedX) % self.nRows    
        self.myCol = (self.myCol + self.mySpeedY) % self.nCols


#with this monster class, we can create a list of monster objects like this:

N_Monsters = 20
N_ROWS = 100 #could be any size        
N_COLS = 200 #could be any size

MAX_SPEED = 4

monsterList = [] #starts with an empty list

for i in range(N_Monsters):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)
    monsterList.append(oMonster)


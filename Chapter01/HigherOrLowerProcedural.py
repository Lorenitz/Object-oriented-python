import random

#card constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in the deck and this function returns a random card from the deck
def getCard(deckListIn):
    #The pop() function in Python is a built-in method used to remove an item from a list or dictionary at a specific index
    # and return it
    thisCard = deckListIn.pop()#pop one of the top of the deck and return
    return thisCard

#Pass in a deck and this function returns a shuffled copy of the deck    
def shuffle(deckListIn):
    deckListOut= deckListIn.copy() #make a copy from the starting deck
    random.shuffle(deckListOut)
    return deckListOut
    
#Main Code
print('Welcome to Higher or Lower')
print('You have to choose whether the next card to be shown will be higher or lower than the current card')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start')

print()

startingDeckList = []

# For each suit, it will loop through the rank tuple (13 times), that is why we use the enumerate
# and finally it will append each loop to the startingDeckList dictionary
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)
        
score = 50

while True: #playmultipletimes
    print()
    gameDecklist = shuffle(startingDeckList)
    currentCardDict = getCard(gameDecklist)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + 'of' + currentCardSuit)
    print()
    
    for cardNumber in range(0, NCARDS): #play one game of this many cards
      currentCardRank
      currentCardSuit
      #  answer = input('Will the next card be higher or lower than the ' + currentCardRank + ' of '
      #                 + currentCardSuit + '? (enter h or 1):')
      #  answer = answer.casefold() #force lowercase
              
    nextCardDict = getCard(gameDecklist)
    nextCardRank = nextCardDict['rank']
    nextCardSuit = nextCardDict['suit']
    nextCardValue = nextCardDict['value']
    print('Next card is:', nextCardRank + ' of ' + nextCardSuit)
    
    if answer == 'h':
        if nextCardValue > currentCardValue:
            print('You got it right, it was higher')
            score = score + 20
        else:
            print("Sorry it was not higher")
            score = score - 15
    elif answer == '1':
        if nextCardValue < currentCardValue:
            score = score + 20
            print('You got it right, it was lower')
        else:
            score = score - 15
            print('Sorry, it was not lower')
            
    print('Your score is:', score)
    print()
    currentCardValue = nextCardValue
    currentCardSuit = nextCardSuit
    
    goAgain = input('To play again, press Enter, or "q" to quit: ')
    if goAgain == 'q':
        break               
    
print('Ok bye')    
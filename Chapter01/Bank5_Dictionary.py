#Non-OOP Bank
#Version 5
#Any number of accounts - with a list of dictionaries


accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password': aPassword}
    accountsList.append(newAccountDict)
    
def show(accountNumber):
    global accountList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Name', thisAccountDict['name'])
    print('     Balance', thisAccountDict['balance'])
    print('     Password', thisAccountDict['password'])
    print()
    
def getBalance(accountNumber, password):
    global accountList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']


#--snipped additional deposit() and withdraw() functions--


#Create two sample accounts
print("Joe's account is account number:", len(accountList))
newAccount("Joe", 100, 'soup')
print("Mary's account is account number:", len(accountList))
newAccount("Mary", 12345, 'nuts')  
    
    
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make the deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do?')
    action = action.lower() #force lowercase
    action = action[0]
    print()
    
    if action == 'b':
        print('Get Balance: ')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    
    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount - int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        
        # newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        #if newBalance is not None:
        #   print('Your new balance is:', newBalance )   
    
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name?')
        userStartingAmount = input('What is the amount of your initial deposit?')
        userStartingAmount = int(userStartingAmount)
        userStartingAmount = input('What password would you like to use for this account?')
        userStartingAmount = int(userStartingAmount)
        
        userAccountNumber = len(accountList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new result number is:', userAccountNumber)    
    
    
    print('Done')                
    
        
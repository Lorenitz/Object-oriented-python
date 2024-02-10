accountNameList = []
accountBalanceList = []
accountPasswordsList = []
accountNumber = ''

def newAccount(name, balance, password):
    global accountNameList, accountBalanceList, accountPasswordsList
    
    accountNameList.append(name)
    accountNameList.append(balance)
    accountNameList.append(password)
    
def show(AccountNumber):
    global accountNameList, accountBalanceList, accountPasswordsList    
    print('Account', accountNumber)
    print('     Name', accountNameList[accountNumber])
    print('     Balance', accountBalanceList[accountNumber])
    print('     Name', accountPasswordsList[accountNumber])
    print()

def getBalance(accountNumber, password):
    global accountNameList, accountBalanceList, accountPasswordsList       
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalanceList[accountNumber]

#Create two sample accounts
print("Joe's account is account number:", len(accountNameList))
newAccount("Joe", 100, 'soup')
print("Mary's account is account number:", len(accountNameList))
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
    
    print('Done')            
accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    
def show():
    global accountName, accountBalance, accountPassword
    print('     Name', accountName)
    print('     Balance', accountBalance)
    print('     Password', accountPassword)
    print()
    
def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    
    if password != accountPassword:
        print('Incorrect password')
        return None
    
    accountBalance = accountBalance + amountToDeposit
    return accountBalance
    
def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    
    if password != accountPassword:
        print('Incorrect password for this account')
        return None
    
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    
    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount("Joe", 100, 'soup')

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
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is:', accountBalance)
            
    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect password')
            
        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is:' , accountBalance)    
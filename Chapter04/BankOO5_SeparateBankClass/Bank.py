# Bank that manages a dictionary of Account Objects

from Account import *

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0
        
def createAccount(self, theName, theStartingAmount, thePassword):
    oAccount = Account(self, theName, theStartingAmount, thePassword)
    newAccountNumber = self.nextAccountNumber
    self.accountDict[newAccountNumber] = oAccount
    # Increment to prepare for next account to be created
    self.nextAccountNumber = self.nextAccountNumber + 1
    return newAccountNumber       

def openAccount(self):
    print('*** Open Account***')
    userName = input('What is the name for the new user accoount?')
    userStartingAmount = input('What is the starting balance for this account?')
    userStartingAmount = int(userStartingAmount)
    userPassword = input('What is the password you want to use for this account?')
    
    userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
    print('Your new account is:', userAccountNumber)
    print()
    
def closeAccount(self):
    print('*** Close Account ***')    
    userAccountNumber = input('What is your account number?')
    userAccountNumber = int(userAccountNumber)
    userPassword = input('What is your password?')
    oAccount = self.accountDict[userAccountNumber]
    theBalance = oAccount.getBalance(userPassword)
    
    if theBalance is not None:
        print('You had', theBalance, 'in your account, which is being returned to you')
        #Remove user's account from dictionary of account
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')

def balance(self):
    print('*** Get Balance ***')
    userAccountNumber = input('Please enter your account number:')
    userAccountNumber = int(userAccountNumber)
    userAccountPassword = input('Please enter the password: ')
    oAccount = self.accountsDict[userAccountNumber]
    theBalance = oAccount.getBalance(userAccountPassword)
    if theBalance is not None:
        print('Your balance is:', theBalance)

def deposit(self):
    print('*** Deposit ***')
    accountNum = input('Please enter the account number:')
    accountNum = int(accountNum)
    
    depositAmount = input('Please enter amount to deposit:')
    depositAmount = int(depositAmount)
    userAccountPassword = input('Please enter the password:')
    # First, we get the object account, based on the account number
    oAccount = self.accountsDict[accountNum]
    # Once we have it, we call the deposit function passing depositamount and password
    theBalance = oAccount.deposit(depositAmount, userAccountPassword)
    if theBalance is not None:
        print('Your new Balance is:', theBalance)
        
def show(self):
    print('*** Show ***')
    for userAccountNumber in self.accountsDict:
        oAccount = self.accountsDict[userAccountNumber]
        print(' Account:', userAccountNumber)
        oAccount.show()
  
def withdraw(self):
    print('*** Withdraw ***')
    userAccountNumber = input('Please enter your account number: ')
    userAccountNumber = int(userAccountNumber)
    userAmount = input('Please enter the amount to withdraw: ')
    userAmount - int(userAmount)
    userAccountPassword = input('Please enter the password: ')
    oAccount = self.accountsDict[userAccountNumber]
    theBalance = oAccount.withdraw(userAmount, userAccountPassword)
    if theBalance is not None:
        print('Withdraw:', userAmount)
        print('Your new balance is:', theBalance)                    
        
        
                
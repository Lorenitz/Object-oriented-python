# Test program using accounts
# Version 3, using dictionary of accounts

# Bring in all the code from the Account class file

from Account import *

accountsDict = {}

nextAcccountNumber = 0

# Create two accounts:

oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAcccountNumber
accountsDict[joesAccountNumber] = oAccount

print('Account number for Joe is:', joesAccountNumber)
nextAcccountNumber = nextAcccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marrysAccountNumber = nextAcccountNumber
accountsDict[marrysAccountNumber] = oAccount
print('Account number for Mary is:', marrysAccountNumber)
nextAcccountNumber = nextAcccountNumber + 1


accountsDict[joesAccountNumber].show()
accountsDict[marrysAccountNumber].show()
print()

# Call some methods on the different accounts

print('Calling method of the two accounts...')
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marrysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marrysAccountNumber].deposit(100, 'MarysPassword')

accountsDict[joesAccountNumber].show()
accountsDict[marrysAccountNumber].show()

# Create another account with information from the user
print()

print()
userName = input('What is the name for the new user account?')
userBalance = input('What is the starting balance for this account?')
userBalance = int(userBalance)
userPassword = input("What is the password you want to use for this account?")
oAccount = Account(userName, userBalance, userPassword)

newAccountNumber = nextAcccountNumber

accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAcccountNumber = nextAcccountNumber + 1

accountsDict[newAccountNumber].show()

# Let's deposit 100 into the new account

accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)

print()

print("After depositing 100, the user's balance is:", userBalance)

# show the new account
accountsDict[newAccountNumber].show()

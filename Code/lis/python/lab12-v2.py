#Lab 12  ATM

'''
v1
Let's represent an ATM with a class containing two attributes: a balance and an interest rate.
A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account

v2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string
to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your
 class for printing out the list of transactions, and add a transactions option to your REPL loop.
'''

#create class
class ATM: 
  def __init__(self):
    # attributes
    self.balance = 0
    self.interest = 0.001
    self.transactions = []

  # class methods
  def check_balance(self):
    # returns the account balance
    return self.balance

  def deposit(self, amount):
    # deposits the given amount in the account
    self.balance += amount

    deposit_transaction = "user deposited ${:.2f}".format(amount)
    self.transactions.append(deposit_transaction)
    
  def check_withdrawal(self, amount):
    # returns true if the withdrawn amount won't put the account in the negative
    return self.balance > amount

  def withdraw(self, amount):
    # withdraws the amount from the account and returns it  
    if self.check_withdrawal(amount):
      self.balance -= amount

      withdraw_transaction = "user withdraw ${:.2f}".format(amount)
      self.transactions.append(withdraw_transaction)

  def calc_interest(self):
    # returns the amount of interest calculated on the account
    return (self.balance * self.interest)

  def print_transactions(self):
    # returns list of deposits and withdrawals
    for items in self.transactions:
      print(items)

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method 
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
      print(f'A list of your recent transactions: ')
      atm.print_transactions() # call the transactions() method
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of transactions')
        print('exit - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
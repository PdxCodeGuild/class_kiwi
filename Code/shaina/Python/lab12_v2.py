# Lab 12: Version 2
'''
Have the ATM maintain a list of transactions. 
Every time the user makes a deposit or withdrawal, add a string to a list saying 
'user deposited $15' or 'user withdrew $15'. 
Add a new method print_transactions() to your class for printing out the list of transactions, 
and add a transactions option to your REPL loop.
'''
class ATM:
    def __init__(self, balance = 0, interest_rate = 0.001):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self): # returns the account balance
        return self.balance

    def deposit(self, amount): # deposits the given amount in the account
        self.balance += amount
 
        return amount

    def check_withdrawal(self, amount): # returns true if the withdrawn amount won't put the account in the negative
        if self.balance - amount > 0:
            return True
        else:
            return False

    def withdraw(self, amount): # withdraws the amount from the account and returns it
        self.balance -= amount
        return amount

    def calc_interest(self): # returns the amount of interest calculated on the account
        self.interest_rate *= self.balance
        return self.interest_rate

    def print_transactions(self, transactions): # Added print_transactions() class to print out the list of transactions
        transactions = '\n'.join(transactions)
        return f'Transactions:\n{transactions}'
# ____________________________________________________________________________________________ #
# Prewritten Code

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
transactions = [] # List of transactions
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        transactions.append(f'user deposited {amount}') # add a string to transactions list
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            transactions.append(f'user withdrew {amount}') # add a string to transactions list
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        transactions = atm.print_transactions(transactions)
        print(transactions)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - list of transactions') # transactions option added to REPL loop
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
        
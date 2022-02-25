#Lab 12 - ATM - Version 2 - Working Final

#Version 2
#Have the ATM maintain a list of transactions. Every time the user makes a
#deposit or withdrawal, add a string to a list saying 'user deposited $15' or
#'user withdrew $15'. Add a new method print_transactions() to your class for
#printing out the list of transactions, and add a transactions option to your
#REPL loop.

class ATM:
    def __init__(self, balance = 0, interest = .001, transactions = []):
        self.balance = balance
        self.interest = interest
        self.transactions = transactions
    
    def check_balance(self):
        self.transactions.append('User checked their balance')
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False
    
    def withdraw(self, amount):
        self.balance - amount
        self.transactions.append(f'User withdrew ${amount}')
        return amount
    
    def calc_interest(self):
        return self.balance * self.interest

    def print_transactions(self):
        return self.transactions
    
    
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
        transact = atm.print_transactions() #call the print_transactions() method
        print(f'User Transactions: {transact}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
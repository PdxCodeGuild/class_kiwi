"""
Let's represent an ATM with a class containing two attributes: 
a balance and an interest rate. A newly created account will 
default to a balance of 0 and an interest rate of 0.1%. Implement 
the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
"""


class ATM:
    def __init__(self, balance=0, interest=.001):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")
        return self.balance

    def calc_interest(self):
        return round((self.balance * self.interest), 2)

    def print_transactions(self):
        return "\n".join(self.transactions)


'''
Have the ATM maintain a list of transactions. Every time the user 
makes a deposit or withdrawal, add a string to a list saying 'user 
deposited $15' or 'user withdrew $15'. Add a new method print_transactions() 
to your class for printing out the list of transactions, and add a 
transactions option to your REPL loop.
'''


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'print':
        transactions = atm.print_transactions()
        print(f"Transactions: {transactions}")
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('print    - prints transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

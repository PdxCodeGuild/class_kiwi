"""
ATM
Version 1
Timothy Hampton
Hampton12101@gmail.com 
2/24/2022
"""


transactions = {
        "Withdrawals": [],
        "Deposits": []
        }


class ATM:    # create an instance of our class

    def __init__(self,balance=0,interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def check_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        transactions["Deposits"].append(amount)
    def check_withdrawal(self,amount):
        if amount <= self.balance:
            return True
        else:
            return False
    def withdraw(self,amount):
        self.balance -= amount
        transactions["Withdrawals"].append(amount)
    def calc_interest(self):
        interest = self.balance * 0.1
        return interest
    def print_transactions(self):
        return transactions
        
atm = ATM(0,0.1)

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
        print(f'Your deposit history is {transactions["Deposits"]}')
        print(f'Your withdrawal history is {transactions["Withdrawals"]}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions - view a list of your transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
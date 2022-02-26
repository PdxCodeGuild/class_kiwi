## Lab 12: ATM

# Create a class that represents an ATM with 2 attributes, balance and interest rate. 
#version 1
# class ATM:
#     def __init__(self):
#         self.balance = 0
#         self.interest_rate = .1
        
#     def check_balance(self):
#     # returns the account balance
#         return self.balance
    
#     def deposit(self, amount):
#     # deposits the given amount
#         self.balance += amount
        
#     def check_withdrawal(self, amount):
#     # returns true if the withdrawn amount wont put the account in the negative
#         if self.balance > amount:
#             return True
        
#     def withdraw(self, amount):
#     #withdraws the amount from the account and returns it
#         self.balance = self.balance - amount
        
#     def calc_interest(self):
#     #returns the amount of interest calculated on the account
#         return self.balance * self.interest_rate

#version 3
class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = .1
        self.transactions = []
        
    def check_balance(self):
    # returns the account balance
        return self.balance
        
    def deposit(self, amount):
    # deposits the given amount
        self.transactions.append(f'User deposited ${amount}')
        self.balance += amount
        
    def check_withdrawal(self, amount):
    # returns true if the withdrawn amount wont put the account in the negative
        if self.balance > amount:
            return True
        
    def withdraw(self, amount):
    #withdraws the amount from the account and returns it
        self.transactions.append(f'User withdrew ${amount}')
        self.balance = self.balance - amount
        
    def calc_interest(self):
    #returns the amount of interest calculated on the account
        return self.balance * self.interest_rate
        
    def print_transaction(self):
    #print user transactions
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
    elif command == 'history':
        history = atm.print_transaction()
        print(history)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - transaction history')
        print('exit - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
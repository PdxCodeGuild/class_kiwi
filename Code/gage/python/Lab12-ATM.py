'''


VERSION 1


class ATM():
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    def check_balance(self): # returns the account balance
        return self.balance
    def deposit(self, amount): # deposits the given amount in the account
        self.balance = self.balance + amount
        return amount
    def check_withdrawal(self, amount): # returns true if the withdrawn amount won't put the account in the negative
        if self.balance - amount > 0:
            return True
        else:
            return False
    def withdraw(self, amount): # withdraws the amount from the account and returns it
        self.balance = self.balance - amount
        return amount
    def calc_interest(self): # returns the amount of interest calculated on the account
        accumulated = self.balance * self.interest - self.balance
        return accumulated
    

atm = ATM(0, 1.01) # create an instance of our class
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
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

        '''





'''


VERSION 2

class ATM():
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    def check_balance(self): # returns the account balance
        return self.balance
    def deposit(self, amount): # deposits the given amount in the account
        self.balance = self.balance + amount
        return amount
    def check_withdrawal(self, amount): # returns true if the withdrawn amount won't put the account in the negative
        if self.balance - amount > 0:
            return True
        else:
            return False
    def withdraw(self, amount): # withdraws the amount from the account and returns it
        self.balance = self.balance - amount
        return amount
    def calc_interest(self): # returns the amount of interest calculated on the account
        accumulated = self.balance * self.interest - self.balance
        return accumulated
    def print_transactions(self, history):
        all_transactions = ""
        for trans in history:
            all_transactions += trans + ", "
        return all_transactions
    

atm = ATM(0, 1.01) # create an instance of our class
print('Welcome to the ATM')
history = []
while True:
    
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        history.append(f"User deposited ${amount}")
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            history.append(f"User withdrew ${amount}")
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'statement':
        statement = atm.print_transactions(history)
        print(f"BANK STATEMENT: {statement}")
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

'''
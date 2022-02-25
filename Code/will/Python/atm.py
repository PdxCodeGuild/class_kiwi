class ATM():

#   initialize atm class
    def __init__(self, balance=0, interest=0.1, transactions=[]):
        self.balance = balance
        self.interest = interest
        self.transactions = transactions
#   define balance checking
    def check_balance(self):
        balance = self.balance
        return balance

#   define depositing money
    def deposit(self, amount):
        self.balance += amount

#   define checking for an overdraft
    def check_withdrawal(self, amount):
        if self.balance - amount > 0:
            return True
        else:
            return False

#   define withdrawing money
    def withdraw(self, amount):
        self.balance -= amount
        return amount

#   define calculating the interest of the account
    def calc_interest(self):
        interest = self.balance * self.interest
        return interest
#   define appending a transaction to a list
    def append_transaction(self, string):
        self.transactions.append(string)

#   define printing a transaction list
    def print_transactions(self):
        transaction_history = self.transactions
        return transaction_history




atm = ATM()
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        atm.append_transaction(f'User deposited ${amount}')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            atm.append_transaction(f'User withdrew ${amount}')
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        transaction_history = atm.print_transactions()
        print(transaction_history)
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
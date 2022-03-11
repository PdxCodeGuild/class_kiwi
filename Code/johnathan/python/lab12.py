
# # Lab 12: ATM w/ Version 2

# Let's represent an ATM with a class containing two attributes: 
# a balance and an interest rate. A newly created account will default to a balance of 0 
# and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

 
class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.transactions = [] #Add a new method `print_transactions()` to your class for printing out the list of transactions, 

# - `check_balance()` returns the account balance
    def check_balance(self):
        account_balance = self.balance 
        return account_balance 
# - `deposit(amount)` deposits the given amount in the account
    def deposit(self, amount):
        self.transactions.append(f'User deposited ${amount}')
        self.balance = self.balance + amount 
        return amount 
# - `check_withdrawal(amount)` returns true if the withdrawn amount won't 
# put the account in the negative    
    def check_withdrawal(self, amount):
        if amount < self.balance >= 0:
            return True 
        else: 
            return False
#withdraws the amount from the account and returns it  
    def withdraw(self, amount):
        self.transactions.append(f'User withdrew ${amount}')
        self.balance = self.balance - amount 
        return self.balance
#returns the amount of interest calculated on the account
    def calc_interest(self):
        amount = self.interest_rate * self.balance
        return amount
#print user transactions
    def user_transaction(self):
        return "\n".join(self.transactions)

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
        transactions = atm.user_transaction() # call the user_transactions() method
        print(transactions)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')






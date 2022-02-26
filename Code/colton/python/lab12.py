class ATM:
    """ATM"""
    def __init__(self, balance=0, interest=0.1):
        self.balance = balance
        self.interest = interest

    # Returns acount balance
    def check_balance(self):
        """Check balance"""
        amount = self.balance
        return amount
    
    # Deposits the given amount in the account
    def deposit(self, amount):
        """Deposit into balance"""
        self.balance += amount
        return 
    
    # Returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        """Check withdrawal to make sure it doesn't send account to a negative num"""
        if self.balance - amount >= 0:
            return True

    # Withdraws the amount from the account and returns it
    def withdraw(self, amount):
        """Withdraw from balance"""
        self.balance -= amount
        return
    
    # Returns the amount of interest calculated on the account
    def calc_interest(self):
        """Calculate accrued interest on balance"""
        return round((self.balance * self.interest), 2)
    
    # Returns transaction history
    def print_transactions(transactionlist):
        """Return history of transactions"""
        history = """
Total Transactions
------------------
"""
        for i in transactionlist:
            history += f"{i}\n"
        

        return history




transactionlist = []
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
        transactionlist.append(f'Deposited ${amount}')
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            transactionlist.append(f'Withdrew ${amount}')
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print out all transactions')
        print('exit     - exit the program')
    elif command == 'transactions':
        history = ATM.print_transactions(transactionlist) # call the print_transactions method.
        print(history)
    elif command == 'exit':
        break
    else:
        print('Command not recognized')

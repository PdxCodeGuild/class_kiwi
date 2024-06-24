

class ATM:
    def __init__(self, balance =0, interest=.001):
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
       
    def print_transactoins(self):
        return "\n".join(self.transactions)
        
        # Version 2
    
    
        
        
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
    elif command == 'print':
        transactions = atm.print_transactoins()
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
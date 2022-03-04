
class Atm:

    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    def check_balance(self, balance=0):
        return balance
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        return self.balance

    def check_withdrawal(self,amount):
        self.amount = self.amount
        self.balance = self.balance

        if self.balance >= self.amount:
            return True
        elif self.amount > self.balance:
            return False

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance =self.balance - self.amount

            return self.balance
    def calc_interest(self,interest=0.1):
        #Formula for intrest = Principal(deposit) * intrest(0.1)* time(1 for one year)
        gain = self.balance - 0 #Initial balance was zero
        self.interest = gain * 0.1 * 1

        return self.interest
    
    def print_transactions(self,amount):
        if self.amount == self.deposit(amount):
            return self.deposit(amount)
        elif self.amount == self.withdraw(amount):
            return self.withdraw(amount)
        elif self.balance == balance:
            return self.balance
    
atm = Atm(0, 0.1)

print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        balance = atm.balance # This returns additional check balances if withdraw or deposit occurs
        print(f'Your balance is ${atm.balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        
        print(f'Deposited ${amount} your new balance is {atm.balance}')
    elif command == 'withdraw':
        amount = float(input('How much would you like?: '))
        balance = atm.balance - amount
        # atm.balance = balance

        if atm.balance > amount:
            print(f"Withdrew ${amount}, your new balance is {balance}")
        else:
            print('Insufficient funds')
           
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${round(amount,2)} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions - last deposit/withdraw')
    elif command == 'transactions':
        user_transactions = input('What transaction would you like? deposit/withdraw? ')
        if user_transactions == 'deposit':
            atm.deposit(amount)
            atm.balance
            print(f"User deposited {atm.withdraw(amount)}")
        elif user_transactions == 'withdraw':
            atm.withdraw(amount)
            atm.balance
            print(f"User withdrew {amount} ")


    elif command == 'exit':
        break
    else:
        print('Command not recognized')
        
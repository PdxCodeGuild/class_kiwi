#version 1


class ATM:
    def __init__(self):
        self.balance = 0        #setting base vaules with init
        self.intrest = .001

    def check_balance(self):    #returning balance amount
        return self.balance

    def deposit(self, amount):     #adding amount passed int method to balance
        self.balance += amount

    def check_withdrawal(self, amount):    #if you try to withdraw an amount below 0 then returns false
        if self.balance - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):       #subtracts amount from balance
        self.balance = self.balance - amount
        return self.balance

    def calc_intrest(self):     #returns value of self.intrest times self.amount
        return (self.balance * self.intrest)


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
        amount = atm.calc_intrest() # call the calc_interest() method
        atm.deposit(amount)
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



#VERSION 2



class ATM():
    def __init__(self):
        self.balance = 0
        self.intrest = .001
        self.transactions = []   #added a list to append transactions to

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"User deposited ${amount}")    #appending to self.tranactions

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.transactions.append(f"User withdrew ${amount}")
        return self.balance

    def calc_intrest(self):
        return (self.balance * self.intrest)

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
        amount = atm.calc_intrest() # call the calc_interest() method
        atm.deposit(amount)
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
    elif command == "print transactions":
        transactions = atm.print_transactions()      #calling print transactions method
        for action in transactions:      #looping through each transaction and printing induvidualy 
            print(f"{action}\n")
    else:
        print('Command not recognized')
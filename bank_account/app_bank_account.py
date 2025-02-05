#def __init__(self,x,y,z): self.x = x   self.y = y  self.z = z
#@classmethod def
#@staticmethod def
#del nombre_instancia >> elimina una instancia
#magic methods: def __str__(self): >> devuelve como queremos ver un print a la clase o a una instancia de mi clase
#magic methods: def __len__(self): >> devuelve como queremos ver un len a la clase o a una instancia de mi clase
#magic methods: def __del__(self): >> devuelve como se le informa al usuario que se ha eliminado una instancia

import os
from random import *

class Person:
    """class that defines a person with its own name and surname"""
    def __init__(self, name, surname):
        self.name = name.capitalize()
        self.surname = surname.capitalize()

class Client(Person):
    """class that inherits all methods/attributes from class Person, it basically defines the client's information including
    name, surname, account number and balance and operations related to its account (deposit, withdraw, deletion)"""
    def __init__(self, name, surname, account_number, account_balance):
        super().__init__(name, surname)
        self.account_number = account_number
        self.account_balance = account_balance
    
    def __del__(self):
        return f'Client "{self.name} {self.surname}" has been deleted, account {self.account_number} is not active any longer'
    
    def __str__(self):
        return f'Client s name is "{self.name} {self.surname}", bank account number and balance:\n{self.account_number}\n{self.account_balance}'
    
    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self,amount):
        self.account_balance -= amount

class CurrentNumberAvailable:
    """class that shares current number of account available for a fresh user"""
    begin_account = 100000

    @classmethod
    def new_customer(cls):
        cls.begin_account += 1

def create_client():
    """function that creates a client in our system"""

    name = str(input('Enter your name: ')).lower().capitalize()
    surname = str(input('Enter your surname: ')).lower().capitalize()
    CurrentNumberAvailable.new_customer()
    account_number = CurrentNumberAvailable.begin_account
    print(f'Your account number is {account_number}')
    account_balance = 0
    while type(account_balance) != type(float()):
        try:
            account_balance = float(input('How much do you want to desposit? '))
        except: print('Insert a valid amount please')
    return Client(name,surname,account_number,account_balance)

def process(customer):
    """Function that operates the bank account process including deposit and withdraw"""
    election_num = 0

    print(f'Good day {customer.name} {customer.surname}')
    while election_num != 'E':
        try:
            print('#D# Deposit\n#W# Withdraw\n#E# End')
            election_num = str(input('Select (d,w,e): ')).upper()
            os.system('cls')

            if election_num not in ('D','W','E'):
                print('You have not selected a valid process, please try again')
            elif election_num == 'D':
                amount = float(input('Insert an amount to add to your account: '))
                customer.deposit(amount)
                print(f'ACCOUNT = {customer.account_balance}')
            elif election_num == 'W':
                amount = float(input('Insert an amount to get from your account: '))
                if amount > customer.account_balance:
                    print('You do not have enough capital available to substract that amount')
                else:
                    customer.withdraw(amount)
                    print(f'ACCOUNT = {customer.account_balance}')
            else:
                print('Thank you for your time, have a nice day')
        except:
            ValueError
            print('You have not inserted a valid number, please try again')

###start process from creation
client_os = create_client()
process(client_os)

client_pt = create_client()
process(client_pt)
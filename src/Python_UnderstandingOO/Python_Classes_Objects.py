# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:01:34 2024

@author: PACHECO
"""

class Account:
    #pass # placeholder, there is no code
    
    #Constructor
    def __init__(self, number, holder, balance, agency, limit):
        print("Creating bank account...")
        self._number = number #an underscore before the variable, it is declared as a private attribute
        self._holder = holder
        self._balance = balance
        self._agency = agency
        self._limit = limit
    
    def withdraw(self, value):
        self._balance -= value
        
    def deposit(self, value):
        self._balance += value

    def extract(self):
        print(f'The balance of the account of {self._holder} is: {self._balance}')
    
    #Encapsulation
    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)
        
account_1 = Account(123, 'Eduardo', 55.0, '001', 1000.0)
account_2 = Account(123, 'Jesus', 100, '002', 1000.0)

account_1._balance = 5000
account_1.extract()
print("\n")


#Encapsulation
value = 100

account_1.extract()
account_1.withdraw(value)
account_1.extract()
account_2.extract()
account_2.deposit(value)
account_2.extract()
print("\n")

account_1 = Account(123, 'Eduardo', 500.0, '001', 1000.0)
account_2 = Account(123, 'Jesus', 50, '002', 1000.0)

account_1.transfer(100.0, account_2)
account_1.extract()
account_2.extract()


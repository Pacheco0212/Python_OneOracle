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
        self.number = number
        self.holder = holder
        self.balance = balance
        self.agency = agency
        self.limit = limit
    
    def withdraw(self, value):
        self.balance -= value
        
    def deposit(self, value):
        self.balance += value

    def extract(self):
        print(f'The balance of the account of {self.holder} is: {self.balance}')
        
account_1 = Account(123, 'Eduardo', 55.0, '001', 1000.0)

account_1.deposit(700)
account_1.withdraw(40)
account_1.extract()
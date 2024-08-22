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
        self.__number = number #two underscore before the variable, it is declared as a private attribute
        self.__holder = holder
        self.__balance = balance
        self.__agency = agency
        self.__limit = limit
    
    def withdraw(self, value):
        self.__balance -= value
        
    def deposit(self, value):
        self.__balance += value

    def extract(self):
        print(f'The balance of the account of {self.__holder} is: {self.__balance}')
    
    #Encapsulation
    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)
        
    def get_balance(self):
        return self.__balance
    
    def get_holder(self):
        return self.__holder
    
    def set_limit(self, limit):
        self.__limit = limit
        return self.__limit
        
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
print("\n")

#Properties
print(f"{account_1.get_balance()}\n")

class Client:
    def __init__(self, name):
        self.__name = name
     
    @property
    def name(self):
        return self.__name.title()
    
    @name.setter
    def name(self, name):
        self.__name = name
    
client = Client("eduardo")
print(client.name)

client.name = "daniela"
print(client.name)

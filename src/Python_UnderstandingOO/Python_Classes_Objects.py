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
        
    def __canWithdraw(self, withdrawValue): #declaring a private method
        availableValue = self.__balance + self.__limit
        return withdrawValue >= availableValue
    
    def withdraw(self, value):
        if(self.__canWithdraw(value)):
            self.__balance -= value
        else:
            print(f"El valor {value} excedió el límite permitido")
        
    def deposit(self, value):
        self.__balance += value

    def extract(self):
        print(f'The balance of the account of {self.__holder} is: {self.__balance}')
    
    #Encapsulation
    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def holder(self):
        return self.__holder
    
    @staticmethod
    def bankCode():
        return '1001'
    
    @staticmethod
    def bankCodes():
        return {'BR':'1001','Santander':'1002','Itau':'1003'}
    
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

account_1 = Account(123, 'Eduardo', 500.0, '001', 1000.0)
account_2 = Account(123, 'Jesus', 50, '002', 1000.0)

account_1.transfer(100.0, account_2)
account_1.extract()
account_2.extract()
print("\n")

#Properties
print(f"{account_1.balance}\n")

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
print("\n\n")

#Private and statics methods 
account_1 = Account(123, 'Eduardo', 500.0, '001', 1000.0)
account_2 = Account(123, 'Jesus', 50, '002', 1000.0)

account_1.withdraw(1000)

print(f"\n{Account.bankCode()}")
codes = Account.bankCodes()
print(f"\n{codes['Santander']}")
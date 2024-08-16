# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:03:48 2024

@author: PACHECO
"""

number = 123
holder = 'Eduardo'
balance = 55.0
limit = 1000.0


def account(number, holder, balance, limit):
    #dictionary struture
    account = {'number': number,
            'holder' : holder,
            'balance' : balance,
            'limit' : limit}
    
    return account

account_1 = {'number': 123,
        'holder' : 'Eduardo',
        'balance' : 55.0,
        'limit' : 1000.0}

def withdraw(account, value):
    account['balance'] -= value
    
def deposit(account, value):
    account['balance'] += value

def extract(account):
    print(f'The balance of the account is {account["holder"]} es: {account["balance"]}')
         
          
withdraw(account_1, 20)
extract(account_1)
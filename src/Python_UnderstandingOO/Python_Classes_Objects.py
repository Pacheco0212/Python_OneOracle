# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:01:34 2024

@author: PACHECO
"""

class Account:
    #pass # placeholder, there is no code
    
    #Constructor
    def __init__(self, number, holder, balance, agency, limit):
        print("Creando una cuenta bancaria...")
        self.number = number
        self.holder = holder
        self.balance = balance
        self.agency = agency
        self.limit = limit
        
account_1 = Account(123, 'Eduardo', 55.0, '001', 1000.0)
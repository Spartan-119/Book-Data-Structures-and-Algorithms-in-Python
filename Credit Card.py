# -*- coding: utf-8 -*-
"""
READ TILL PAGE 71 (93 OF 770)

Created on Mon Aug 29 03:58:31 2022

@author: Abin
"""

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        
        # setting the private data attributes
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        
        # the initial balance being 0
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    # creating a method to return charge
    def charge(self, price):
        '''
        Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed,
        else return False if charge was denied.
        '''
        
        if price + self._balance > self._limit:
            
            # if charge would exceed the limit, cannot accept
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        '''
        Process customer payment that reduces balance.
        '''
        self._balance -= amount
        
cc = CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 1000)

# Testing the class
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))
        
    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)
    
    for c in range(3):
        print('Customer Name:', wallet[c].get_customer())
        print('Bank:', wallet[c].get_bank())
        print('Account:', wallet[c].get_account())
        print('Limit:', wallet[c].get_limit())
        print('Balance:', wallet[c].get_balance())
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            # printing the updated balance
            print('New Balance:', wallet[c].get_balance())
        
        print()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
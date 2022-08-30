# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:08:48 2022

@author: Abin
"""

import warnings
warnings.filterwarnings("ignore", message="Reloaded modules: <module_name>")

from Credit_Card import CreditCard

# Inherting the CreditCard class
class PredatoryCreditCard(CreditCard):
    
    '''
    The new constructor will have an additional new parameter,
    Annual Percentage Rate (APR).
    The body of our new constructor relies upon
    making a call to the inherited constructor to perform most of the initialization (in
    fact, everything other than the recording of the percentage rate).
    '''
    
    def __init__(self, customer, bank, account, limit, apr):
        '''
        Creating a predatory credit card instance.
        
        The initial balance being 0.
        
        All the attributes being the same with an additional parameter being -->
        APR: Annual Percentage Rate (0.0825 for 8.25% APR)
        '''
        super.__init__(customer, bank, account, limit)  # Calling the super constructor
        self._apr = apr
    
    # OVERRIDING the charge method from the Parent class
    def charge(self, price):
        '''
        Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed,
        else return False and assess an extra $5 fee is charge is denied.
        '''
        success = super().charge(price)     # Calling the inherited method.
        if not success:
            self._balance += 5              # assess penalty
        return success                      # caller expects some return
    
    def process_month(self):
        '''
        Assess monthly interest on outstanding balance.
        '''
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor.
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

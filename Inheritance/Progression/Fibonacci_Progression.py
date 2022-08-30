# -*- coding: utf-8 -*-
"""
Extending the Progression class to make the Fibonacci Progression

@author: Abin
"""

from Progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        '''
        Creating a new Fibonacci Progression.
        '''
        super.__init__(first)           # initializing the first value
        self._prev = second - first
        
    def _advance(self):                 # Override the inherited method
        '''
        Update the current value by taking the sum of previous two.
        '''
        self._prev, self._current = self._current, self._prev + self._current
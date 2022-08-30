# -*- coding: utf-8 -*-
"""
Extending the Progression class to make the Arithmetic Progression

@author: Abin
"""

from Progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, start = 0, increment = 1):
        '''
        Creating a new Arithmetic Progression.
        '''
        super().__init__(start)           # initializing the base
        self._increment = increment
        
    def _advance(self):                 # Override the inherited method
        '''
        Update the current value by adding the fixed increment.
        '''
        self._current += self._increment
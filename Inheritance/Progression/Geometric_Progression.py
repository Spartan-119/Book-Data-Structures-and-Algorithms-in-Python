# -*- coding: utf-8 -*-
"""
Extending the Progression class to make the Geometric Progression

@author: Abin
"""

from Progression import Progression

class GeometricProgression(Progression):
    def __init__(self, start = 1, factor = 2):
        '''
        Creating a new Arithmetic Progression.
        '''
        super.__init__(start)           # initializing the first value
        self._factor = factor
        
    def _advance(self):                 # Override the inherited method
        '''
        Update the current value by adding the fixed increment.
        '''
        self._current *= self._factor
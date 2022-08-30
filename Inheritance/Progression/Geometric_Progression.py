# -*- coding: utf-8 -*-
"""
Extending the Progression class to make the Geometric Progression

@author: Abin
"""

from Progression import Progression

class GeometricProgression(Progression):
    def __init__(self, start = 1, factor = 2):
        '''
        Creating a new Geometric Progression.
        '''
        super.__init__(start)           # initializing the first value
        self._factor = factor
        
    def _advance(self):                 # Override the inherited method
        '''
        Update the current value by multiplying it by the factor value.
        '''
        self._current *= self._factor
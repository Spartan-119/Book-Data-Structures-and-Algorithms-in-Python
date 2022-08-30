# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 12:49:13 2022

@author: Abin
"""

class Progression:
    '''
    Class for generic progression.
    '''
    def __init__(self, start = 0):
        # initialize the current value to the start of the progression
        self._current = start
        
    def _advance(self):
        '''
        Update self._current to a new value.
        If current is set to None, this means the end of a finite progression.
        '''
        self._current += 1
        
    def __next__(self):
        '''
        Return the next element, or else raise the StopIteration error.
        '''
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current          # return current value to return
            self._advance()                 # advance to prepare for the next time
            return answer                   # return the answer
        
    def __iter__(self):
        # by convention the iter must return itself
        return self
    
    def print_progression(self, n):
        # Print the next n values of the progression
        print(' '.join(str(next(self)) for j in range(n)))
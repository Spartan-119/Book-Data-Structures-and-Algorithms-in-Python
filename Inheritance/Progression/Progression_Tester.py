# -*- coding: utf-8 -*-
"""
The Main Tester class

@author: Abin
"""

from Progression import Progression
from Arithmetic_Progression import ArithmeticProgression
from Geometric_Progression import GeometricProgression
from Fibonacci_Progression import FibonacciProgression

if __name__ == '__main__':
    print('Default Progression:')
    Progression().print_progression(10)
    print()
    
    print('Arithmetic Progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)
    print()
    
    print('Arithmetic Progression with start 2 and increment 5:')
    ArithmeticProgression(2, 5).print_progression(10)
    print()
    
    print('Geometric Progression with default factor:')
    GeometricProgression().print_progression(10)
    print()
    
    print('Geometric Progression with the factor 3:')
    GeometricProgression(3).print_progression(10)
    print()
    
    print('Fibonacci Progression with default start values:')
    FibonacciProgression().print_progression(10)
    print()
    
    print('Fibonacci Progression with default start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
        
    '''
    Output:
        Default Progression:
        0 1 2 3 4 5 6 7 8 9

        Arithmetic Progression with increment 5:
        5 6 7 8 9 10 11 12 13 14

        Arithmetic Progression with start 2 and increment 5:
        2 7 12 17 22 27 32 37 42 47

        Geometric Progression with default factor:
        1 2 4 8 16 32 64 128 256 512

        Geometric Progression with the factor 3:
        3 6 12 24 48 96 192 384 768 1536

        Fibonacci Progression with default start values:
        0 1 1 2 3 5 8 13 21 34

        Fibonacci Progression with default start values 4 and 6:
        4 6 10 16 26 42 68 110 178 288
    '''
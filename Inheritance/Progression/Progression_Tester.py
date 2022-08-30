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
    
    print('Arithmetic Progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)
    
    print('Arithmetic Progression with start 2 and increment 5:')
    ArithmeticProgression(2, 5).print_progression(10)
    
    print('Geometric Progression with default factor:')
    GeometricProgression().print_progression(10)
    
    print('Geometric Progression with the factor 3:')
    GeometricProgression(3).print_progression(10)
    
    print('Fibonacci Progression with default start values:')
    FibonacciProgression().print_progression(10)
    
    print('Fibonacci Progression with default start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
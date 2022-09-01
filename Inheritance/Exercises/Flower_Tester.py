# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:04:38 2022

@author: Abin
"""

from Flower import Flower

if __name__ == '__main__':
    f1 = Flower()
    
    f1.set_name('Iris Virginica')
    f1.set_petals(4)
    f1.set_price(30)
    
    print(f1.get_name())
    print(f1.get_petals())
    print(f1.get_price())
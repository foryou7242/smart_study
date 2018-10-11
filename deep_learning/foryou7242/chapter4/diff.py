#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:39:51 2018

@author: son
"""

def function_1(x):
    return 0.01*x**2 + 0.1*x
def function_2(x):
    return np.sum(x**2)

import numpy as np

import matplotlib.pylab as plt

from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    
    x = np.arange(0.0, 20, 0.01)
    x1 = np.arange(0.0, 20, 0.01)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x,y)
    plt.show()
    
    
    import numerical_diff as nd
    #0.2 0.3
    print(nd.numerical_diff(function_1, 5))
    print(nd.numerical_diff(function_1, 10))
    
    print(nd.origin_numerical_diff(function_1, 5))
    print(nd.origin_numerical_diff(function_1, 10))
    
    
    
    y = nd.numerical_diff(function_1, x)
    plt.plot(x,y)
    plt.show()
    y = nd.origin_numerical_diff(function_1, x)
    plt.plot(x,y)
    plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:37:19 2018

@author: son
"""

import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return ((f(x+h) - f(x-h))/ (2*h))
def origin_numerical_diff(f, x):
    h = 1e-4
    return ((f(x+h) - f(x))/ (h))

def numerical_gradient(f,x):
    h=1e-4
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        
        idx = it.multi_index

        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        it.iternext()   
    return grad
    
def gradient_descent(f, init_x, lr=0.1, step_num= 100):
    x= init_x
    x_his = []
#    print(x_his.shape)
    for i in range(step_num):
        
        grad = numerical_gradient(f,x)
        x -=lr* grad
       # print(x)
        x_his.append(x.copy())
    x_ = np.array(x_his)
    '''
    plt.figure()    
    plt.plot(x_[:,0], x_[:,1], 'o')#,headwidth=10,scale=40,color="#444444")
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.legend()
    plt.draw()
    plt.show()
    '''
    return x
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:08:14 2018

@author: son
"""

import numpy as np

import matplotlib.pylab as plt


import numerical_diff as nd
import diff

init_x = np.array([-3.0,4.0])
a = nd.gradient_descent(diff.function_2, init_x = init_x, lr = 0.1)
print(a)
#print(nd.numerical_gradient(diff.function_2, np.array([3.0,4.0])))
'''
x0 = np.arange(-2, 2.5, 0.25)
x1 = np.arange(-2, 2.5, 0.25)
X, Y = np.meshgrid(x0, x1)

X = X.flatten()
Y = Y.flatten()

tx = np.array([X, Y])

grad = nd.numerical_gradient(diff.function_2, tx )
    
plt.figure()
plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#444444")#,headwidth=10,scale=40,color="#444444")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x0')
plt.ylabel('x1')
plt.grid()
plt.legend()
plt.draw()
plt.show()
'''
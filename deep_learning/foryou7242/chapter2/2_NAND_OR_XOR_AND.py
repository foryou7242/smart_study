# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def AND(x1, x2) :
    x=np.array([x1, x2])
    w= np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0;
    else:
        return 1;
    
    
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    x = np.array([x1, x2])
    x1_ = NAND(x1, x2)
    x2_ = OR(x1, x2)
    return AND(x1_, x2_)
    
    


for i in range(0,2):
    for j in range(0,2):
        print("x {} y {} AND is {}" .format(i , j, AND(i,j)))
for i in range(0,2):
    for j in range(0,2):
        print("x {} y {} NAND is {}" .format(i ,j, NAND(i,j)))
for i in range(0,2):
    for j in range(0,2):
        print("x {} y {} OR is {}" .format (i ,j, OR(i,j)))
for i in range(0,2):
    for j in range(0,2):
        print("x {} y {} XOR is {}" .format (i ,j, XOR(i,j)))
        
        
        

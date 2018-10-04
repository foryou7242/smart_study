#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:40:03 2018

@author: son
"""

import numpy as np
'''
t = [0  ,1  ,0  ,0,0  ,0  ,0,0,0  ,0  ]
y = [0.1,0.9,0.0,0,0.0,0.0,0,0,0.0,0.0]
'''

def MSE(y,t ):
    return np.sum((y-t)**2) * 0.5


def CEE(y, t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    
    return np.sum(t*np.log(y + 0.0001)) * -1/ batch_size
#print(CEE(np.array(y), np.array(t)))





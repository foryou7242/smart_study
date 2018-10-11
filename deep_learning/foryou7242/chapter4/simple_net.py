#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 19:48:38 2018

@author: son
"""

# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from functions import softmax
import lossFunction as lf
import numerical_diff as nd


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        z = np.dot(x, self.W)
        y = softmax(z)
        return y
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = lf.CEE(y, t)
        return loss

def f(W):
    #print(id(x))
    return net.loss(x, t)


x = np.array([0.6, 0.9])
print(id(x))
t = np.array([0, 0, 1])

net = simpleNet()

p = net.predict(x)
print(np.argmax(p))
print(p)
t = np.array([0,0,1])
err = net.loss(x,t)
print(err)


'''
f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print(dW)
'''
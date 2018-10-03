#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:27:31 2018

@author: sungyunlee
"""

import numpy as np

A = np.array([[1,2], [3,4], [5,6]])
print(A)
print(np.ndim(A))
print(A.shape)


A = np.array([[1,2], [3,4]])
print(A.shape)
B = np.array([[5,6], [7,8]])
print(B.shape)
print(np.dot(A, B))

A = np.array([[1,2,3], [4,5,6]])
print(A.shape)
B = np.array([[1,2], [3,4], [5,6]])
print(B.shape)
print(np.dot(A, B))

C = np.array([[1,2], [3,4]])
print(C.shape)
print(A.shape)
print(np.dot(A, C))

A = np.array([[1,2], [3,4], [5,6]])
print(A.shape)
B = np.array([7,8])
print(B.shape)
print(np.dot(A, B))


X = np.array([1,2])
print(X.shape)
W = np.array([[1,3,5], [2,4,6]])
print(W.shape)
Y = np.dot(A, B)
print(Y)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:34:17 2018

@author: son
"""

import sys, os

import lossFunction as lf


#sys.path.append(os.pardir)

import numpy as np

from mnist import load_mnist
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

choice = np.random.choice(60000,10)
print(choice)
print(x_train.shape)
print(t_train.shape)
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print(x_batch)
print(t_batch)

print(lf.CEE(x_batch, t_batch))
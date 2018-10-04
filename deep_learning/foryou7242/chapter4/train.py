#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:45:39 2018

@author: son
"""

import numpy as np
from mnist import load_mnist
import matplotlib.pylab as plt
from two_layer import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []
iters_num = 100
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
i_his = []
network = TwoLayerNet(784,50,10)
for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print('start')
    grad = network.numerical_gradient(x_batch, t_batch)
    print('end')
    for key in ('W1', 'b1' ,'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
        
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    i_his.append(i)
    plt.figure()
    plt.xlim([0, 100])
    plt.ylim([0, 3])
    plt.xlabel('x')
    plt.ylabel('loss')
    plt.plot(i_his,train_loss_list)
    plt.grid()
    plt.legend()
    plt.show()
    
    

print(train_loss_list)
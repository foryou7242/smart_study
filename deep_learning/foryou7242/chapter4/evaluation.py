#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:23:28 2018

@author: son
"""

import numpy as np
from mnist import load_mnist
import matplotlib.pylab as plt
from two_layer import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []
train_acc_list = []
test_acc_list =[]

iters_num = 6000
train_size = x_train.shape[0]
batch_size = 100
iter_per_epoch = max(train_size/batch_size, 1)



learning_rate = 0.1
i_his = []
network = TwoLayerNet(784,50,10)
for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    #print('start')
    a = network.predict(x_batch)
    grad = network.numerical_gradient(x_batch, t_batch)
    #print('end')
    for key in ('W1', 'b1' ,'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    loss = network.loss(x_batch, t_batch)
    
    train_loss_list.append(loss)
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        print((test_acc, train_acc))
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        i_his.append(i)        
        plt.figure()
        plt.xlim([0, 1000])
        plt.ylim([0, 3])
        plt.xlabel('x')     
        plt.ylabel('loss')
        plt.plot(i_his,train_acc_list)
        plt.plot(i_his,test_acc_list)
        plt.grid()
        plt.legend()
        plt.show()
    
    
    

#print(train_loss_list)
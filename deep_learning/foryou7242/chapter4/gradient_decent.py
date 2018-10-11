#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:33:15 2018

@author: son
"""

import numerical_diff as nd
import diff as d
import numpy as np
x = np.array([3.0,4.0])
a = nd.gradient_descent(d.function_2,init_x = x, step_num = 40, lr= 0.9)
print(a)
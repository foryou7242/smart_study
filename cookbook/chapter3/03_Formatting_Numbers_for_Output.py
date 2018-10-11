#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:35:55 2018

@author: sungyunlee
"""

'''
Problem
You need to format a number for output, 
controlling the number of digits, alignment, 
inclusion of a thousands separator, and other details.
'''

# To format a single number for output, use the built-in format() function. 

x = 1234.56789

# Two decimal places of accuracy
print(format(x, '0.2f'))

# Right justified in 10 chars, one-digit accuracy
print(format(x, '>10.1f'))

# Left justified
print(format(x, '<10.1f'))

# Centered
print(format(x, '^10.1f'))

# Inclusion of thousands separator
print(format(x, ','))
print(format(x, '0,.1f'))

# If you want to use exponential notation, change the f to an e or E, 
# depending on the case you want used for the exponential specifier. 

print(format(x, 'e'))
print(format(x, '0.2E'))

# The general form of the width and precision in both cases is '[<>^]?width[,]?(.dig its)?' 
# where width and digits are integers and ? signifies optional parts. 
# The same format codes are also used in the .format() method of strings.

print('The value is {:0,.2f}'.format(x))

# Formatting numbers for output is usually straightforward. 
# The technique shown works for both floating-point numbers and Decimal numbers 
# in the decimal module.

# When the number of digits is restricted, values are rounded away according 
# to the same rules of the round() function.
print(x)
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

# Formatting of values with a thousands separator is not locale aware. 
# If you need to take that into account, you might investigate functions 
# in the locale module. You can also swap separator characters 
# using the translate() method of strings. 

swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

# In a lot of Python code, numbers are formatted using the % operator. 
print('%0.2f' % x)
print('%10.1f' % x)
print('%-10.1f' % x)

# This formatting is still acceptable, but less powerful than 
# the more modern format() method. For example, some features 
# (e.g., adding thousands separators) aren’t sup‐ ported when using the % operator 
# to format numbers.
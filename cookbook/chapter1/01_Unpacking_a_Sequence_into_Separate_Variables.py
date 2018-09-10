#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:38:18 2018

@author: sungyunlee
"""
# Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
p = (4, 5)
x, y = p
print(x, y)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name, shares, price, date)

# The only requirement is that the number of variables and structure match the sequence.
name, shares, price, (year, mon, day) = data

# If there is a mismatch in the number of elements, you’ll get an error.
p = (4, 5)
x, y, z = p

# Unpacking actually works with any object that happens to be iterable, 
# not just tuples or lists. This includes strings, files, iterators, and generators. 

s = 'Hello'
a, b, c, d, e = s
print(a,b,c,d,e)

# When unpacking, you may sometimes want to discard certain values. 
# Python has no special syntax for this, 
# but you can often just pick a throwaway variable name for it

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares, price)
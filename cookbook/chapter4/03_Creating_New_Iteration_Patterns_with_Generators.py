#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:03:19 2018

@author: sungyunlee
"""

'''
Problem
You want to implement a custom iteration pattern that’s different than 
the usual built- in functions (e.g., range(), reversed(), etc.).
'''

'''
If you want to implement a new kind of iteration pattern, define it using 
a generator function. 
Here’s a generator that produces a range of floating-point numbers:
'''
def frange(start, stop, increment): 
    x = start
    while x < stop: 
        yield x
        x += increment
        
'''
To use such a function, you iterate over it using a for loop or use it with some other
function that consumes an iterable (e.g., sum(), list(), etc.). 
'''

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))

'''
The mere presence of the yield statement in a function turns it into a generator.
Unlike a normal function, a generator only runs in response to iteration. 
Here’s an experiment you can try to see the underlying mechanics of 
how such a function works
'''

def countdown(n):
    print('Starting to count from', n) 
    while n > 0:
        yield n
        n -= 1 
    print('Done!')
        
# Create the generator, notice no output appears
c = countdown(3)
print(c)

# Run to first yield and emit a value
print(next(c))
# Run to the next yield
print(next(c))
# Run to next yield
print(next(c))
# Run to next yield (iteration stops)
print(next(c))

'''
The key feature is that a generator function only runs in response to “next” operations 
carried out in iteration. Once a generator function returns, iteration stops. 
However, the for statement that’s usually used to iterate takes care of these details, 
so you don’t normally need to worry about them.
'''
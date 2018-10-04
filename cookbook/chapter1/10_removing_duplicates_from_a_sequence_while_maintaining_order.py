#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:30:13 2018

@author: son
"""

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)



a = [1,2,3,6,6,12,2,1,23]
#a = 5
b = list(dedupe(a))
print(b)


#dict
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

b = list(dedupe(a, lambda d: (d['x'],d['y'])))
with open('test.txt', "r") as f:
    for line in dedupe(f):
        print(f"line {line} b {b}")
        
#nameing a slice
        
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25   ..........'
cost = int(record[20:32]) * float(record[40:48])

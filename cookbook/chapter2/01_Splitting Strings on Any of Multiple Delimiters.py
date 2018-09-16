#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 21:39:27 2018

@author: sungyunlee
"""

'''
Problem
You need to split a string into fields, but the delimiters 
(and spacing around them) aren’t consistent throughout the string.
'''


# The split() method of string objects is really meant for very simple cases, 
# and does not allow for multiple delimiters or account for possible whitespace
# around the delim‐ iters
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
tmp = re.split(r'[;,\s]\s*', line)
print(tmp)


# When using re.split(), 
# you need to be a bit careful should the regular expression pattern involve 
# a capture group enclosed in parentheses. If capture groups are used, 
# then the matched text is also included in the result

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# Getting the split characters might be useful in certain contexts. For example,
# maybe you need the split characters later on to reform an output string:
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters
tmp = ''.join(v+d for v,d in zip(values, delimiters))
print(tmp)

# If you don’t want the separator characters in the result, but 
# still need to use parentheses to group parts of the regular expression pattern, 
# make sure you use a noncapture group

tmp = re.split(r'(?:,|;|\s)\s*', line)
print(tmp)

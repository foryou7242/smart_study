#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 23:41:35 2018

@author: sungyunlee
"""


'''
Problem
You need to check the start or end of a string for specific text patterns, 
such as filename extensions, URL schemes, and so on.
'''

# A simple way to check the beginning or 
# end of a string is to use the str.starts with() or str.endswith() methods. 

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))


# If you need to check against multiple choices, 
# simply provide a tuple of possibilities to startswith() or endswith():

import os
filenames = os.listdir('.')
print(filenames)
tmp = [name for name in filenames if name.endswith(('.py', '.ipynb')) ]
print(tmp)
tmp = any(name.endswith('.py') for name in filenames)
print(tmp)

from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read() 
    else:
        with open(name) as f: return f.read()
        
        
# If you happen to have the choices specified in a list or set, 
# just make sure you convert them using tuple() first       
        
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(choices)

# Similar operations can be performed with slices

filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

# You might also be inclined to use regular expressions as an alternative

import re
url = 'http://www.python.org'
tmp = re.match('http:|https:|ftp:', url)
print(tmp)
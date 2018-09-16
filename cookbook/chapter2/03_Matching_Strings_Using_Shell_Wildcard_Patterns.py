#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 00:19:53 2018

@author: sungyunlee
"""
'''
Problem
You want to match text using the same wildcard patterns 
as are commonly used when working in Unix shells 
(e.g., *.py, Dat[0-9]*.csv, etc.).
'''

# The fnmatch module provides two functions—fnmatch() and 
# fnmatchcase()—that can be used to perform such matching. 

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])


# fnmatch() matches patterns using the same case-sensitivity rules as 
# the sys‐ tem’s underlying filesystem (which varies based on operating system)

# On OS X (Mac)
print(fnmatch('foo.txt', '*.TXT'))
# On Windows
print(fnmatch('foo.txt', '*.TXT'))

# If this distinction matters, use fnmatchcase() instead. 
# It matches exactly based on the lower- and uppercase conventions that you supply:

print(fnmatchcase('foo.txt', '*.TXT'))

# An often overlooked feature of these functions is their potential use 
# with data processing of nonfilename strings
from fnmatch import fnmatchcase
addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
]
tmp1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(tmp1)
tmp2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(tmp2)
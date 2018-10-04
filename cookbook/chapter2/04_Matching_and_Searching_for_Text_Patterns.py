#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:01:55 2018

@author: sungyunlee
"""

'''
Problem
You want to match or search text for a specific pattern.
'''

# If the text you’re trying to match is a simple literal, 
# you can often just use the basic string methods, 
# such as str.find(), str.endswith(), str.startswith(), or similar. For example:

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

# suppose you want to match dates specified as digits, such as “11/27/2012.” 
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
    
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
    
# If you’re going to perform a lot of matches using the same pattern, 
# it usually pays to precompile the regular expression pattern 
# into a pattern object first.
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
    
if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() always tries to find the match at the start of a string. 
# If you want to search text for all occurrences of a pattern, 
# use the findall() method instead
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)

# When defining regular expressions, it is common to introduce capture groups 
# by en‐ closing parts of the pattern in parentheses.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# Capture groups often simplify subsequent processing of the matched text 
# because the contents of each group can be extracted individually. 
m = datepat.match('11/27/2012')
print(m)

# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month, day, year = m.groups()
# Find all matches (notice splitting into tuples)
print(text)
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# The findall() method searches the text and finds all matches, 
# returning them as a list. If you want to find matches iteratively, 
# use the finditer() method instead
for m in datepat.finditer(text):
    print(m.groups())

# r'(\d+)/(\d+)/(\d+)' '(\\d+)/(\\d+)/(\\d+)'.
# Be aware that the match() method only checks the beginning of a string. 
# It’s possible that it will match things you aren’t expecting
m = datepat.match('11/27/2012abcdef')
print(m)
print(m.group())

# If you want an exact match, make sure the pattern includes the end-marker ($)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')

# you can often skip the compilation step and 
# use module-level functions in the re module instead
re.findall(r'(\d+)/(\d+)/(\d+)', text)
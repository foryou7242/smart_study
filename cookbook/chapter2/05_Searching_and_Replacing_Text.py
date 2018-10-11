#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:37:59 2018

@author: sungyunlee
"""

'''
Problem
You want to search for and replace a text pattern in a string.
'''

# For simple literal patterns, use the str.replace() method.

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# For more complicated patterns, 
# use the sub() functions/methods in the re module. To illustrate, 
# suppose you want to rewrite dates of the form “11/27/2012” as “2012-11-27.”
# The first argument to sub() is the pattern to match and 
# the second argument is the replacement pattern. 
# Backslashed digits such as \3 refer to capture group numbers in the pattern.

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' 
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))



# If you’re going to perform repeated substitutions of the same pattern, 
# consider compil‐ ing it first for better performance.
import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

# For more complicated substitutions, 
# it’s possible to specify a substitution callback func‐tion instead. 
# As input, the argument to the substitution callback is a match object, 
# as returned by match() or find(). 
# Use the .group() method to extract specific parts of the match. 

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

# If you want to know how many substitutions were made 
# in addition to getting the replacement text, use re.subn() instead
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)
print(n)

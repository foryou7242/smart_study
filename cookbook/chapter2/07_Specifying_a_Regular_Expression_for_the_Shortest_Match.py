#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:16:23 2018

@author: sungyunlee
"""

'''
Problem
You’re trying to match a text pattern using regular expressions, 
but it is identifying the longest possible matches of a pattern. 
Instead, you would like to change it to find the shortest possible match.
'''

# This problem often arises in patterns that try to match text enclosed 
# inside a pair of starting and ending delimiters (e.g., a quoted string). 
import re
str_pat = re.compile(r'\"(.*)\"') 
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# the pattern r'\"(.*)\"' is attempting to match text enclosed inside quotes. 
# However, the * operator in a regular expression is greedy, 
# so matching is based on finding the longest possible match. 
# Thus, in the second example involving text2, 
# it incorrectly matches the two quoted strings.

# To fix this, add the ? modifier after the * operator in the pattern
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

# This makes the matching nongreedy, and produces the shortest match instead.

# This recipe addresses one of the more common problems encountered 
# when writing regular expressions involving the dot (.) character. 

# the dot matches any character except a newline.

# if you bracket the dot with starting and ending text (such as a quote), 
# matching will try to find the longest possible match to the pattern.
# This causes multiple occurrences of the starting or ending text 
# to be skipped altogether and included in the results of the longer match

# Adding the ? right after operators such as * or + forces 
# the matching algorithm to look for the shortest possible match instead
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:12:39 2018

@author: sungyunlee
"""

'''
Problem
You need to convert or output integers represented by binary, octal, or 
hexadecimal digits.
'''

# To convert an integer into a binary, octal, or hexadecimal text string, 
# use the bin(), oct(), or hex() functions, respectively

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# Alternatively, you can use the format() function 
# if you don’t want the 0b, 0o, or 0x prefixes to appear. 

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# Integers are signed, so if you are working with negative numbers, 
# the output will also include a sign. 

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

# If you need to produce an unsigned value instead, 
# you’ll need to add in the maximum value to set the bit length. 
# For example, to show a 32-bit value, use the following

x = -1234
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

# To convert integer strings in different bases, simply use the int() function
# with an appropriate base. 
print(int('4d2', 16))
print(int('10011010010', 2))

# For the most part, working with binary, octal, and hexadecimal integers 
# is straightfor‐ ward. Just remember that these conversions only pertain 
# to the conversion of integers to and from a textual representation. 
# Under the covers, there’s just one integer type.

# Finally, there is one caution for programmers who use octal. 
# The Python syntax for specifying octal values is slightly different than 
# many other languages. For example, if you try something like this, 
# you’ll get a syntax error

import os
os.chmod('script.py', 0755)

# Make sure you prefix the octal value with 0o, as shown here:
os.chmod('script.py', 0o755)



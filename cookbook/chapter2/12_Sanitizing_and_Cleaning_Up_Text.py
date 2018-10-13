#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:14:07 2018

@author: sungyunlee
"""

'''
Problem
Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page
 and you’d like to clean it up somehow.
'''

# The problem of sanitizing and cleaning up text applies to a wide variety of problems 
# involving text parsing and data handling. At a very simple level, 
# you might use basic string functions (e.g., str.upper() and str.lower()) 
# to convert text to a standard case. Simple replacements using str.replace() 
# or re.sub() can focus on removing or changing very specific character sequences. 
# You can also normalize text using unicode data.normalize()

# However, you might want to take the sanitation process a step further. Perhaps, 
# for example, you want to eliminate whole ranges of characters or 
# strip diacritical marks. To do so, you can turn to the often overlooked 
# str.translate() method

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# The first step is to clean up the whitespace. To do this, 
# make a small translation table and use translate()

remap = { 
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None 
        }
a = s.translate(remap)
print(a) # Deleted

# As you can see here, whitespace characters such as \t and \f have been remapped 
# to a single space. The carriage return \r has been deleted entirely.
# You can take this remapping idea a step further and build much bigger tables. 

import unicodedata
import sys
cmb_chrs = dict.fromkeys(
        c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# In this last example, a dictionary mapping every Unicode combining character
# to None is created using the dict.fromkeys().

# The original input is then normalized into a decomposed form using 
# unicodedata.normalize(). From there, the translate function is used to delete
# all of the accents. Similar techniques can be used to remove other kinds of 
# characters (e.g., control characters, etc.).

# As another example, here is a translation table that maps 
# all Unicode decimal digit characters to their equivalent in ASCII:

digitmap = { 
        c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode)
        if unicodedata.category(chr(c)) == 'Nd'
        }
print(len(digitmap))
# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


# Yet another technique for cleaning up text involves I/O decoding and encoding 
# func‐ tions. The idea here is to first do some preliminary cleanup of the text, 
# and then run it through a combination of encode() or decode() operations 
# to strip or alter it.
print(b)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

# Here the normalization process decomposed the original text into characters 
# along with separate combining characters. The subsequent ASCII encoding/decoding 
# simply dis‐ carded all of those characters in one fell swoop. Naturally, 
# this would only work if getting an ASCII representation was the final goal.

# A major issue with sanitizing text can be runtime performance. As a general rule, 
# the simpler it is, the faster it will run. For simple replacements, 
# the str.replace() method is often the fastest approach—even 
# if you have to call it multiple times. For instance, to clean up whitespace,

def clean_spaces(s):
    s = s.replace('\r', '') 
    s = s.replace('\t', ' ') 
    s = s.replace('\f', ' ') 
    return s

# If you try it, you’ll find that it’s quite a bit faster than using translate() 
# or an approach using a regular expression.
    
# On the other hand, the translate() method is very fast if you need to perform 
# any kind of nontrivial character-to-character remapping or deletion.
    
# In the big picture, performance is something you will have to study further 
# in your particular application. Unfortunately, it’s impossible to suggest 
# one specific technique that works best for all cases, so try different approaches 
# and measure it.
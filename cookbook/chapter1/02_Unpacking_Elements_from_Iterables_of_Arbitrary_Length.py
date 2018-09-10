#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 23:41:23 2018

@author: sungyunlee
"""

'''
Probelm
You need to unpack N elements from an iterable, 
but the iterable may be longer than N elements, 
causing a “too many values to unpack” exception.
'''


# Python “star expressions” can be used to address this problem. 
def drop_first_last(grades): 
    first, *middle, last = grades 
    return avg(middle)

'''
Solution
'''
# suppose you have user records that consist of a name and email address, 
# followed by an arbitrary number of phone number
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

user_record = ('Dave', 'dave@example.com')
name, email, *phone_numbers = user_record

# The starred variable can also be the first one in the list.
sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record 
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs) 
print(trailing_avg, current_qtr)

'''
Discussion
'''
# Extended iterable unpacking is tailor-made for unpacking iterables of
# unknown or ar‐ bitrary length
# It is worth noting that the star syntax can be especially useful 
# when iterating over a sequence of tuples of varying length

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]
def do_foo(x, y): 
    print('foo', x, y)
def do_bar(s): 
    print('bar', s)
for tag, *args in records: 
    if tag == 'foo':
        do_foo(*args) 
    elif tag == 'bar':
        do_bar(*args)
        
# Star unpacking can also be useful when combined 
# with certain kinds of string processing operations, such as splitting

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)
print(fields)


# Sometimes you might want to unpack values and throw them away. 
# You can’t just specify a bare * when unpacking, but you could use 
# a common throwaway variable name, such as _ or ign (ignored).

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)

# There is a certain similarity between star unpacking and 
# list-processing features of var‐ ious functional languages
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)

# One could imagine writing functions that perform such splitting 
# in order to carry out some kind of clever recursive algorithm

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
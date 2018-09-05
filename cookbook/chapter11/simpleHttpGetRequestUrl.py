#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:18:54 2018

@author: sungyunlee
"""

from urllib import request, parse # Base URL being accessed

#http://www.interpark.com/malls/index.html?smid1=header&smid2=logo
#http://bimage.interpark.com/UI/pc/main/2017/gnb/logo_book.png
url = 'http://www.interpark.com/malls/index.html'
# Dictionary of query parameters (if any)
parms = {
   'smid1' : 'header',
   'smid2' : 'logo'
}
# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
#u = request.urlopen(url+'?' + querystring)
u = request.urlopen(url+'?', querystring.encode('ascii'))
print(u.header_items())
print(u.geturl())
print(':'.join(hex(x)[2:] for x in querystring.encode('ascii')))

#resp = u.read()
resp_header = u.info()
print(resp_header)
print('Response Content Type is = ', resp_header["content-type"])
print('Response Content Length is = ', resp_header["content-length"])
 

'''
for line in u.readline():
    print(line)
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:48:10 2018

@author: sungyunlee
"""


from urllib import request, parse # Base URL being accessed

print("############### Request Section ###############")
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

# Extra headers
headers = {
    'User-agent' : 'SmartStudyTool',
    'Spam' : 'Eggs'
}
#req = request.Request(url+'?', querystring.encode('ascii'), headers=headers)
req = request.Request(url+'?', querystring.encode('ascii'))
req.add_header('User-agent', 'SmartStudyTool')
req.add_header('Spam', 'Eggs')

print(req.get_full_url())
print(req.header_items())

# Make a GET request and read the response
u = request.urlopen(req)

print("############### Response Section ###############")
#resp = u.read()
resp_header = u.info()
print(resp_header)
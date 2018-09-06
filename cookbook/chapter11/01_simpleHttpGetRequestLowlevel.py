#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:50:16 2018

@author: sungyunlee
"""
import urllib.request
from http.client import HTTPConnection
from urllib import parse

print("############### Response HEAD Section ###############")
c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()
    
print('Status', resp.status)
for name, value in resp.getheaders():
    print(name, value)
print("############### Response Auth Section ###############")
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_opener(auth)
r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
#resp = u.read()
resp_header = u.info()
print(resp_header)
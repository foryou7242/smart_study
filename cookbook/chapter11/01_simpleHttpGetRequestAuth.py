#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:58:14 2018

@author: sungyunlee
"""
from urllib import parse # Base URL being accessed
import requests

print("############### Request Section ###############")
#http://www.interpark.com/malls/index.html?smid1=header&smid2=logo
#http://bimage.interpark.com/UI/pc/main/2017/gnb/logo_book.png
url = 'http://pypi.python.org/pypi?'
# Dictionary of query parameters (if any)
parms = {
   'action' : 'login'
}
# Encode the query string
querystring = parse.urlencode(parms)



resp = requests.get(url + '?:' + querystring, auth=('user','password'))

print("############### Response Section ###############")
resp_msg = resp.text
print(resp_msg)
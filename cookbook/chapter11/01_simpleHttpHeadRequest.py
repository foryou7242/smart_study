#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:53:49 2018

@author: sungyunlee
"""

import requests
import json

print("############### Request Section ###############")
#http://www.interpark.com/malls/index.html?smid1=header&smid2=logo
#http://bimage.interpark.com/UI/pc/main/2017/gnb/logo_book.png
url = 'http://www.interpark.com/malls/index.html'
print(url)

resp = requests.head(url)
status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']

print("############### Response Section ###############")
resp_msg = resp.text
print(status)
print(last_modified)
print(content_type)
print(content_length)
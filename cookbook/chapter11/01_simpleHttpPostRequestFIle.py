#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:35:24 2018

@author: sungyunlee
"""


import requests
import json

print("############### Request Section ###############")
#http://www.interpark.com/malls/index.html?smid1=header&smid2=logo
#http://bimage.interpark.com/UI/pc/main/2017/gnb/logo_book.png
url = 'http://www.httpbin.org/post'

# Extra headers
headers = {
    'User-agent' : 'SmartStudyTool'
}

# File
file = { 'file': ('data.json', open('data.json', 'rb')) }

resp = requests.post(url, files=file, headers=headers)
print(file)
print("############### Response Section ###############")
resp_msg = resp.text
print(resp_msg)

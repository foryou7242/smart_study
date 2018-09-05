#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:17:52 2018

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
    'User-agent' : 'SmartStudyTool',
    'Content-type' : 'application/json'
}

# Body
body = {
   'text': 'Hello HTTP #1 **cool**, and #1!'
}
json_body = json.dumps(body)

resp = requests.post(url, data=json_body, headers=headers)
print(resp.url)
print(headers)
print(json_body)

print("############### Response Section ###############")
resp_msg = resp.text
print(resp_msg)

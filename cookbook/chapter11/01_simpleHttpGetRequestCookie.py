#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:28:38 2018

@author: sungyunlee
"""

import requests
import json

print("############### Request Section ###############")
#http://www.interpark.com/malls/index.html?smid1=header&smid2=logo
#http://bimage.interpark.com/UI/pc/main/2017/gnb/logo_book.png
url = 'http://www.interpark.com'

# Extra headers
headers = {
    'User-agent' : 'SmartStudyTool'
}


# First request
resp1 = requests.get(url)
# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)
print("############### Response Section ###############")
resp_msg = resp2.text
print(resp_msg)

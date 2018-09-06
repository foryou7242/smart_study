#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:58:11 2018

@author: sungyunlee
"""

import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37', headers = { 'User-agent': 'goaway/1.0' })
resp = r.json
print(resp)
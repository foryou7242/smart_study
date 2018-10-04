#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:38:03 2018

@author: son
"""



line = 'asdf fjdk; afed, fjek,asdf          foo'
import re
re.split(r'[;,\s]\s*', line)
print(line)

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:10:06 2016
reduce1 for Project 3

@author: Dale
"""

import sys

current_vowelset = None
current_total = 0
vowelset = None

for line in sys.stdin:
    line = line.strip()
    vowelset, total = line.split(":")
    total = int(total)
    if current_vowelset == vowelset:
        current_total += total
    else:
        if current_vowelset:
            print('%s : %s' % (current_vowelset, current_total))
        current_total = total
        current_vowelset = vowelset
if current_vowelset == vowelset:
    print('%s : %s' % (current_vowelset, current_total))
    
    

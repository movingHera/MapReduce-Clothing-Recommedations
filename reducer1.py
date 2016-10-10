# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:10:06 2016
reduce1 for Project 3

@author: Dale
"""

import sys

current_vowelcount = None
current_total = 0
vowelcount = None

for line in sys.stdin:
    line = line.strip()
    vowelcount, total = line.split(":")
    total = int(total)
    if current_vowelcount == vowelcount:
        current_total += total
    else:
        if current_vowelcount:
            print('%s : %s' % (current_vowelcount, current_total))
        current_total = total
        current_vowelcount = vowelcount
if current_vowelcount == vowelcount:
    print('%s : %s' % (current_vowelcount, current_total))
    
    

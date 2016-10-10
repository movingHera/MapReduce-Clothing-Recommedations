# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:52:56 2016
Output1 for Project 3

@author: Dale
"""
import sys

line = sys.stdin.readline()
while line:
    for word in line.split():
        vowels = [] 
        for char in word.lower():
            if char in "aeiouy":
                vowels.append(char)
        print(''.join(map(str,sorted(vowels))) + " : " + "1")
    line = sys.stdin.readline()


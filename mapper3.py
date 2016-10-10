# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:52:56 2016
Output1 for Project 3

@author: Dale
"""
import sys

line = sys.stdin.readline().split()

while line:
    clothingID = line[0]
    for ID in line:
        if line.index(ID) > line.index(":") and line[line.index(ID)] != "!":
            if line.index(ID) > line.index("!"):
                print(clothingID + " : " + "!" + ID)
            else:
                print(clothingID + " : " + ID)
    line = sys.stdin.readline().split()
    


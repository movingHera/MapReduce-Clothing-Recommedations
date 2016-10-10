# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:10:06 2016
reduce1 for Project 3

@author: Dale
"""

import sys
import itertools
import collections

line = sys.stdin.readline().split()

## Enter lines into key, value pairs in a dictionary
clothingIDs = dict()
while line:
    if line[0] in clothingIDs:
        clothingIDs[line[0]].append(line[2])
    else:
        clothingIDs[line[0]] = [line[2]]
    line = sys.stdin.readline().split()

## Sort the dictionary by keys
clothingIDs = collections.OrderedDict(sorted(clothingIDs.items()))

## Extract keys to log all combinations
## For each key combination, return only those values that pair well with all keys
IDs = list(clothingIDs.keys())
for L in range(2,len(IDs)+1):
    for subset in itertools.combinations(IDs,L):
        values = []
        
        ## Avoid items that do not pair well with the item of interest (indicated by "!")
        for i in subset:
            values.append([v for v in clothingIDs[i] if "!" not in v])
        
        ## Combine the list of lists to get one list of all recommended items for all keys in the pairing
        ## Example: for the "1 2" pairing, combine [2, 3, 5] and [1, 3, 4, 5]
        values_combined = list(itertools.chain.from_iterable(values))
        
        ## Only include recommended clothing items that pair well with all items in the shopping cart
        ## The number of appearances of the value must equal that number of items in the shopping cart
        final_values = []
        for cnt in values_combined:
            if values_combined.count(cnt) == len(subset):
                final_values.append(cnt)
        
        ## Print the shopping cart pairing and recommended items
        print(" ".join(str(e) for e in subset) + " : " + " ".join(str(e) for e in sorted(list(set(final_values)))))
        
    

    

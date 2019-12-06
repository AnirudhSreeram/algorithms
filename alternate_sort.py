#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 6 2019

@author: Anirudh Sreeram
"""

def alternateSort (arr,n):
    arr.sort()   # Sort the array in ascending order. 
    print(arr)
    
    # Create pointers for the beginning and the end of the array.
    hi = n-1
    low = 0
    
    
    while(hi > low):
        print (str(arr[hi]), end =" "),
        print (str(arr[low]), end =" ")
        hi -=1  # Decrement the end pointer by one.
        low += 1  # Increment the pointer in the beginning by one.
        
    # Odd number of elements are present in the array.    
    if (n % 2 != 0):
        print(arr[low], end =" ") # type the middle most number in the end.


# Initial inputs.    
arr = [1, 12, 4, 6, 7, 10]  
n = len(arr) 
print(arr)  
alternateSort(arr, n)  


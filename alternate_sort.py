#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 6 2019

@author: Anirudh Sreeram
"""

def alternateSort (arr,n):
    arr.sort()
    print(arr)
    hi = n-1
    low = 0
    
    while(hi > low):
        print (str(arr[hi]) + " ")
        hi -=1
        print (str(arr[low]) + " ")
        low += 1
    if (n % 2 != 0):
        print(arr[low])
    
arr = [1, 12, 4, 6, 7, 10]  
n = len(arr) 
print(arr)  
alternateSort(arr, n)  


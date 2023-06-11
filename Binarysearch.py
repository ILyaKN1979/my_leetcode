# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:09:14 2023

@author: IlYA
"""

array = [1, 2, 6, 8, 12, 45, 77 ,78, 88, 99,100,111]

x= 111

left =  0 
right = len(array)

while left<=right:
    res = (left+right)//2
    if array[res]==x:
        break
    elif array[res]>x: 
        right =res-1
    elif array[res]<x:
        left = res+1
        
print(array[res])        
        


        
        
    



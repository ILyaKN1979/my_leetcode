# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:03:56 2023

Given an integer array nums where every element appears three times except for one, which appears
exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99



@author: IlYA
"""

nums = [0,99,0,1,0,1,1]
nums = [2,2,3,2]

res = 0
tmp = 0

for num in nums:
    res = (res ^ num) & ~tmp
    #print(res)
    tmp = (tmp ^ num) & ~res


print(res)

   

#---------------------------------------------
# the first idea, but coplexity is O(n*n)
v_is={}

for v in nums:
    if v in v_is.keys():
        v_is[v]+=1
    else:
        v_is[v]=1

for  i,v in v_is.items():
    if v==1:
        res = i 
        
print(res)        
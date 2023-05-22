# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:52:47 2023

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.


Examples:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

@author: IlYA
"""

nums = [1,1,1,2,2,3]
k = 2

tmp_dict = {}
res = []

for i, v in enumerate(nums):
    tmp_dict[v] = tmp_dict.get(v, 0) + 1

res = sorted(tmp_dict, key=tmp_dict.get, reverse=True)[:k]


# the first variant the complexity is O(n + k * (n + 1)) 
"""
tmp_dict = {}    
res =[]
for i,v in enumerate(nums):
    if v not in tmp_dict:
        tmp_dict[v]=1
    else:     
        tmp_dict[v]+=1
i=1        
while i<=k: 
    max_tmp = max(tmp_dict, key=tmp_dict.get)
    res.append(max_tmp)
    del tmp_dict[max_tmp]
    i+=1
"""
print(res)


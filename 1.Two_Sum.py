# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:36:54 2023

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Examples: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Input: nums = [3,2,4], target = 6
Output: [1,2]

@author: IlYA
"""
import time 

nums = [2,7,11,15]
target = 9
output = 0 


nums = [2,7,11,15]
target = 9


start_time = time.perf_counter()

dic = {}
for i in range(0, len(nums)):
    
    difference = target - nums[i] 
    
    if difference in dic:
        output = [dic[difference], i]
 
    dic[nums[i]] = i             
     
print(output)

print(time.perf_counter()-start_time)
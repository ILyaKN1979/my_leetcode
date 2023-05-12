# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:06:31 2023

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

@author: IlYA
"""




nums1 = [4]
nums2 = [-3,-1]


new_nums = sorted(nums1 + nums2)

len_nums = len(new_nums)
 
if  len_nums % 2 != 0:
    res = new_nums[int((len_nums-1)/2)]
else:
    res = (new_nums[int(len_nums/2-1)] + new_nums[int(len_nums/2)])/2
"""
new_nums = []
len_nums1 =len(nums1)
len_nums2 =len(nums2)
j = 0
i = 0
fl_i=0
if len_nums1<1:
    new_nums=nums2
else:     
    while i < len_nums1:
            
        while j <len_nums2:
                
            if fl_i==0 and nums1[i] < nums2[j] :
                   
                    new_nums.append(nums1[i])
                    i+=1
                    if i==len_nums1:
                        fl_i=1
                    else: 
                        break
                    
            else: 
                new_nums.append(nums2[j])
                if j<len_nums2:
                    j+=1
                if i<len_nums1-1 :
                    break
        
        if j==len_nums2 and (i<len_nums1 or i==0) :
           new_nums.append(nums1[i]) 
           i+=1

len_nums=len(new_nums)

if  len_nums % 2 != 0:
    res = new_nums[int((len_nums-1)/2)]
else:
    res = (new_nums[int(len_nums/2-1)] + new_nums[int(len_nums/2)])/2

    
"""    
    
print(res)   











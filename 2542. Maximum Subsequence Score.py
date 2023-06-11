# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:43:30 2023

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. 
You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.

It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ...,nums2[ik - 1]).

Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

@author: IlYA
"""
nums1 = [2,1,14,12]
nums2 = [11,7,13,6]
k = 3


nums1 = [1,3,3,2]
nums2 = [2,1,3,4] 
k = 3


# output = 168 
max_score = 0

from itertools import combinations


for indices in combinations(range(len(nums1)), k):
    sum_nums1 = sum(nums1[i] for i in indices)
    min_nums2 = min(nums2[i] for i in indices)
    
    score = sum_nums1 * min_nums2
    max_score = max(max_score, score)


print(max_score)




"""
res = 0
j=0
i=0
while i in range(0, len_n):
    if i+k <= len_n:
        tmp=score(nums1[i:i+k], nums2[i:i+k]) 
        if tmp > res:
            res = tmp
        i+=1 
    else:
       break
       if j+k < len_n:
            j+=1
            i=j
       else:
           break

#print(res)

"""


















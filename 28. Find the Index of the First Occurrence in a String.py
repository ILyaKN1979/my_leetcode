# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:52:56 2023

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack
or -1 if needle is not part of haystack.

Examples:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

@author: IlYA
"""

haystack = "qqqaaaq"
needle = "aaa"

len_s1 = len(haystack)  # Length of haystack
len_s2 = len(needle)    # Length of needle

if len_s1 == len_s2:  # If both strings have the same length
    if haystack == needle:  # If haystack is equal to needle
        res = 0  # Set the result to 0
    else:
        res = -1  # Set the result to -1 (not found)

elif len_s1 > len_s2:  # If haystack is longer than needle
    for i in range(0, len_s1 - len_s2 + 1):  # Iterate over possible starting positions
        if needle == haystack[i:i + len_s2]:  # Check if the substring matches the needle
            res = i  # Set the result to the starting position
            break  # Exit the loop since we found a match
        else:
            res = -1  # Set the result to -1 (not found)

else:  # If haystack is shorter than needle
    res = -1  # Set the result to -1 (not found)

print(res)  # Print the result

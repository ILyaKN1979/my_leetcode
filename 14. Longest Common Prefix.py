# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 06:14:50 2022

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


@author: IlYA K
"""

strs = ["flower","flow","flight"]

def longest_common_prefix(strs):
    if not strs:
        return ""
           
    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:len(prefix)-1]
            if not prefix:
                return ""
    return prefix

print(longest_common_prefix(strs))
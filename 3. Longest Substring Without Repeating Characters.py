# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:08:04 2023

Given a string s, find the length of the longest 
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

@author: IlYA
"""

s = "abcabcxsbb"

chars = set()
i, j = 0, 0
res = 0
while j < len(s):
    if s[j] not in chars:
        chars.add(s[j])
        j += 1
        res = max(res, j - i)
        
    else:
        chars.remove(s[i])
        i += 1

print(res)


"""
# This version 1.0 is working  but not optimal  

res = 0 
len_s= len(s)

if len_s>0:
    for k,v in enumerate(s):
        list_tmp = []
        list_tmp.append(v)
        counter = 1    
        for i in range(k+1,len_s):
            if s[i] not in list_tmp:
                counter+=1
                list_tmp.append(s[i])
                
            else: break
        if counter>res:
            res=counter
            print(list_tmp)

print (res)
"""    
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:27:04 2023

Given a string s, return the longest 
palindromic substring in s.


Examples:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
-----
Input: s = "cbbd"
Output: "bb"

@author: IlYA
"""

s = "accd"

def palindromic_f (st):
    return st == st[::-1]


if len(s)== 1:
    res = s
else: 
    res =""
    while len(s)> 1:
      
        sub_s = s
        if palindromic_f(sub_s) == True and len(res)<len(s): 
            res = sub_s
            break
                
        for j in range(0, len(s)):
            sub_s = s[j+1:]
            if palindromic_f(sub_s) == True and len(res)<len(sub_s): 
                res = sub_s
          
            sub_s = s[:-(j+1)]
            if palindromic_f(sub_s) == True and len(res)<len(sub_s): 
                res = sub_s
        
        s = s[1:len(s)-1]
       
            
print("res = "+res)        


"""
# this implementation is O(n^3) 
def palindromic_f (st):
    return st == st[::-1]

len_s= len(s)
if len_s == 1:
    res = s
else: 
    res =""
    
    
for i in range(0,len_s):
    sub_s = s[i]
    if  len(res)<len(sub_s): 
            res = sub_s
    for j in range(i+1, len_s):
        sub_s = sub_s +s[j]
        if palindromic_f(sub_s) == True and len(res)<len(sub_s): 
            res = sub_s
    
print(res)        
"""

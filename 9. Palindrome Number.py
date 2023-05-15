# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:11:07 2023
Given an integer x, return true if x is a 
palindrome
, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


@author: IlYA
"""

x = -121

res = str(x) == str(x)[::-1]

print(res)    



"""
tmp1=[]
tmp2=[]
num = x


res=False
if num>=0: 
        
    x = [int(a) for a in str(num)]
    print(x)

    if len(x) % 2==0:
        k=int(len(x))
        tmp1 = list((x[:int(k/2)]))
        tmp2 = list(reversed(x[int(k/2):]))  
        print(tmp1, tmp2)
        if tmp1 ==tmp2 :
            res=True
    else:
        k=int(len(x))
        print(k)
        tmp1 = list((x[:(int((k-1)/2))]))
        tmp2 = list(reversed(x[(int((k-1)/2+1)):]))  
        print(tmp1, tmp2)
        if tmp1 ==tmp2 :
            res=True
print(res)
"""


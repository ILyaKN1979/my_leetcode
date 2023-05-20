# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:55:05 2023

Given two binary strings a and b, return their sum as a binary string.

Examples:

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

@author: IlYA
"""

a = "1010"

b = "1011"

a_r= a[::-1]
b_r= b[::-1]

len_a = len(a_r)
len_b = len(b_r)

res =[]
corr = 0 
if len_a>=len_b:
    for i in range(0, len_a):
        if i<len_b:
            s = int(a_r[i])+int(b_r[i])+corr
            
            if s == 2: 
                res.append('0')
                corr = 1 
            elif s == 3: 
                res.append('1')
                corr = 1 
            else: 
                corr=0 
                res.append(str(s))
        else:        
            if i < len_a: 
                s= int(a_r[i]) + corr
                if s==2:
                    
                    res.append('0')
                    corr = 1 
                else:
                    corr=0 
                    res.append(s)
    if corr == 1:
        res.append('1')
else: 
    for i in range(0, len_b):
        if i<len_a:
            s = int(a_r[i])+int(b_r[i])+corr
            
            if s == 2: 
                res.append('0')
                corr = 1 
            elif s == 3: 
                res.append('1')
                corr = 1 
            else: 
                corr=0 
                res.append(str(s))
        else:        
            if i < len_b: 
                s= int(b_r[i]) + corr
                if s==2:
                    
                    res.append('0')
                    corr = 1 
                else:
                    corr=0 
                    res.append(s)
    if corr == 1:
        res.append('1')    
    
    
print(''.join(res[::-1]))                  

# this solution is more slowly

res=''
carry=0 

i= len(a)-1
j = len(b)-1 

while i>=0 or j>=0 :
    bit_a = int(a[i]) if i >= 0 else 0
    bit_b = int(b[j]) if j >= 0 else 0
    
    sum = bit_a + bit_b + carry
    bit = sum % 2
    carry = sum // 2
    
     
    res= str(bit)+res 
    i-=1
    j-=1
     
if carry:
    res = '1'+ res 

print(res) 

        
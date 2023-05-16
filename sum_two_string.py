# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s1= '999'
s2= '111'

test= int(s1)+int(s2)

len_s1=len(s1)
len_s2=len(s2)
s1_rev=s1[::-1]
s2_rev=s2[::-1]
res = []

m = 0
if len_s1 >= len_s2: 
    for i in range(0, len_s1):
       
        if i<len_s2:
            s = int(s1_rev[i]) + int(s2_rev[i]) + m
        else: 
            s = int(s1_rev[i]) + m
            
        if s>9:
            m=1 
            res.append(str(s)[1])

        else: 
            m=0 
            res.append(str(s)[0])
    if m == 1:
        res.append(str(m))
else: 
    for i in range(0, len_s2):
       
        if i<len_s1:
            s = int(s2_rev[i]) + int(s1_rev[i]) + m
        else: 
            s = int(s2_rev[i]) + m
            
        if s>9:
            m=1 
            res.append(str(s)[1])

        else: 
            m=0 
            res.append(str(s)[0])
    if m == 1:
        res.append(str(m))



res = ''.join(res[::-1])  


            
print (res)             
print (test)

   
          
        

        

        
        
        
            
            
            
            
    
    
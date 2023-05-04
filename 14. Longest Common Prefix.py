# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 06:14:50 2022

@author: IlYA K
"""

strs = ["ab", "a"]

res=''
fl_stop=0


if  len(strs)==1:
    res=strs[0]
    fl_stop=1


for j in range(0, len(strs[0])):
    
    counter=0   
    
    if (fl_stop == 0):
         
        for i in range(1, len(strs)): 
            
            len_first=len(strs[0])
            
            len_next= len(strs[i])
            
           
            if len_next-j>0:
                
                if strs[0][j] == strs[i][j]:                
     
                    counter=counter+1
                    
                else:
                    
                    fl_stop=1
                    break
        
                if counter == len(strs)-1: 
                    res=res+strs[i][j]
                    #fl_stop=1
           
    
    else:
        break        
    
print(res)
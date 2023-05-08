# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:34:37 2023


Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements

on the secondary diagonal that are not part of the primary diagonal.

 
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.



@author: IlYA
"""

mat = [[7,3,1,9],
       [3,4,6,9],
       [6,9,6,6],
       [9,5,8,5]]

#Output: 55

#mat=[[6]]

size = len(mat)
res = 0

for i in range(0, size):
     res+= mat[i][i] + mat[size-1-i][i]
    

if size%2 != 0:
    res-=  mat[int((size+1)/2)-1][int((size+1)/2)-1] 
    print('!!!')    
    
    

print(res)
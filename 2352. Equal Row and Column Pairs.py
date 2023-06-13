# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:08:58 2023

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Examples: 

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

@author: IlYA
"""


import numpy as np

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
res = 0

grid = np.array(grid)  # Convert to NumPy array
n = len(grid)

rows = [tuple(row) for row in grid]  # Convert rows to tuples

for i in range(n):
    count = rows.count(tuple(grid[:, i])) 
    if count>0:
        res += count
        
print(res)

# not good version 
'''
for i in range(n):
    for j in range(n):
        if np.array_equal(grid[i, :], grid[:,j]):
            res += 1

print(res)
'''
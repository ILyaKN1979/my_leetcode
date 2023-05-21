# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:15:42 2023

You are given an n x n binary matrix grid where 1 represents land and 0 
represents water.

An island is a 4-directionally connected group of 1's not connected to any
other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 
Examples:

Input: grid = [[0,1],[1,0]]
Output: 1


Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2


Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


@author: IlYA
"""

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

for row in grid:
    for item in row:
        print("{:3}".format(item), end=" ") 
    print() 

print('---------')    

def find_island(i, j, island):
    # Recursive function to find an island given its starting position (i, j)
    if i < 0 or j < 0 or j >= len_g or i >= len_g or (i,j) in v:
        return
    if grid[i][j] == 1:
        v[(i, j)] = 1
        island.append((i, j))
        # Explore neighboring cells in all four directions
        find_island(i + 1, j, island)
        find_island(i, j + 1, island)
        find_island(i - 1, j, island)
        find_island(i, j - 1, island)
    return island


len_g = len(grid)
v = {}
first = []
second = []

# Iterate through each cell in the grid
for i in range(len_g):
    for j in range(len_g):
        if (i, j) not in v:
            # If the cell is unvisited and contains a 1, find the island it belongs to
            if grid[i][j] == 1:
                if not first:
                    # If first island is empty, assign the result to first
                    first = find_island(i, j, [])
                else:
                    # Otherwise, assign the result to second
                    second = find_island(i, j, [])
     

res = float('inf')
# Calculate the smallest distance required to connect the two islands
for i in first:
    for j in second:
        l = abs(i[0] - j[0]) + abs(i[1] - j[1])-1
        if res > l:
            res = l

# Print the positions of the two islands, and the smallest number of 0's required to connect them
print(first)
print(second)
print('---------')
print(res)
         
            
            
            
            
            
            
            
            
            
        
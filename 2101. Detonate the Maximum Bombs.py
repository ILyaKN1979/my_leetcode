# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:55:18 2023

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.


Examples: 
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

@author: IlYA
"""


#bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

#bombs = [[1,1,10],[10,10,1]]

#bombs = [[56,80,2],[55,9,10],[32,75,2],[87,89,1],[61,94,3],[43,82,9],[17,100,6],[50,6,7],[9,66,7],[98,3,6],[67,50,2],[79,39,5],[92,60,10],[49,9,9],[42,32,10]]
#res= 3

bombs = [[4,4,3],[4,4,3],[4,4,3],[4,4,3]]


#bombs= [[2,71,5],[16,58,8],[19,28,9],[38,53,3],[80,95,10],[29,74,9],[17,50,10],[94,1,3],[47,64,5],[40,29,7],[65,78,5],[84,95,3],[45,29,1],[56,99,9],[73,3,4],[16,79,4],[79,43,4],[20,27,1],[49,68,6]]
# res= 2

bombs = [[7,26,7],[7,18,4],[3,10,7],[17,50,1],[3,25,10],[85,23,8],[80,50,1],[58,74,1],[38,39,7],[50,51,8],[31,99,3],[53,6,5],[59,27,10],[87,78,9],[68,58,3]]
#res = 3

#bombs =[[2,1,3],[6,1,4]]

#bombs =[[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
#res= 9 


def nearby_bombs(bomb1, bomb2):
    if ((bomb1[0]-bomb2[0])**2+(bomb1[1]-bomb2[1])**2)**0.5<=bomb1[2]:
        return True
    else: 
        return False 

tmp_list = [[] for v in bombs]
number = len(bombs)

for i in range(0, number):
    for j in range(0, number):
        if i==j:
            continue
        if nearby_bombs(bombs[i], bombs[j]): 
            tmp_list[i].append(j)

max_res = 1          
for x in range(len(tmp_list)):
    if len(tmp_list[x])<1:
        continue
    res = 1
    seen = {x}
    
    stack = [x]
    while stack: 
        new = stack.pop()
        for v in tmp_list[new]: 
            if v not in seen: 
                res += 1
                seen.add(v)
                stack.append(v)
    
    if max_res<res: 
        max_res=res
print('result = '+ str(max_res))    
        

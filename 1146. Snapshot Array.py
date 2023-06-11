# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 11:04:42 2023

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


@author: IlYA
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.array = {i: [[-1, 0]] for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.array[index]
        
        # Check if the requested snap_id is within the range of snapshots for the index
        if snapshots[0][0] > snap_id:
            return 0
        if snapshots[-1][0] <= snap_id:
            return snapshots[-1][1]
        
        # Perform binary search to find the correct snapshot
        left, right = 0, len(snapshots) - 1

        while left <= right:
            mid = (left + right) // 2
            if snapshots[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return snapshots[right][1]



# Try to use SnapshotArray
 
obj = SnapshotArray(5)
param_1 = None
obj.set(0,3)
param_2 = None
param_3 = obj.snap()

obj.set(0, 5)
param_4 = None
param_5 = obj.snap()
param_6 = obj.get(0,1)
param_7= obj.get(0, 0)

print([param_1, param_2, param_3, param_4, param_5, param_6,param_7])
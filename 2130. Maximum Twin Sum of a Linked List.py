# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:48:50 2023

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of 

the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes
with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 


@author: IlYA
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):
    tmp_array = []
    while head: 
        tmp_array.append(head.val)
        head = head.next
    if len(tmp_array) == 1: 
        res = tmp_array[0]
    s=0
   
    if len(tmp_array) %2 ==0: 
        fl = 0
    else:
        fl = 1
     
    len_array = len(tmp_array)//2  

    for i in range(0, len_array+1):
        if fl==1 and i==len_array:
            if tmp_array[i] > s: 
               s = tmp_array[i]
               break
        if (tmp_array[i] + tmp_array[-(i+1)]) > s:
            s = tmp_array[i] +tmp_array[-(i+1)]    

    return s

# test
l = [4,9,2]

# The function that takes the head of the linked list and the new node's value to be added.
def addNode(head, new_val):
    new_node = ListNode(new_val)
    if not head:  # If the list is empty, make the new node the head
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next

        current.next = new_node
    return head

# Create a linked list l1
for i,v in enumerate(l):
    if i == 0 :
        l1 = ListNode(v)
    else:     
        l1 = addNode(l1, v)

print(pairSum(l1))



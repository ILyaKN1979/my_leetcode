# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:01:44 2023

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Exampls:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

@author: IlYA
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    
   if not head or not head.next: 
       return head 
   next_pair = head.next.next 
   new_ll = head.next
   new_ll.next = head
   head.next = swapPairs(next_pair)
   
   return new_ll

# test
l = [1,2,3,4]

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

        
# Swap every two adjacent nodes
result = swapPairs(l1)

while result:
    print(result.val)
    result = result.next



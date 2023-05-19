# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:39:26 2023

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.


Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

@author: IlYA
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoList(list1, list2):
    dummy = ListNode(0)
    curr = dummy
    
    # Traverse both lists until one of them reaches the end
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    # Append the remaining nodes of the non-empty list
    if list1:
        curr.next = list1
    if list2:
        curr.next = list2
    
    return dummy.next



# test
l1 = [1,2,4] 
l2 = [1,3,4]

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

# Create a linked list l1_n
    
for i,v in enumerate(l1):
    if i == 0 :
        l1_n = ListNode(v)
    else:     
        l1_n = addNode(l1_n, v)

# Create a linked list l2_n

for i,v in enumerate(l2):
    if i == 0 :
        l2_n = ListNode(v)
    else:     
        l2_n = addNode(l2_n, v)
    

      
# Swap every two adjacent nodes

result = mergeTwoList(l1_n, l2_n)

while result:
    print(result.val)
    result = result.next



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
    
    new = True 
    while list1 or list2:
        
        if list1 and list2:
            
            if list1.val <= list2.val:
                l_fl1= True
                l_fl2= False
                if new == True:
                    l_n = ListNode(list1.val)
                    new = False
                else:
                    l_n=addNode(l_n , list1.val)
            else:
                l_fl2= True
                l_fl1= False
                if new == True:
                   l_n = ListNode(list2.val)
                   new = False
                else:
                    addNode(l_n , list2.val)
        else:
              if list1:
                 l_fl1= True
                 l_fl2= False
                 
                 if new == True:
                     l_n = ListNode(list1.val)
                     new = False
                 else:
                     l_n=addNode(l_n , list1.val) 
              if list2:
                l_fl2= True
                l_fl1= False
                if new == True:
                    l_n = ListNode(list2.val)
                    new = False
                else:
                   l_n=addNode(l_n , list2.val) 
   
         
        if list2 and l_fl2:
            list2 = list2.next
        if list1 and l_fl1:
            list1 = list1.next   
          

    return l_n

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



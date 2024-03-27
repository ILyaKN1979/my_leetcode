# -*- coding: utf-8 -*-
"""
Spyder Editor

Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.




"""
class Stack(object):  # Define a stack class
    
    def __init__(self):  # Initialize the stack
        self.array = []  # Initialize an empty array to store elements
        
    def is_empty(self):  # Check if the stack is empty
        if len(self.array) == 0:  # If the length of the array is 0
            return True  # The stack is empty
        else:  # Otherwise
            return False  # The stack is not empty
        
    def add_value(self, new):  # Method to add a value to the stack
        self.array.append(new)  # Append the new value to the stack
        
    def size(self):  # Method to get the size of the stack
        return len(self.array)  # Return the length of the array, which is the size of the stack
    
    def take_value(self):  # Method to take a value from the stack
        last = self.array.pop()  # Remove and return the last element from the stack
        return last  # Return the last element
        
stack = Stack()  # Create an instance of the Stack class



def balanced_parentheses(s):  # Function to check if parentheses are balanced
    tmp_start = ('(', '[', '{')  # Define the opening parentheses

    tmp_out = {('(', ')'), ('[', ']'), ('{', '}')}  # Define the pairs of parentheses

    if len(s) % 2 != 0:  # If the length of the s is odd
        return False  # The parentheses cannot be balanced
    
    for char in s:  # Iterate through each character in the s
        if char in tmp_start:  # If the character is an opening parenthesis
            stack.add_value(char)  # Add it to the stack
        else:  # If the character is a closing parenthesis
            if stack.is_empty():  # If the stack is empty
                return False  # The parentheses cannot be balanced
            if (stack.take_value(), char) not in tmp_out:  # If the pair of parentheses is not valid
                return False  # The parentheses cannot be balanced
            
    return stack.is_empty()  # If all parentheses are balanced, return True

print(balanced_parentheses('{[]}'))  # Test the function


from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()

t.test(balanced_parentheses)

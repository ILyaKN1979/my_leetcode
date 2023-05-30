# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:27:14 2023

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

@author: IlYA
"""

s= "-13+8"

s = s.lstrip()
temp= ('1','2','3','4','5','6','7','8','9','0')
fl = True
fl_m = False
fl_p = False
res = 0
s_res = ''

if len(s)==0:
    res = 0
elif len(s) == 1:
    if s[0] in temp:
        res = int(s[0])
    else:
        res = 0
elif len(s)>1: 
    if s[0] == '+' and s[1] =='-':
        res =0 
    elif s[0] == '-' and s[1] == '+':
        res = 0 
    elif s[0] == '-' and s[1] == '-':
        res = 0 
    elif s[0] == '+' and s[1] == '+':
        res = 0 
    
    else:
        for l in s:
            if l == '+' and fl_m==False:
                continue
            if  l =='-' and fl_m==False:
                s_res += l 
                fl_m = True
                continue
            if fl == True and l in temp: 
                fl_m=True
                s_res+=l
            else:
                fl=False

                
if len(s_res)!=0 and s_res!='-':
    if int(s_res)>2**31:
        res = 2**31-1
    elif int(s_res)<-(2**31):
        res = -(2**31)     
    else: 
        res = int(s_res)

print(res)        
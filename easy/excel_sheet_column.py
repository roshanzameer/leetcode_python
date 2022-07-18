# https://leetcode.com/problems/excel-sheet-column-number/submissions/

"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

"""

def titleToNumber(columnTitle):
    
    #alnum_map = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5} # Not needed if using ord
    
    place_value = len(columnTitle) - 1
    sum = 0
    

    for i in range(len(columnTitle)):
        sum += ((26 ** place_value) * (ord(columnTitle[i]) - 64))
        place_value -=1
        #because ord(A) is 65. And ord(char) - 64 gives ordered values for char starting from 1. 
    
    return sum
            

print(titleToNumber('AAC'))
            



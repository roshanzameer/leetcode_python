# https://leetcode.com/problems/valid-parentheses/

#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "()[]{}"
#Output: true


def isValid(s: str) -> bool:
	
	record = [] 
	
	pairs = {"}": "{", "]": "[", ")": "("}   
	
	for sym in s:	# O(n)

		if sym == '{' or sym == '[' or sym == '(':
			record.append(sym)    # O(1)
		else:
			if len(record) >= 1 and pairs[sym] == record[-1]:   
				record.pop()    # O(1)
			else:               # If its a closed paranthesis and no open pair already seen
				return False

	return len(record) == 0 
	
	
print(isValid("()[]{"))

# Time Complexity O(n)




def isvalid_alternate(s):

	# Alternate Approach

	for i in range(len(s) // 2):

		s = s.replace('{}', '').replace('()', '').replace('[]', '')

	return len(s) == 0

print(isvalid_alternate("(("))
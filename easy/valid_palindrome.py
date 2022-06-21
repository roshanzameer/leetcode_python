# https://leetcode.com/problems/valid-palindrome/

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.



def isPalindrome(s):
    filtered_str = ''.join(e.lower() for e in s if e.isalnum())

    left = 0
    right = len(filtered_str) -1

    while left <= right:

        if filtered_str[left] != filtered_str[right]:
            return False
        left+=1
        right-=1
    return True


print(isPalindrome(' '))
      
# https://leetcode.com/problems/longest-common-prefix/

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.



def longestCommonPrefix(strs) -> str:

    res = ""
    word = min(strs, key=len)       # O(n)
    
    for i in range(len(word)):      # O(m)
        
        for j in strs:              # O(n)
                
            if j[i] != word[i]:
                return res
        res += word[i]              # O(m)  A new string is built each time
            
    return res


print(longestCommonPrefix(["flower","flow","flight"]))



# Complexity: O( n  +  m*n  +  m*m)
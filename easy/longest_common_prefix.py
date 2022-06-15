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
    word = min(strs, key=len)
    
    for i in range(len(word)):
        
        for j in strs:
                
            if j[i] != word[i]:
                return res
        res += word[i]
            
    return res


print(longestCommonPrefix(["flower","flow","flight"]))
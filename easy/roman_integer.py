# https://leetcode.com/problems/roman-to-integer/
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.


def romanToInt(s: str) -> int:
    
    """
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = s.upper()

    sum = 0
    for idx, symbol in enumerate(s):
        value = roman_dict[symbol]
        if idx+1 < len(s) and roman_dict[s[idx + 1]] > value:
            sum -= value
        else:
            sum += value

    return sum


print(romanToInt('MMMDCCXXIV'))

# https://leetcode.com/problems/plus-one/

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


def plusOne(digits):

    for i in range(len(digits)-1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits
    
        digits[i] = 0

    digits.insert(0, 1)
    return digits

print(plusOne([1,2,3,4]))



def plusOne_whileloop(digits):

    i = len(digits) -1

    while True:
        if i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                
            else:
                digits[i] += 1
                break
        
        else:
            digits.insert(0, 1)
            break

        i -= 1
    
    return digits
                

print(plusOne_whileloop([9,9,9,9]))


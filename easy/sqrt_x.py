# https://leetcode.com/problems/sqrtx/


"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
 
Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

"""


def mySqrt(x):
    if x <= 1:
        return x

    low = 1
    high = x
    
    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            low = mid + 1
            ans = mid

        else:
            high = mid - 1
    # left=0
    # right=x
    # while left<=right:
    #     mid=(left+right)//2
    #     if mid*mid==x:
    #         return mid
    #     elif mid*mid>x:
    #         right=mid-1
    #     else:
    #         left=mid+1
            

    return ans



print(mySqrt(48))



def sqrt(x):
    index = 1
    while index*index <= x:
        index += 1
    return index-1

print(sqrt(48))


# Bablylonion Algorithm: https://www.youtube.com/watch?v=RQmjgvWbMd8
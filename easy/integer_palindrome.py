def isPalindrome(num):

    # Ask whether Negative number is a palindrome or not
    # Ask whether decimal or leading zeroes can be considered or not

    # Convert to string approach

    str_int = str(num)
    rev_str = str_int[::-1]
    if str_int == rev_str:
       return True
    return False

print(isPalindrome(1221))



def isPalindromeNoString(num):

    # This approach uses Mathematic operations like Division and Modulo to check if First digit equal to Last digit and remove
    # them in every iteration
    #1.  1221 ----> 1   2 2    1 -----> 1 == 1 
    #2.   22  ----> 2          2 -----> 2 == 2
    # since every iteration returned True, the integer is a palindrome

    if num < 0:                   # Only considering Positive integers
        return False    

    div = 1

    while num >= 10 * div:               # building the divisor number
        div *= 10

    while num:
        left = num // div
        right = num % 10
        if left != right:      # First digit not equal to last, return False
            return False 

        num = (num % div) // 10       # Remove first and last digit
        div /= 100                    # remove 2 digits (0's) from divisor

    return True


print(isPalindromeNoString(125621))
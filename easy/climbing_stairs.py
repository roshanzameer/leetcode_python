# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs_recursion(n):
    """
    The pattern follows a fibonacci series. Hence can be done in 3 methods. 
    Recursion, Top Down DP, or Bottom Up DP.
    """ 

    if n <= 3:
        return n
    else:
        return climbStairs_recursion(n-1) + climbStairs_recursion(n-2) 


print(climbStairs_recursion(10)) # O(2^n)


def climbStair_bottom_up(n):

    fib_map = {0:0, 1:1, 2:2, 3:3}   # Memoization

    if n <= 3:
        return n

    else:
        for i in range(4, n+1):
            fib_map[i] = fib_map[i-1] + fib_map[i-2]

    return fib_map[n]

print(climbStair_bottom_up(10))   # O(n),  T(N)



fib_arr = [0,1,2,3] + [0]*10

def climbStair_top_down(n):
    """
    In this approach we save the solution to subproblems in a global array
    """
    if n <=3:
        return n

    if not fib_arr[n]:
        fib_arr[n] = climbStair_top_down(n-1) + climbStair_top_down(n-2)
    
    return fib_arr[n]

    

print(climbStair_top_down(10))   # # O(n), T(N)
# https://leetcode.com/problems/search-insert-position/

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Constraint: O(logn)

def searchInsert(nums, target):

    low = 0
    high = len(nums)-1

    while low <= high:            # O(logn)
        
        mid = (low + high) // 2

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid +1
        else:
            high = mid -1
        
    return low

print(searchInsert([1,2,7,8], 4))
            
        
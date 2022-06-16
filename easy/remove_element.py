# https://leetcode.com/problems/remove-element/

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).



def removeElement(nums, val):
    
    valid_size = 0              # O(1)

    for i in range(len(nums)): # O(n)
        
        if nums[i] != val:
            nums[valid_size] = nums[i]  # O(1)
            valid_size += 1             # O(1)

    print(nums)
    return valid_size




print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))

# TC: O(n)
# SC: O(1)


def remove_el(nums, val):
        
    left = 0
    
    for right in range(1, len(nums)):
        
        if nums[left] == val:
            if nums[right] == val:
                right += 1
            nums[left] = nums[right]
            left += 1
            right+=1
        
        else:
            left +=1
            

        print(left, right, nums)


print(remove_el(nums = [0,1,2,2,3,0,4,2], val = 2))

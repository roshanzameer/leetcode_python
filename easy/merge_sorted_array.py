# https://leetcode.com/problems/merge-sorted-array/


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].



def merge(nums1,m,nums2,n):


    last = m+n-1

    while m > 0 and n > 0:
        if nums1[m -1] < nums2[n-1]:
            nums1[last] = nums2[n-1]
            n -= 1
        else:
            nums1[last] = nums1[m-1]
            m -= 1
        last -= 1
        
    
    while n > 0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last-1
    
    return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
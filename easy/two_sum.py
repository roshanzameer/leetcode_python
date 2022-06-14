def twoSum(nums, target):
    
	seen_dict = {}
	
	for idx, num in enumerate(nums):
		diff = target - num
		if diff in seen_dict:
			return [idx, seen_dict[diff]]
		seen_dict[num] = idx

	return []                                           
    
			
print(twoSum([2,7,11,15], 9))

def missing_number(nums):
	n = len(nums)
	missing_value = n

	for i in range(n):
		missing_value ^= i ^ nums[i]

	return missing_value



print(missing_number([3, 0, 1]))
print(missing_number([9,6,4,2,3,5,7,0,1]))

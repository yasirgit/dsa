def find_second_largest_element(nums):
	if len(nums) < 2:
		return None

	first = second = float('-inf')

	for num in nums:
		if num > first:
			second = first
			first = num
		elif num > second and num != first:
			second = num

	return second if second != float('-inf') else None



arr = [2,3,1,5,4]
print(find_second_largest_element(arr))
# Implement Binary Search 
# 	Explanation: Halve a sorted array repeatedly to locate the target. 
# 	Example: [1,3,5,7,9], target=5 → index=2

# 1. Restate the problem in your own words
# 	“We have a sorted array and a target value. We want to find the index of the target using binary search, 
# 		which repeatedly halves the search space. If the target isn’t present, we should return some ‘not found’ indicator like -1.”

# 2. Clarify the requirements
# 	- Return type / behavior
# 		- “Should I return the index of the target, or a boolean?”
# 		- “If the target is not found, should I return -1, or something else?”
# 	- Duplicates
# 		- “If there are multiple occurrences of the target, do you want any one index, or specifically the first or last occurrence?”
# 	- Input guarantees
# 		- “Can I assume the array is sorted in non-decreasing order?”
# 		- “Could the array be empty?”
# 	- Constraints
# 		- “Roughly what can be the maximum size of the array?”

# 3. State the core idea in plain language
# “I’ll maintain two pointers: low and high, representing the current search range. While the range is valid, I’ll:
# 	- Compute the middle index
# 	- Compare arr[mid] with the target
# 		- If it matches, return mid
# 		- If arr[mid] is less than target, discard the left half (move low to mid + 1)
# 		- If arr[mid] is greater than target, discard the right half (move high to mid - 1)
# 		- If the loop ends without a match, I’ll return -1.”

# 4. Time and space complexity
# “Each step halves the search space, so the time complexity is O(log n).
# I’ll implement it iteratively, so the space complexity is O(1).
# If I used recursion, there’d be an additional O(log n) call stack space.”

# 5. Choose iterative vs recursive
# “I’ll use an iterative implementation:
# 	- It avoids stack overflow for very large arrays.
# 	- It’s typically clearer and uses constant space.”

# But if they’re into recursion, say:
# 	- “I can also write it recursively if you prefer; the logic is the same, just expressed as a function that recurses on either the left or right half.”

# 6. Confirm and then code
# “If this approach makes sense, I’ll go ahead and implement the iterative version that returns the index of any occurrence of the target, or -1 if it’s not found.”


def binary_search_iterative(arr, target):
	low, high = 0, len(arr) - 1

	while low <= high:
		mid = low + (high - low) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	return -1


arr = [1, 3, 5, 7, 9]
print(binary_search_iterative(arr, 5))
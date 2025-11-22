# Implement Linear Search (transposing)
#    Explanation: Scan array sequentially to find target.
#    Example: [4,2,7,1,9], target=7 → index=2

# 1. Restate the problem clearly
# “We need to search for a target value inside a list by scanning elements one by one, and when it is found then swap the place with the immediate element,
 # and return the index where it appears before/after the swap.”

# 2. Clarify the requirements
# - Are we allowed to modify the array in-place?
# - When I find the target and move it, should I return its new index after reordering, or the original index where it was found?
# - What about duplicates?
# - Can I assume the array is a valid list and that equality comparison for its elements is well-defined?

# 3. Define the expected time/space complexity
# “Since we must check each element until we find the target, the worst-case time complexity is O(n). Space complexity is O(1) because we only use constant extra memory.”

# 4. Outline the step-by-step logic in plain language
# - Start from index 0.
# - Compare current element with the target.
# - If it matches → return its index.
# - Otherwise move to the next element.
# - If we reach the end → return indication of 'not found'.

# 5. Discuss edge cases
# - Empty array → return “not found”.
# - Target appears multiple times → decide what to return (usually first).
# - Target is at index 0 → early exit.
# - Large arrays → still O(n), discuss expectations.

# 6. Optional: Compare alternatives briefly
# “Linear search is optimal only for unsorted arrays. If the array was sorted, I’d use binary search to get O(log n).”

# 7. Offer to start coding only after alignment
# “If the above approach looks correct to you, I’ll start implementing it.”

def linear_search_transpose(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			if i > 0:
				arr[i], arr[i-1] = arr[i-1], arr[i]
				return i-1
			return i
	return -1


arr = [4, 2, 7, 1, 9]
target = 7
print(linear_search_transpose(arr, target))
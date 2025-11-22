# Implement Bubble Sort 
# 	Explanation: Swap adjacent out-of-order elements repeatedly. 
# 	Example: [5,1,4,2,8] → [1,2,4,5,8]

# 1. Restate the Problem
# 	“We need to sort an array by repeatedly comparing adjacent elements 
# 		and swapping them if they are in the wrong order. This process continues until the array is fully sorted.”

# 2. Clarify Requirements
# 	1. Sorting Order
# 		“Should I sort in ascending or descending order?”
# 	2. In-place or returning a new array
# 		“Do you want the sort to be in-place, or should I return a new sorted list?”
# 	3. Input constraints
# 		“What is the expected range of the array size?”
# 		“Are elements guaranteed to be comparable? Integers only or mixed types?”
# 	4. Stability
# 		“Do you require a stable sort? Bubble Sort is naturally stable.”

# 3. Outline the Core Idea (Plain Language, No Code)
# 	“I’ll repeatedly traverse the array.
# 	On each pass, I compare adjacent elements and swap them if they’re out of order.
# 	After each pass, the largest remaining element will ‘bubble up’ to its correct position at the end of the array.
# 	I continue this until a pass completes with no swaps, which means the array is sorted.”

# 4. Discuss Possible Optimizations
# 	1. Early Stopping
# 		“If during a pass no swaps occur, the array is already sorted, and I can exit early.”
# 	2. Reduce the inner loop range
# 		“After each pass, the last element is in correct position, so I don’t need to inspect it again.”

# 5. Talk About Complexity
# 	1. Time Complexity
# 		Worst: O(n²)
# 		Average: O(n²)
# 		Best (already sorted + early stopping): O(n)
	
# 	2. Space Complexity
# 		O(1) (in-place, no extra data structures)
# 		Stability: Bubble Sort is stable, which is a good point to mention.

# 6. Edge Cases to Consider
# 	- Empty array → “already sorted”
# 	- Single element → “already sorted”
# 	- Array already sorted (should quickly detect)
# 	- Array sorted in reverse order (worst case)
# 	- Duplicate elements (should maintain stability)
# 	- Arrays with negative numbers or mixed values

# 7. Confirm and Then Code
# 	“If this approach sounds good to you, I’ll implement an in-place, stable Bubble Sort with early exit optimization.”


def bubble_sort(arr):
	n = len(arr)

	for i in range(n):
		swapped = False

		for j in range(0, n - i - 1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		if not swapped:
			break

	return arr


arr = [1, 2, 4, 5, 8]
bubble_sort(arr)
print(arr)


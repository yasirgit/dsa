# 1. Restate the Problem
# 	“We need to sort an array using a divide-and-conquer approach:
# 		1. split the array into two halves,
# 		2. recursively sort each half, and
# 		3. merge the sorted halves into a fully sorted array.”

# 2. Clarify Requirements
# 	1. “Ascending or descending order?”
# 	2. “Is using additional space acceptable? Standard Merge Sort uses O(n) auxiliary space.”
# 	3. “Do you need the sort to be stable? Merge Sort is naturally stable.”
# 	4. “Are there any constraints on array size or data types?”

# 3. Explain the Merge Sort Strategy
# 	“I’ll use a divide-and-conquer approach:
# 		- If the array has 0 or 1 elements, it’s already sorted.
# 		- Otherwise, I split the array into two halves.
# 		- I recursively sort each half.
# 		- Then I merge the two sorted halves using a two-pointer approach.
# 	Merging is the key step: I compare the smallest remaining elements in each half and build the sorted result.”

# 4. Describe the Merge Process (Very Important)
# 	“During the merge step, I maintain two pointers —
# 	one for the left half and one for the right half.
# 	I compare their values, insert the smaller one into a result list,
# 	and advance that pointer.

# 	Once one side is exhausted, I append the remaining elements from the other side.”

# 5. Discuss Complexity
# 	Time Complexity:
# 		“O(n log n) —
# 		log n levels of recursion,
# 		and O(n) work to merge at each level.”

# 	Space Complexity:
# 		“O(n) auxiliary space for merge arrays.
# 		Recursive stack is O(log n).
# 		So overall: O(n) space.”

# 6. Walk Through Edge Cases
# 	Demonstrate thoroughness:
# 	Empty array
# 	Single element array
# 	Already sorted input
# 	Reverse sorted input
# 	All duplicates
# 	Mixed types (if allowed)
# 	Large array requiring many merge steps

# 7. Choose Recursion or Iterative (Bottom-Up)
# 	“I’ll implement the classic recursive top-down version unless you prefer bottom-up, iterative Merge Sort.”

# 8. Confirm Before Coding
# 	“If this approach looks correct, I’ll go ahead and implement the recursive version with a standard merge function that uses two pointers.”

# Recursive Approach
# Time: O(n log n)
# Space: O(n)

def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge(left, right)


def merge(left, right):
	merged = []
	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1

	merged.extend(left[i:])
	merged.extend(right[j:])

	return merged


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [3, 9, 10, 27, 38, 43, 82]
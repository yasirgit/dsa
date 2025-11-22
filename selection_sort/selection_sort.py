# 1. Restate the Problem
# 	“We need to sort the array by repeatedly selecting the minimum element 
# 	from the unsorted part and swapping it with the first unsorted position. After each pass, the sorted region grows by one element.”

# 2. Clarify Requirements
# 	1. Sorting Order
# 		“Should the array be sorted in ascending or descending order?”
# 	2. In-place vs returning new list
# 		“Should I modify the array in-place, or return a new sorted array?”
# 	3. Data type constraints
# 		“Are all elements comparable — integers only, or possibly strings or custom objects?”
# 	4. Stability requirement
# 		“Should the sort be stable? Selection Sort is not stable by default unless modified.”

# 3. Describe the Core Idea in Plain Language
# 	- “I’ll maintain two parts of the array:
# 		- a sorted section at the front
# 		- an unsorted section in the remainder

# 	- For each index i from 0 to n-1:
# 		- I scan the unsorted region to find the minimum element
# 		- Then I swap that minimum with the element at position i

# After each iteration, the smallest remaining element is placed in its final sorted position.”

# 4. Mention Complexity & Tradeoffs
# 	Time Complexity
# 		Best: O(n²)
# 		Average: O(n²)	
# 		Worst: O(n²)

# 	Space Complexity
# 		O(1) → In-place sorting.

# 	Stability
# 		Not stable, because swapping can reorder equal elements.

# 5. Edge Cases to Consider
# 	- State what your implementation will handle:
# 		- Empty array
# 		- Single element array
# 		- Already sorted array
# 		- Reverse sorted array
# 		- Array with duplicate values (and how swaps affect stability)

# 6. Confirm Before Coding
# 	“If this approach sounds good, I can implement an in-place Selection Sort that finds the minimum on each pass and swaps it to the front.”

def selection_sort(arr):
	n = len(arr)

	for i in range(n):
		min_element_index = i

		for j in range(i+1, n):
			if arr[j] < arr[min_element_index]:
				min_element_index = j

		arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

	return arr

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
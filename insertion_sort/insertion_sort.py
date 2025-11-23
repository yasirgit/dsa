# 1. Restate the Problem
# 	“We want to sort the array by progressively building a sorted portion at the beginning. 
# 	For each element, we insert it into the correct position within the already-sorted prefix by shifting larger elements to the right.”

# 2. Clarify Requirements
# 	- “Should the array be sorted in ascending order?”
# 	- “Do you expect an in-place sort, or should I return a new sorted list?”
# 	- “Do you require the sort to be stable? Insertion Sort is stable.”
# 	- “Any constraints on the size of the array or element types? Are all elements comparable?”

# 3. Explain the Core Idea (Plain Language)
# 	“I treat the first element as a sorted subarray.
# 	Then for each subsequent element, I compare it with elements in the sorted portion and shift those elements to the right until 
# 	I find the correct position for the current element.
# 	Then I insert it there.
# 	Over time, the sorted portion grows until the whole array is sorted.”

# 4. Emphasize the Two-Pointer Logic
# 	“I’ll use two pointers:
# 		- one iterates through the array (i)
# 		- the other shifts elements inside the sorted prefix (j).”

# 5. Talk About Complexity
# 	Time Complexity
# 		- Best: O(n) (already sorted)
# 		- Average: O(n²)
# 		- Worst: O(n²) (reverse sorted)
# 	Space Complexity
# 		- O(1) (in-place)
# 	Stability
# 		- Stable (important to mention)

# 6. Mention Why Insertion Sort Can Be Good
# 	Even though it’s O(n²), you can show nuanced thinking:
# 		- Good for nearly sorted data
# 		- Used by Python's Timsort for small runs
# 		- Low overhead
# 		- Stable and adaptive

# 7. Edge Cases
# 	Show you’ve thought about correctness:
# 		- Empty array
# 		- Single element array
# 		- Already sorted
# 		- Reverse sorted (worst case)
# 		- Duplicate values
# 		- Negative numbers or mixed integers

# 8. Confirm Before Coding
# 	“If this approach sounds correct, I’ll implement an in-place, stable Insertion Sort that uses two pointers to insert each element into the sorted prefix.”

def insertion_sort(arr):
	n = len(arr)

	for i in range(1, n):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j -= 1

		arr[j+1] = key

	return arr



arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)   # [5, 6, 11, 12, 13]
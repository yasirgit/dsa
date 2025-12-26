# 1. Restate the problem
# 	“We want to sort an array using Quick Sort:
# 	pick a pivot, partition the array so that elements less than the pivot are on the left and greater are on the right, 
# 	then recursively sort the left and right partitions.”

# 2. Clarify requirements
# 	- “Should I sort in ascending order?”
# 	- “Is an in-place implementation preferred, or can I use extra arrays?”
# 	- “Are you okay with a simple pivot choice (like last element or middle element), or would you prefer a randomized pivot?”
# 	- “Are all elements comparable? Any special constraints like many duplicates?”
# 	- “Do you need a stable sort? Standard in-place Quick Sort is not stable.”

# 3. Explain the high-level algorithm
# 	“Quick Sort is a divide-and-conquer algorithm:
# 		- If the array has 0 or 1 elements, it’s already sorted.
# 		- Otherwise, I choose a pivot.
# 		- I partition the array: items less than the pivot go to one side, items greater than the pivot to the other side.
# 		- The pivot ends up in its final sorted position.
# 		- Then I recursively sort the left and right subarrays around the pivot.”

# 4. Describe the partitioning strategy (very important)
# 	“I’ll use a partition function:
# 		- Choose the last element as the pivot.
# 		- Maintain an index i that marks the boundary between elements less than the pivot and the rest.
# 		- Iterate with index j through the array (except the pivot):
# 		- When I find an element less than or equal to the pivot, I swap it with the element at i and increment i.
# 		- At the end, I swap the pivot into position i; that’s its correct sorted position.
# 		- I return i as the partition index.”


def quick_sort(arr):
	def partition(low, high):
		pivot = arr[high]
		i = low - 1

		for j in range(low, high):
			if arr[j] <= pivot:
				 i += 1
				 arr[i], arr[j] = arr[j], arr[i]

		arr[i+1], arr[high] = arr[high], arr[i+1]

		return i + 1

	def quick_sort_recursive(low, high):
		if low < high:
			p = partition(low, high)
			quick_sort_recursive(low, p-1)
			quick_sort_recursive(p+1, high)


	quick_sort_recursive(0, len(arr) - 1)

	return arr
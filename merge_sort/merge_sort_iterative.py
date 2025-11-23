def merge_sort_iterative(arr):
	n = len(arr)
	width = 1

	while width < n:
		for i in range(0, n, 2 * width):
			left = arr[i : i + width]
			right = arr[i + width : i + 2 * width]
			arr[i : i + 2 * width] = merge(left, right)
		width *= 2

	return arr


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
merge_sort_iterative(arr)
print(arr)  # [3, 9, 10, 27, 38, 43, 82]
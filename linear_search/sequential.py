# Implement Linear Search
#    Explanation: Scan array sequentially to find target.
#    Example: [4,2,7,1,9], target=7 → index=2

# 1. Restate the problem clearly
# “We need to search for a target value inside a list by scanning elements one by one and return the index where it appears.”

# 2. Clarify the requirements
# - Should I return the index or a boolean?
# - What should I do if the target doesn't exist? Return -1? None?
# - Can the array contain duplicates? If yes, return first or all occurrences?
# - Is the data structure strictly an array/list, or could it be a linked list?
# - Are there constraints on input size? (Important for bigger problems)

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

def linear_search(arr, target):
   for i in range(len(arr)):
      if arr[i] == target:
         return i
   return -1


arr = [4, 2, 7, 1, 9]
target = 7
print(linear_search(arr, target))
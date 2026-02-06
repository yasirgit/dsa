def moveZeroes(nums):
    # This pointer keeps track of where the next non-zero element goes
    lastNonZeroFoundAt = 0
    
    # Step 1: Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroFoundAt] = nums[i]
            lastNonZeroFoundAt += 1
            
    # Step 2: Fill the remaining positions with zeros
    for i in range(lastNonZeroFoundAt, len(nums)):
        nums[i] = 0
        
    return nums

# Example
example = [0, 1, 0, 3, 12]
print(moveZeroes(example)) # Output: [1, 3, 12, 0, 0]
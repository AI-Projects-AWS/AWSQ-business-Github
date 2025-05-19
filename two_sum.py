    num_map = {}  # To store number and its index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        
    
    return []  # If no solution is found

# Example usage
if __name__ == "__main__":
    # Example 1: Basic usage
    nums = [2, 7, 11, 15]
    target = 9
    try:
        result = two_sum(nums, target)
        print(f"Example 1: Indices of numbers that add up to {target}: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    
    # Example 2: No solution
    nums = [1, 2, 3, 4]
    target = 10
    try:
        result = two_sum(nums, target)
        if result:
            print(f"Example 2: Indices of numbers that add up to {target}: {result}")
        else:
            print(f"Example 2: No solution found for target {target}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    
    # Example 3: Error handling
    try:
        result = two_sum([], 5)
        print(f"Result: {result}")
    except (TypeError, ValueError) as e:
        print(f"Example 3: Caught expected error - {e}")
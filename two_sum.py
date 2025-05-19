from typing import List, Optional

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns the indices of the two numbers in `nums` that add up to `target`.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[int]: Indices of the two numbers that add up to the target.
        Returns an empty list if no solution is found.
        
    Raises:
        TypeError: If nums is not a list or target is not an integer.
        ValueError: If nums is empty or contains non-integer values.
    """
    # Input validation
    if nums is None:
        raise TypeError("Input 'nums' cannot be None")
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list")
    if not nums:
        raise ValueError("Input 'nums' cannot be empty")
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in 'nums' must be integers")
    if not isinstance(target, int):
        raise TypeError("Input 'target' must be an integer")
    
    num_map = {}  # To store number and its index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
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
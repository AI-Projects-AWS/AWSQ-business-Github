# Two Sum Problem Solution

This repository contains a Python implementation of the "Two Sum" problem, a common coding interview question.

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Solution

The solution uses a hash map approach with O(n) time complexity and O(n) space complexity:

1. Iterate through the array once
2. For each element, check if its complement (target - current element) exists in the hash map
3. If found, return the indices of the current element and its complement
4. If not found, add the current element and its index to the hash map
5. If no solution is found after iterating through the array, return an empty list

## Usage

```python
from two_sum import two_sum

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
```

## Running Tests

The repository includes comprehensive unit tests. To run the tests:

```bash
python -m unittest test_two_sum.py
```

## Function Documentation

```python
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
```
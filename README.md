# Two Sum Problem Solution

This repository contains a Python implementation of the "Two Sum" problem, a common coding interview question. The implementation provides an efficient solution with comprehensive error handling and test coverage.

## Repository Structure

The repository consists of the following files:

- **two_sum.py**: Contains the main implementation of the Two Sum algorithm
- **test_two_sum.py**: Comprehensive unit tests for the Two Sum function
- **README.md**: Documentation about the repository and how to use the code

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Solution Approach

The solution uses a hash map approach with O(n) time complexity and O(n) space complexity:

1. Iterate through the array once
2. For each element, check if its complement (target - current element) exists in the hash map
3. If found, return the indices of the current element and its complement
4. If not found, add the current element and its index to the hash map
5. If no solution is found after iterating through the array, return an empty list

This approach is significantly more efficient than the brute force method (which would be O(n²)) as it requires only a single pass through the array.

## Installation

### Prerequisites

- Python 3.6 or higher

### Cloning the Repository

To clone this repository to your local machine, run:

```bash
git clone https://github.com/yourusername/two-sum-solution.git
cd two-sum-solution
```

No additional dependencies are required to run the code.

## Usage

### Basic Usage

```python
from two_sum import two_sum

# Example 1: Basic usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] (indices of 2 and 7)

# Example 2: When no solution exists
nums = [1, 2, 3, 4]
target = 10
result = two_sum(nums, target)
print(result)  # Output: [] (empty list)
```

### Error Handling

The function includes comprehensive error handling:

```python
# Example 3: Error handling
try:
    result = two_sum([], 5)  # Empty list
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Input 'nums' cannot be empty

try:
    result = two_sum([1, 2, "3"], 5)  # Non-integer in list
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: All elements in 'nums' must be integers
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

## Running Tests

The repository includes comprehensive unit tests covering various scenarios including:
- Basic functionality
- Edge cases
- Error handling
- Performance with large inputs

To run the tests:

```bash
python -m unittest test_two_sum.py
```

Or to run a specific test:

```bash
python -m unittest test_two_sum.TestTwoSum.test_basic_case
```

## Contributing

Contributions to improve the implementation or extend the test coverage are welcome. Please feel free to submit a pull request or open an issue to discuss potential improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
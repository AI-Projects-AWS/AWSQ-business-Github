# Two Sum Problem Solution

This repository contains a Python implementation of the "Two Sum" problem, a common coding interview question. The implementation provides an efficient solution with comprehensive error handling and test coverage.

## Repository Structure

The repository consists of the following files:

- **two_sum.py**: Contains the main implementation of the Two Sum algorithm
- **test_two_sum.py**: Comprehensive unit tests for the Two Sum function
- **three_sum.java**: Java implementation of the Three Sum problem
- **security_scanner.py**: Security scanner for code repositories
- **test_security_scanner.py**: Unit tests for the security scanner
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

## Extended Functionality: Finding All Pairs

In addition to the original `two_sum` function that returns the first pair found, this repository also includes a `two_sum_all_pairs` function that returns all pairs of indices where the corresponding numbers add up to the target.

The extended solution maintains the same efficient approach:
1. Build a hash map of values to their indices (handling duplicates)
2. Iterate through the array and find all pairs that add up to the target
3. Return a list of all unique pairs found

## Security Scanner

The repository includes a security scanner that can identify potential security issues in Python and Java code. The scanner checks for common security vulnerabilities such as:

- Use of dangerous functions (eval, exec)
- Hardcoded credentials
- Insecure file operations
- Use of deprecated/insecure methods
- Potential for denial of service

### Using the Security Scanner

To scan your code for security issues:

```bash
python security_scanner.py -p /path/to/your/code
```

This will generate:
- A JSON report (security_report.json)
- An HTML report (security_report.html)
- A log file (security_scan.log)
- A summary in the console

#### Command Line Options

```
usage: security_scanner.py [-h] [-p PATH] [-j JSON] [-H HTML] [-v]

Security Scanner for Code Repositories

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the repository to scan
  -j JSON, --json JSON  Path to the JSON report output file
  -H HTML, --html HTML  Path to the HTML report output file
  -v, --verbose         Enable verbose output
```

### Running Security Scanner Tests

To run the tests for the security scanner:

```bash
python -m unittest test_security_scanner.py
```

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

### Finding All Pairs

```python
from two_sum import two_sum_all_pairs

# Example: Finding all pairs that add up to the target
nums = [2, 7, 11, 15, 2, 7]
target = 9
result = two_sum_all_pairs(nums, target)
print(result)  # Output: [[0, 1], [4, 5]] (indices of all pairs of 2 and 7)
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

```python
def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Returns all pairs of indices of the numbers in `nums` that add up to `target`.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[List[int]]: List of index pairs where each pair contains the indices of 
        two numbers that add up to the target. Returns an empty list if no solution is found.
        
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

To run tests for the extended functionality:

```bash
python -m unittest test_two_sum.TestTwoSumAllPairs
```

## Contributing

Contributions to improve the implementation or extend the test coverage are welcome. Please feel free to submit a pull request or open an issue to discuss potential improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
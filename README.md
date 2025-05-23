# Two Sum and Three Sum Problem Solutions

This repository contains implementations of the "Two Sum" problem in Python and the "Three Sum" problem in Java, both common coding interview questions. The implementations provide efficient solutions with comprehensive error handling and test coverage.

## Repository Structure

The repository consists of the following files:

- **two_sum.py**: Contains the main implementation of the Two Sum algorithm in Python
- **test_two_sum.py**: Comprehensive unit tests for the Two Sum function
- **three_sum.java**: Contains the implementation of the Three Sum algorithm in Java
- **README.md**: Documentation about the repository and how to use the code

## Problem Description

### Two Sum Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Three Sum Problem

Given an array of integers `nums`, find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

## Solution Approach

### Two Sum Solution

The Two Sum solution uses a hash map approach with O(n) time complexity and O(n) space complexity:

1. Iterate through the array once
2. For each element, check if its complement (target - current element) exists in the hash map
3. If found, return the indices of the current element and its complement
4. If not found, add the current element and its index to the hash map
5. If no solution is found after iterating through the array, return an empty list

This approach is significantly more efficient than the brute force method (which would be O(n²)) as it requires only a single pass through the array.

### Three Sum Solution

The Three Sum solution uses a sorting and two-pointer approach with O(n²) time complexity:

1. Sort the input array (O(n log n))
2. Iterate through the array with a fixed pointer (i)
3. For each position i, use two pointers (left and right) to find pairs that sum to the negative of nums[i]
4. Skip duplicate values to avoid duplicate triplets
5. Return all unique triplets that sum to zero

This approach is more efficient than the brute force method (which would be O(n³)) and handles the requirement of not having duplicate triplets in the result.

## Extended Functionality: Finding All Pairs

In addition to the original `two_sum` function that returns the first pair found, this repository also includes a `two_sum_all_pairs` function that returns all pairs of indices where the corresponding numbers add up to the target.

The extended solution maintains the same efficient approach:
1. Build a hash map of values to their indices (handling duplicates)
2. Iterate through the array and find all pairs that add up to the target
3. Return a list of all unique pairs found

## Installation

### Prerequisites

- Python 3.6 or higher (for Two Sum)
- Java 8 or higher (for Three Sum)

### Cloning the Repository

To clone this repository to your local machine, run:

```bash
git clone https://github.com/yourusername/sum-problems-solution.git
cd sum-problems-solution
```

No additional dependencies are required to run the code.

## Usage

### Two Sum Usage

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

### Finding All Pairs with Two Sum

```python
from two_sum import two_sum_all_pairs

# Example: Finding all pairs that add up to the target
nums = [2, 7, 11, 15, 2, 7]
target = 9
result = two_sum_all_pairs(nums, target)
print(result)  # Output: [[0, 1], [4, 5]] (indices of all pairs of 2 and 7)
```

### Three Sum Usage

```java
// Compile the Java file
javac three_sum.java

// Run the program
java three_sum
```

Example output:
```
Example 1 Input: [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2 Input: [0, 0, 0]
Output: [[0, 0, 0]]

Example 3 Input: [-2, 0, 1, 1, 2]
Output: [[-2, 0, 2], [-2, 1, 1]]
```

To use the Three Sum implementation in your own Java code:

```java
import java.util.*;

public class YourClass {
    public static void main(String[] args) {
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> result = three_sum.threeSum(nums);
        System.out.println(result);
    }
}
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

### Two Sum Functions

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

### Three Sum Function

```java
/**
 * Finds all unique triplets in the array which sum to zero.
 * 
 * @param nums The input array of integers
 * @return A list of lists, where each inner list contains three integers that sum to zero
 */
public static List<List<Integer>> threeSum(int[] nums)
```

## Running Tests

### Testing Two Sum Implementation

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

### Testing Three Sum Implementation

The Three Sum implementation includes example test cases in the main method. To run these tests:

```bash
javac three_sum.java
java three_sum
```

This will compile and run the Java program, which includes several test cases demonstrating the functionality of the Three Sum solution.

## Contributing

Contributions to improve the implementation or extend the test coverage are welcome. Please feel free to submit a pull request or open an issue to discuss potential improvements.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
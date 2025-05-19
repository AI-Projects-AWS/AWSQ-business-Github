import unittest
from two_sum import two_sum, two_sum_all_pairs

class TestTwoSum(unittest.TestCase):
    def test_basic_case(self):
        """Test the basic case where a solution exists."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]  # Indices of 2 and 7
        self.assertEqual(two_sum(nums, target), expected)
    
    def test_different_order(self):
        """Test with numbers in a different order."""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]  # Indices of 2 and 4
        self.assertEqual(two_sum(nums, target), expected)
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers in the list."""
        nums = [3, 3, 2, 4]
        target = 6
        expected = [0, 2]  # Indices of 3 and 3
        self.assertEqual(two_sum(nums, target), expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]  # Indices of -3 and -5
        self.assertEqual(two_sum(nums, target), expected)
    
    def test_no_solution(self):
        """Test when no solution exists."""
        nums = [1, 2, 3, 4]
        target = 10
        expected = []  # No solution
        self.assertEqual(two_sum(nums, target), expected)
    
    def test_none_input(self):
        """Test with None input."""
        with self.assertRaises(TypeError):
            two_sum(None, 5)
    
    def test_empty_list(self):
        """Test with an empty list."""
        with self.assertRaises(ValueError):
            two_sum([], 5)
    
    def test_non_list_input(self):
        """Test with a non-list input."""
        with self.assertRaises(TypeError):
            two_sum("not a list", 5)
    
    def test_non_integer_elements(self):
        """Test with non-integer elements in the list."""
        with self.assertRaises(ValueError):
            two_sum([1, 2, "3", 4], 5)
    
    def test_non_integer_target(self):
        """Test with a non-integer target."""
        with self.assertRaises(TypeError):
            two_sum([1, 2, 3, 4], "5")
    
    def test_large_list(self):
        """Test with a large list."""
        nums = list(range(1000))
        target = 1500
        expected = [501, 999]  # Indices of 501 and 999
        self.assertEqual(two_sum(nums, target), expected)

class TestTwoSumAllPairs(unittest.TestCase):
    def test_basic_case(self):
        """Test the basic case where a single solution exists."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [[0, 1]]  # Indices of 2 and 7
        self.assertEqual(two_sum_all_pairs(nums, target), expected)
    
    def test_multiple_solutions(self):
        """Test with multiple solutions."""
        nums = [2, 7, 11, 15, 2, 7]
        target = 9
        # Expected pairs: (2,7) at indices (0,1) and (4,5)
        expected = [[0, 1], [4, 5]]
        result = two_sum_all_pairs(nums, target)
        # Sort the result for consistent comparison
        result.sort()
        self.assertEqual(result, expected)
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers that form multiple pairs."""
        nums = [3, 3, 2, 4, 3, 3]
        target = 6
        # Expected pairs: (3,3) at indices (0,1), (0,4), (0,5), (1,4), (1,5), (4,5)
        # and (2,4) at indices (2,3)
        expected = [[0, 1], [0, 4], [0, 5], [1, 4], [1, 5], [2, 3], [4, 5]]
        result = two_sum_all_pairs(nums, target)
        # Sort the result for consistent comparison
        result.sort()
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3, -4, -5, -3]
        target = -8
        # Expected pairs: (-3,-5) at indices (2,4) and (5,4)
        expected = [[2, 4], [4, 5]]
        result = two_sum_all_pairs(nums, target)
        # Sort the result for consistent comparison
        result.sort()
        self.assertEqual(result, expected)
    
    def test_no_solution(self):
        """Test when no solution exists."""
        nums = [1, 2, 3, 4]
        target = 10
        expected = []  # No solution
        self.assertEqual(two_sum_all_pairs(nums, target), expected)
    
    def test_none_input(self):
        """Test with None input."""
        with self.assertRaises(TypeError):
            two_sum_all_pairs(None, 5)
    
    def test_empty_list(self):
        """Test with an empty list."""
        with self.assertRaises(ValueError):
            two_sum_all_pairs([], 5)
    
    def test_non_list_input(self):
        """Test with a non-list input."""
        with self.assertRaises(TypeError):
            two_sum_all_pairs("not a list", 5)
    
    def test_non_integer_elements(self):
        """Test with non-integer elements in the list."""
        with self.assertRaises(ValueError):
            two_sum_all_pairs([1, 2, "3", 4], 5)
    
    def test_non_integer_target(self):
        """Test with a non-integer target."""
        with self.assertRaises(TypeError):
            two_sum_all_pairs([1, 2, 3, 4], "5")
    
    def test_large_list_with_multiple_solutions(self):
        """Test with a large list that has multiple solutions."""
        # Create a list with multiple pairs that sum to the target
        nums = list(range(100))
        nums.extend([50, 50])  # Add duplicates to create multiple solutions
        target = 100
        
        # Calculate expected result
        result = two_sum_all_pairs(nums, target)
        
        # Verify that the result contains the expected pairs
        self.assertIn([50, 50], result)  # Indices of the two 50s we added
        self.assertIn([1, 99], result)   # Indices of 1 and 99
        self.assertIn([2, 98], result)   # Indices of 2 and 98
        
        # Verify the total number of pairs
        # For numbers 0-99, pairs should be (1,99), (2,98), ..., (49,51)
        # Plus the pair of the two 50s we added
        self.assertEqual(len(result), 50)

if __name__ == "__main__":
    unittest.main()
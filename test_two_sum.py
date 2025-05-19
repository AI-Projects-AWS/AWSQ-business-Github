import unittest
from two_sum import two_sum

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

if __name__ == "__main__":
    unittest.main()
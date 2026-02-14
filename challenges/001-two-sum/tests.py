import unittest
from solution import two_sum


class TestTwoSum(unittest.TestCase):
    """Test cases for two_sum function"""
    
    def test_example_case(self):
        """Test basic example from problem"""
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
    
    def test_unsorted_array(self):
        """Test with unsorted array"""
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(two_sum([-1, -2, -3, -4], -6), (1, 3))
    
    def test_large_numbers(self):
        """Test with large numbers"""
        result = two_sum([1000000, 2000000, 3000000], 5000000)
        self.assertEqual(result, (1, 2))
    
    def test_no_solution(self):
        """Test when no solution exists"""
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)


if __name__ == "__main__":
    unittest.main()

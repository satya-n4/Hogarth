import unittest
from main import sort_odd_numbers

class TestSortOddNumbers(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sort_odd_numbers([]), [])

    def test_only_even_numbers(self):
        self.assertEqual(sort_odd_numbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_only_odd_numbers(self):
        self.assertEqual(sort_odd_numbers([5, 3, 9, 1]), [1, 3, 5, 9])

    def test_mixed_numbers(self):
        self.assertEqual(sort_odd_numbers([10, 7, 2, 9, 4]), [10, 7, 2, 9, 4])

    def test_large_numbers(self):
        self.assertEqual(sort_odd_numbers([100, 23, 67, 45, 89]), [100, 23, 45, 67, 89])

if __name__ == '__main__':
    unittest.main()

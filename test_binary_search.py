import unittest
from binary_search import binary_search, create_list, print_list

class TestBinarySearch(unittest.TestCase):
    """Tests for binary search class"""

    def setUp(self):
        """Creating a list to reuse it in all functions"""
        self.binary_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
        self.item = 25
        self.count= 4
        self.value = 11
        self.string_value = 'false case'

    def test_binary_search(self):
        result = binary_search(self.binary_list, 25)
        self.assertEqual(result, f"\nNumber {self.item} found at the step {self.count}" )

    def test_create_list(self):
        new_list = create_list(self.value)
        self.assertEqual(self.binary_list, new_list)

    def test_fail_create_list(self):
        fail_case = create_list(self.string_value)
        self.assertTrue(fail_case)
        self.assertTrue(1)

if __name__ == '__main__':
    unittest.main()

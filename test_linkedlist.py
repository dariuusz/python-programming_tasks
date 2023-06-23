import unittest
from linkedlist import middle_element, create_dictionary, dictionary_length

class TestLinkedList(unittest.TestCase):
    """Test for finding middle element/s in a dictionary."""

    def setUp(self):
        """Creating a default variables for test cases."""
        self.odd_dictionary = {'a': [1, 2], 'b': [1], 'c': [1, 2]} 
        self.even_dictionary = {'a': [1, 2], 'b': [1], 'c': [1, 2], 'd': [1]}
        self.create_odd_dic = {'a': []}
        self.create_even_dic = {'a': []}
        self.create_list = ['a', 'b']

    def test_dictionary_length(self):
        """Test case for a length of a dictionary."""
        self.assertEqual(dictionary_length(self.odd_dictionary), [ 2 , 0 ])
        self.assertEqual(dictionary_length(self.even_dictionary), [ 2 , 3 ])

    def test_create_dictionary(self):
        """Test case for creating a dictionary"""
        result1 = create_dictionary(self.create_odd_dic, self.odd_dictionary)
        result2 = create_dictionary(self.create_even_dic, self.even_dictionary)
        self.assertEqual(result1, self.odd_dictionary)
        self.assertEqual(result2, self.even_dictionary)

    def test_middle_element(self):
        """Test for finding a middle element/s."""
        odd_mid_elem = [('b', [1])]
        even_mid_elem = [('b', [1]), ('c', [1, 2])]
        self.assertEqual(middle_element(self.odd_dictionary), odd_mid_elem)
        self.assertEqual(middle_element(self.even_dictionary), even_mid_elem)

if __name__ == '__main__':
    unittest.main()
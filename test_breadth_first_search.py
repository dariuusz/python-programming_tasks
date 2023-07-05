import unittest
from breadth_first_search import capitalize_dictionary, create_dictionary, search_dictionary

class TestBreadthFirstSearch(unittest.TestCase):
    """Test for breadth first search algorithm."""

    def setUp(self):
        """Creating default dictionary."""
        self.dictionary = {'darek': ['marek', 'jarek'], 'marek': ['ania'],\
            'ania': ['inka', 'agnieszka'],\
            'julka': []}
        self.empty_dictionary = {'darek': []}
        self.false_dictionary = {'darek': [], 'marek': ['ania'],\
            'ania': ['inka', 'agnieszka'],\
            'julka': []}
        self.name = 'Marek'
        

    def test_capitalize_dictionary(self):        
        """Test case for dictionary capitalization."""
        self.assertEqual(capitalize_dictionary(self.dictionary), {'Darek': ['Marek', 'Jarek'], 'Marek': ['Ania'],\
            'Ania': ['Inka', 'Agnieszka'],\
            'Julka': []})

    def test_create_dictionary(self):
        """Test case for creating dictionary"""
        result = create_dictionary(self.empty_dictionary, self.dictionary)
        self.assertEqual(result, self.dictionary)
        self.assertNotEqual(result, self.false_dictionary)

    def test_search_dictionary(self):
        """Test case for searching an element"""
        name2 = 'John'
        self.assertIn(self.name, capitalize_dictionary(self.dictionary))
        self.assertNotIn(name2, capitalize_dictionary(self.dictionary))

if __name__ == '__main__':
    unittest.main()
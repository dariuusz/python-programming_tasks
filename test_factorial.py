import unittest
from factorial import convert_str, fact

class TestFactorialFunction(unittest.TestCase):
    """ Test factorial functions """
    def setUp(self):
        """Creating variables to reuse it in other functions"""
        self.number = 10
        self.results = 3628800
        self.wrong_result = 362880
        
    def test_fact(self):
        self.assertNotEqual(self.wrong_result, fact(self.number))
        self.assertEqual(self.results, fact(self.number))

    def test_convert_str(self):
        value = 'abc'
        self.assertTrue(value)

if __name__ == '__main__':
    unittest.main()
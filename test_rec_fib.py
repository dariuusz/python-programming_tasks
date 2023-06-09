import unittest 
from rec_fib import rec_fib, user_inp, pr_fib

class TestFibonacciRecursive(unittest.TestCase):
    """ Tests for fibonacci recursive """

    def test_rec_fib(self):
        self.assertEqual(rec_fib(0),0)
        self.assertEqual(rec_fib(1),1)
        self.assertEqual(rec_fib(2),1)
        self.assertEqual(rec_fib(3),2)
        self.assertEqual(rec_fib(4),3)
        self.assertEqual(rec_fib(5),5)

    def test_user_info(self):
        self.assertTrue(-5)
        self.assertTrue(5)

    def test_rec_fib(self):
        fib_number = rec_fib(4)
        self.assertEqual(fib_number, 3)
        self.assertEqual(rec_fib(10), 55)


if __name__ == '__main__':
    unittest.main()
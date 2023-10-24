'''The unittest module provides testing suite'''
import unittest
from mathTL import MathTL


class Test_sub(unittest.TestCase):
    def test_int(self):
        result = MathTL.sub(5,4)
        self.assertEqual(result, 1)

    def test_float(self):
        result = MathTL.sub(3.4,1.1)
        self.assertEqual(result, 2.3)

    def test_string(self):
        result = MathTL.sub("a", 4)
        self.assertEqual(result, -4)


    #place additional test cases for this function here





if __name__ == '__main__':
    unittest.main()
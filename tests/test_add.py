import unittest 
from mathTL import MathTL
'''
Use this file as a template for your own test if you would like too.
'''

class Test_add(unittest.TestCase):
    def test_int(self):
        result = MathTL.add(3,4)
        self.assertEqual(result, 7)

    def test_float(self):
        result = MathTL.add(3.1,4.5)
        self.assertEqual(result, 7.6)

    def test_string(self):
        result = MathTL.add("a", 4)
        self.assertEqual(result, 4)


    #place additional test cases for this function here





if __name__ == '__main__':
    unittest.main()
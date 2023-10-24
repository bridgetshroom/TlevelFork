import unittest 
from mathTL import MathTL

class Test_add(unittest.TestCase):
    def test_int(self):
        result = MathTL.add(3,4)
        self.assertEqual(result, 7)

    def test_float(self):
        result = MathTL.add(3.1,4.5)
        self.assertEqual(result, 7.6)

if __name__ == '__main__':
    unittest.main()
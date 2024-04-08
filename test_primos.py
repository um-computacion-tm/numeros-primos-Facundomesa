import unittest
from primos import primos

class TestIsPrime(unittest.TestCase):
    def test_with_1(self):
        result = primos(1)
        self.assertFalse(result)
    
    def test_with_2(self):
        result = primos(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = primos(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = primos(4)
        self.assertFalse(result)
    
    def test_with_5(self):
        result = primos(5)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
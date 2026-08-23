import unittest
from common_denominators import convert_fracts

class TestCommonDenominators(unittest.TestCase):

    def test_convert_fracts(self):
        a = []
        b = []
        self.assertEqual(convert_fracts(a), b)
        a = [[1, 2], [1, 3], [1, 4]]
        b = [[6, 12], [4, 12], [3, 12]]
        self.assertEqual(convert_fracts(a), b)

if __name__ == '__main__':
    unittest.main()

import unittest
from calculating_with_functions import (
    two, three, four, five, six, seven, eight, nine,
    plus, minus, times, divided_by
)

class TestCalculatingWithFunctions(unittest.TestCase):

    def test_calculating_with_functions(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)

if __name__ == '__main__':
    unittest.main()

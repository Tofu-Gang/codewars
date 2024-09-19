import unittest
from src.binary_array_to_number import binary_array_to_number


class TestBinaryArrayToNumber(unittest.TestCase):

    def test_binary_array_to_number(self):
        self.assertEquals(binary_array_to_number([0, 0, 0, 1]), 1)
        self.assertEquals(binary_array_to_number([0, 0, 1, 0]), 2)
        self.assertEquals(binary_array_to_number([1, 1, 1, 1]), 15)
        self.assertEquals(binary_array_to_number([0, 1, 1, 0]), 6)


if __name__ == '__main__':
    unittest.main()

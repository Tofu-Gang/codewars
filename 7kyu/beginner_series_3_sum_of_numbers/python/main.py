import unittest
from src.get_sum import get_sum


class TestGetSum(unittest.TestCase):

    def test_get_sum(self):
        self.assertEquals(get_sum(0, 1), 1)
        self.assertEquals(get_sum(0, -1), -1)


if __name__ == '__main__':
    unittest.main()

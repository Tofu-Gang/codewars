import unittest
from src.alphanumeric import alphanumeric


class TestAlphanumeric(unittest.TestCase):

    def test_alphanumeric(self):
        self.assertEquals(alphanumeric("hello world_"), False)
        self.assertEquals(alphanumeric("PassW0rd"), True)
        self.assertEquals(alphanumeric("     "), False)


if __name__ == '__main__':
    unittest.main()

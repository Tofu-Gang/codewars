import unittest
from src.find_next_square import find_next_square


class TestFindNextSquare(unittest.TestCase):

    def test_find_next_square(self):
        # should return the next square for perfect squares
        self.assertEquals(find_next_square(121), 144, "Wrong output for 121")
        self.assertEquals(find_next_square(625), 676, "Wrong output for 625")
        self.assertEquals(find_next_square(319225), 320356, "Wrong output for 319225")
        self.assertEquals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")
        # should return -1 for numbers which aren't perfect squares
        self.assertEquals(find_next_square(155), -1, "Wrong output for 155")
        self.assertEquals(find_next_square(342786627), -1, "Wrong output for 342786627")


if __name__ == '__main__':
    unittest.main()

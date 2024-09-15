import unittest
from src.find_short import find_short


class TestFindShort(unittest.TestCase):

    def test_find_short(self):
        self.assertEquals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEquals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEquals(find_short("lets talk about javascript the best language"), 3)
        self.assertEquals(find_short("i want to travel the world writing code one day"), 1)
        self.assertEquals(find_short("Lets all go on holiday somewhere very cold"), 2)
        self.assertEquals(find_short("Let's travel abroad shall we"), 2)


if __name__ == '__main__':
    unittest.main()

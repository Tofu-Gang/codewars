import unittest
from src.same_structure_as import same_structure_as


class TestSameStructureAs(unittest.TestCase):

    def test_same_structure_as(self):
        self.assertEquals(same_structure_as([1, [1, 1]], [2, [2, 2]]),
                          True, "[1,[1,1]] same as [2,[2,2]]")
        self.assertEquals(same_structure_as([1, [1, 1]], [[2, 2], 2]),
                          False, "[1,[1,1]] not same as [[2,2],2]")


if __name__ == '__main__':
    unittest.main()

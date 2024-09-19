import unittest
from src.solution import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEquals(solution("asdfadsf"), ['as', 'df', 'ad', 'sf'])
        self.assertEquals(solution("asdfads"), ['as', 'df', 'ad', 's_'])
        self.assertEquals(solution(""), [])
        self.assertEquals(solution("x"), ["x_"])


if __name__ == '__main__':
    unittest.main()

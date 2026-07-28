import unittest
from split_strings import solution

class TestSplitStrings(unittest.TestCase):
    _TESTS = (
        ("asdfadsf", ['as', 'df', 'ad', 'sf']),
        ("asdfads", ['as', 'df', 'ad', 's_']),
        ("", []),
        ("x", ["x_"]),
    )

    def test_alphabet_position(self):
        for inp, exp in self._TESTS:
            self.assertEqual(solution(inp), exp)

if __name__ == '__main__':
    unittest.main()

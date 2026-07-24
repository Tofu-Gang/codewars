import unittest
from string_ends_with import solution

class TestStringEndsWith(unittest.TestCase):
    _fixed_tests_True = (
        ("samurai", "ai"),
        ("ninja", "ja"),
        ("sensei", "i"),
        ("abc", "abc"),
        ("abcabc", "bc"),
        ("fails", "ails"),
    )
    _fixed_tests_False = (
        ("sumo", "omo"),
        ("samurai", "ra"),
        ("abc", "abcd"),
        ("ails", "fails"),
        ("this", "fails"),
        ("spam", "eggs")
    )

    def test_solution(self):
        for text, ending in self._fixed_tests_True:
            self.assertEqual(solution(text, ending), True)

        for text, ending in self._fixed_tests_False:
            self.assertEqual(solution(text, ending), False)

if __name__ == '__main__':
    unittest.main()

import unittest
from unique_in_order import unique_in_order

class TestUniqueInOrder(unittest.TestCase):

    def test_unique_in_order(self):
        # Should work with empty sequence
        self.assertEqual(unique_in_order(""), [])
        self.assertEqual(unique_in_order([]), [])
        self.assertEqual(unique_in_order(()), [])
        # Should work with single element sequence
        self.assertEqual(unique_in_order("A"), ["A"])
        self.assertEqual(unique_in_order(["A"]), ["A"])
        self.assertEqual(unique_in_order(("A",)), ["A"])
        # Should reduce duplicates
        self.assertEqual(unique_in_order("AA"), ["A"])
        self.assertEqual(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
        # Should be case-sensitive
        self.assertEqual(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])
        # Should work with different element types
        self.assertEqual(unique_in_order([1, 2, 3, 3, -1]), [1, 2, 3, -1])
        self.assertEqual(unique_in_order(["a", "b", "b", "a"]), ["a", "b", "a"])

if __name__ == '__main__':
    unittest.main()

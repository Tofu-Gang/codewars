import unittest
from src.longest_consec import longest_consec


class TestLongestConsec(unittest.TestCase):

    def test_longest_consec(self):
        self.assertEquals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
        self.assertEquals(
            longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1),
            "oocccffuucccjjjkkkjyyyeehh")
        self.assertEquals(longest_consec([], 3), "")
        self.assertEquals(
            longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
                           2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
        self.assertEquals(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
                           "wlwsasphmxxowiaxujylentrklctozmymu")
        self.assertEquals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
        self.assertEquals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
        self.assertEquals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
        self.assertEquals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")


if __name__ == '__main__':
    unittest.main()

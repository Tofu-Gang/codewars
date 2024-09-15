import unittest
from src.boolean_to_string import boolean_to_string


class TestBooleanToString(unittest.TestCase):

    def test_boolean_to_string(self):
        self.assertEquals(boolean_to_string(True), "True")
        self.assertEquals(boolean_to_string(False), "False")


if __name__ == '__main__':
    unittest.main()

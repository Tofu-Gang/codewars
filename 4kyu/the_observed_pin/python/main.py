import unittest
from src.get_pins import get_pins


class TestGetPins(unittest.TestCase):

    def test_get_pins(self):
        self.assertEquals(sorted(get_pins("8")), sorted(["5", "7", "8", "9", "0"]), 'PIN: ' + "8")
        self.assertEquals(sorted(get_pins("11")), sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"]), 'PIN: ' + "11")
        self.assertEquals(sorted(get_pins("369")), sorted([
                "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
                "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
                "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
            ]), 'PIN: ' + "369")


if __name__ == '__main__':
    unittest.main()

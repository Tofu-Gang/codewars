import unittest
from src.to_camel_case import to_camel_case


class TestCamelCase(unittest.TestCase):

    def test_camel_case(self):
        self.assertEquals(to_camel_case(""), "")
        self.assertEquals(
            to_camel_case("the_stealth_warrior"), "theStealthWarrior")
        self.assertEquals(
            to_camel_case("the-stealth-warrior"), "theStealthWarrior")
        self.assertEquals(
            to_camel_case("The_Stealth_Warrior"), "TheStealthWarrior")
        self.assertEquals(
            to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
        self.assertEquals(
            to_camel_case("The_Stealth-Warrior"), "TheStealthWarrior")
        self.assertEquals(to_camel_case("A-B-C"), "ABC")


if __name__ == '__main__':
    unittest.main()

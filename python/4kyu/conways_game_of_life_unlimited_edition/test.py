import unittest
from conways_game_of_life_unlimited_edition import get_generation

class TestConwaysGameOfLifeUnlimitedEdition(unittest.TestCase):

    def test_get_generation(self):
        one_glider = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ]
        one_glider_expected = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
        one_glider_actual = get_generation(one_glider, 1)
        self.assertEqual(one_glider_actual, one_glider_expected, "One glider")

        two_gliders = [
            [1, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 1]
        ]
        two_gliders_expected = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        ]
        two_gliders_actual = get_generation(two_gliders, 16)
        self.assertEqual(two_gliders_actual, two_gliders_expected, "Two gliders")

if __name__ == '__main__':
    unittest.main()

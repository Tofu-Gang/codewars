import unittest
from src.pig_it import pig_it


class TestPigIt(unittest.TestCase):

    def test_pig_it(self):
        self.assertEquals(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEquals(pig_it('This is my string'), 'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()

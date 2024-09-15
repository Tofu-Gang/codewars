import unittest
from src.maskify import maskify


class TestMaskify(unittest.TestCase):

    def test_maskify(self):
        self.assertEquals(maskify(''), '')
        self.assertEquals(maskify('123'), '123')
        self.assertEquals(maskify('SF$SDfgsd2eA'), '########d2eA')


if __name__ == '__main__':
    unittest.main()

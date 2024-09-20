import unittest
from src.decode_morse import decode_morse, decode_bits


class TestDecodeMorse(unittest.TestCase):

    def test_decode_morse(self):
        self.assertEquals(decode_morse(decode_bits(
            '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011'
            '001111110000001111110011001100000011')), 'HEY JUDE')


if __name__ == '__main__':
    unittest.main()

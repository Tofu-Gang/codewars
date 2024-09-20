import unittest
from src.decode_morse import decode_morse


class TestDecodeMorse(unittest.TestCase):

    def test_decode_morse(self):
        self.assertEquals(decode_morse('.-'), 'A')
        self.assertEquals(decode_morse('--...'), '7')
        self.assertEquals(decode_morse('...-..-'), '$')
        self.assertEquals(decode_morse('.'), 'E')
        self.assertEquals(decode_morse('..'), 'I')
        self.assertEquals(decode_morse('. .'), 'EE')
        self.assertEquals(decode_morse('.   .'), 'E E')
        self.assertEquals(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        self.assertEquals(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        self.assertEquals(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        self.assertEquals(decode_morse('...---...'), 'SOS')
        self.assertEquals(decode_morse('... --- ...'), 'SOS')
        self.assertEquals(decode_morse('...   ---   ...'), 'S O S')
        self.assertEquals(decode_morse(' . '), 'E')
        self.assertEquals(decode_morse('   .   . '), 'E E')
        self.assertEquals(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   '
            '.--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
            'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')


if __name__ == '__main__':
    unittest.main()

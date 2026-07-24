import unittest
from function_1_hello_world import greet

class TestFunction1HelloWorld(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet(), "hello world!", "Greet doesn't return hello world!")

if __name__ == '__main__':
    unittest.main()

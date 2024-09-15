import unittest
from src.paperwork import paperwork


class TestPaperwork(unittest.TestCase):

    def test_paperwork(self):
        self.assertEquals(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")
        self.assertEquals(paperwork(1, 2), 2, "Failed at Paperwork(1,2)")
        self.assertEquals(paperwork(-5, 5), 0, "Failed at Paperwork(-5,5)")
        self.assertEquals(paperwork(5, -5), 0, "Failed at Paperwork(5,-5)")
        self.assertEquals(paperwork(-5, -5), 0, "Failed at Paperwork(-5,-5)")
        self.assertEquals(paperwork(5, 0), 0, "Failed at Paperwork(5,0)")


if __name__ == '__main__':
    unittest.main()

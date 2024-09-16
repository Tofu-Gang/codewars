import unittest
from src.dna_strand import DNA_strand


class TestDNAStrand(unittest.TestCase):

    def test_dna_strand(self):
        self.assertEquals(DNA_strand("AAAA"), "TTTT", "String AAAA is")
        self.assertEquals(DNA_strand("ATTGC"), "TAACG", "String ATTGC is")
        self.assertEquals(DNA_strand("GTAT"), "CATA", "String GTAT is")


if __name__ == '__main__':
    unittest.main()

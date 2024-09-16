"""
Complementary DNA
https://www.codewars.com/kata/554e4a2f232cdd87d9000038

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of
the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or
there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""

COMPLEMENT_MAP = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}


def get_complement(symbol: str) -> str:
    """
    :param symbol: one of A, T, C or G
    :return: the other from pair AT or the other from pair CG
    """

    return COMPLEMENT_MAP[symbol]


def DNA_strand(dna: str) -> str:
    """
    :param dna: dna string (consists of any combinations of T, A, C, G symbols)
    :return: complementary side (every symbol replaced by its complement)
    """

    return "".join(get_complement(symbol) for symbol in dna)

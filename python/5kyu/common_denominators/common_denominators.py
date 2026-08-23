__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/54d7660d2daf68c619000d95

Common denominators

You will have a list of rationals in the form

{ {numer_1, denom_1} , ... {numer_n, denom_n} } 
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ] 

where all numbers are positive ints. You have to produce a result in the form:

(N_1, D) ... (N_n, D) 
or
[ [N_1, D] ... [N_n, D] ] 
or
[ (N_1', D) , ... (N_n, D) ] 
or
{{N_1, D} ... {N_n, D}} 
or
"(N_1, D) ... (N_n, D)"

depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

Note:
Due to the fact that the first translations were written long ago - more than 6 years - these first translations have 
only irreducible fractions.

Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by 
simplifying fractions even if they don't have to be.

Note for Bash:
input is a string, e.g "2,4,2,6,2,8" output is then "6 12 4 12 3 12"
"""

from functools import reduce
from math import floor

def gcd(a, b):
    """
    :param a: integer
    :param b: integer
    :return: greatest common denominator of the two input integers
    """

    # ensure that a >= b
    [a, b] = sorted([a, b], reverse=True)

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    """
    :param a: integer
    :param b: integer
    :return: least common multiplier of the two input integers
    """
    return floor(abs(a * b) / gcd(a, b))


def convert_fracts(lst):
    """
    :param lst: input fractions in the format [[numer_1, denom_1], ... [numer_n, denom_n]]
    :return: [[N_1, D], ... [N_n, D]] where D is as small as possible and
    N_1/D == numer_1/denom_1, ... N_n/D == numer_n,/denom_n or empty list for empty input
    """

    try:
        denominators = sorted(tuple(frac[1] for frac in lst), reverse=True)
        denominator = reduce(lambda a, b: lcm(a, b), denominators)
        return list([floor(denominator / frac[1]) * frac[0], denominator] for frac in lst)
    except TypeError:
        return []

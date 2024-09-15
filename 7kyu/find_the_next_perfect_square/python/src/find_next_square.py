"""
Find the next perfect square!
https://www.codewars.com/kata/56269eb78ad2e4ced1000013

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on
your language. You may assume the argument is non-negative.

Examples ( Input --> Output )
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
"""

import math


def int_square_root(number: int) -> int:
    """
    :param number: an integer
    :return: square root of the input number as an integer
    """

    return int(math.sqrt(number))


def is_integral_perfect_square(number: int) -> bool:
    """
    :param number: an integer
    :return: True if the input number square root is also an integer, False otherwise
    """

    return int_square_root(number) ** 2 == number


def find_next_square(sq: int) -> int:
    """
    :param sq: an integer
    :return: the next number which is an integral perfect square or -1 if the input number is not a perfect square
    """

    # Return the next square if sq is a square, -1 otherwise
    if not is_integral_perfect_square(sq):
        return -1
    else:
        number = sq + 1
        while not is_integral_perfect_square(number):
            number += 1
        return number
    
__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument
(also a string).

Examples:
Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
"""

def solution(text, ending):
    """
    :param text: input string
    :param ending: test string ending
    :return: True if the input ends with the test ending, False otherwise
    """

    return text.endswith(ending)

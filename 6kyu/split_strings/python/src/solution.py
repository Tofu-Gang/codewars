"""
Split Strings
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of
characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

from typing import List


def solution(s: str) -> List[str]:
    """
    :param s: a string
    :return: a list of pairs of characters from the input string; last pair completed by an underscore if necessary
    """

    if len(s) % 2 != 0:
        s += "_"

    result = []
    while len(s) > 0:
        result.append(s[:2])
        s = s[2:]
    return result

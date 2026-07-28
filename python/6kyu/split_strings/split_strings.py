__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

Complete the solution so that it splits the string into strings of two characters in a list/array (depending on the 
language you use). If the string contains an odd number of characters then it should replace the missing second 
character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    """
    :param s: input strings
    :return: list of character pairs from the input string (if input length is odd, suffix the last letter with '_')
    """

    # add suffix "_" if the input string length is odd
    s = s if len(s) % 2 == 0 else s+"_"
    return list(s[i:i+2] for i in range(0, len(s), 2))

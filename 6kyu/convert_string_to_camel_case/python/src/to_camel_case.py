"""
Convert string to camel case
https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete the method/function so that it converts dash/underscore delimited words
into camel casing. The first word within the output should be capitalized only
if the original word was capitalized (known as Upper Camel Case, also often
referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

from re import split


################################################################################

def to_camel_case(text: str) -> str:
    """
    :param text: words separated by either - or _
    :return: input text converted to camel case without the delimiters
    """

    try:
        words = split("[-_]", text)
        first = words[0]
        words = words[1:]
        return first + "".join(word.capitalize() for word in words)
    except IndexError:
        return ""

################################################################################

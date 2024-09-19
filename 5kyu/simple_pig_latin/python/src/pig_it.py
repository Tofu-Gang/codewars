"""
Simple Pig Latin
https://www.codewars.com/kata/520b9d2ad5c005041100000f

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import string


def pig_it(text: str) -> str:
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
    untouched.

    :param text: a string
    :return: input text translated into pig latin
    """

    words = text.split()
    for i in range(len(words)):
        word = words[i]
        if all(character not in word for character in string.punctuation):
            words[i] = word[1:]+word[0]+"ay"
    return " ".join(words)

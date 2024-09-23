"""
Nesting Structure Comparison
https://www.codewars.com/kata/520446778469526ec0000001

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the
same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
from typing import List


def same_structure_as(original: List | str, other: List | str) -> bool:
    """
    :param original: only list is considered an iterable, string is not!
    :param other: only list is considered an iterable, string is not!
    :return: True if both params have the same nesting structures and the same length of nested lists, False otherwise
    """

    original_is_iterable = isinstance(original, list)
    other_is_iterable = isinstance(other, list)

    if original_is_iterable and other_is_iterable:
        len_original = len(original)
        len_other = len(other)

        if len_original == len_other:
            return all([same_structure_as(original[i], other[i]) for i in range(len_original)])
        else:
            return False
    elif original_is_iterable == other_is_iterable:
        return True
    else:
        return False

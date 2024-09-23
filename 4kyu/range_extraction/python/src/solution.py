"""
Range Extraction
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The
range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at
least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

Courtesy of rosettacode.org
"""


from typing import List


def solution(numbers: List[int]) -> str:
    """
    A format for expressing an ordered list of integers is to use a comma separated list of either
    -individual integers
    -a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
     The range includes all integers in the interval including both endpoints. It is not considered a range unless it
     spans at least 3 numbers. For example "12,13,15-17"

    :param numbers: list of integers, ascending order
    :return: string in the range format
    """

    # first, create sub-lists of individual ranges of integers
    numbers_ranges = [[]]

    for number in numbers:
        numbers_range = numbers_ranges[-1]
        try:
            if number == numbers_range[-1] + 1:
                numbers_range.append(number)
            else:
                numbers_ranges.append([])
                numbers_ranges[-1].append(number)
        except IndexError:
            numbers_range.append(number)

    # second, replace every sub-list with a string in a range format
    i = 0
    while i < len(numbers_ranges):
        numbers_range = numbers_ranges[i]

        if len(numbers_range) >= 3:
            numbers_ranges[i] = f"{str(numbers_range[0])}-{str(numbers_range[-1])}"
        else:
            numbers_ranges[i] = ",".join(map(str, numbers_range))
        i += 1

    # create and return a resulting range formatted string
    return ",".join(numbers_ranges)

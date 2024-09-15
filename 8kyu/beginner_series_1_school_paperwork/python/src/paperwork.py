"""
Beginner Series #1 School Paperwork
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has
'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
Waiting for translations and Feedback! Thanks!
"""


def paperwork(n: int, m: int) -> int:
    """
    :param n: number of classmates
    :param m: number of pages
    :return: count of blank pages to needed for m pages for n classmates; if n or m is less than zero, return zero
    """

    if n >= 0 and m >= 0:
        return m * n
    else:
        return 0

__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:
seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3

Requirements:
- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Division should be integer division. For example, this should return 2, not 2.666666...:
  eight(divided_by(three()))
"""

def number_function(arg, digit):
    """
    :param arg: either None or operator function call result
    :param digit: integer representing the caller function (zero, one, two, ...)
    :return: either just the digit or eval result of "operand operator operand" formula
    """
    return eval(f"{digit}{arg}") if arg else digit

"""
:param arg: either None or operator function call result 
:return: either just the digit representing the function or eval result of "operand operator operand" formula
"""
def zero(arg=None): return number_function(arg, 0)
def one(arg=None): return number_function(arg, 1)
def two(arg=None): return number_function(arg, 2)
def three(arg=None): return number_function(arg, 3)
def four(arg=None): return number_function(arg, 4)
def five(arg=None): return number_function(arg, 5)
def six(arg=None): return number_function(arg, 6)
def seven(arg=None): return number_function(arg, 7)
def eight(arg=None): return number_function(arg, 8)
def nine(arg=None): return number_function(arg, 9)

"""
:param right_operand: right operand
:return: string of operator and right operand
"""
def plus(right_operand): return f"+{right_operand}"
def minus(right_operand): return f"-{right_operand}"
def times(right_operand): return f"*{right_operand}"
def divided_by(right_operand): return f"//{right_operand}"

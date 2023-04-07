# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

import math

def find_next_square(sq):
    """
    You might know some pretty large perfect squares. But what about the NEXT one?

    Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
    Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

    If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is
    non-negative.

    Examples:
    >>> find_next_square(121)
    144
    >>> find_next_square(625)
    676
    >>> find_next_square(114)
    -1

    """
    sqrt = math.sqrt(sq)
    return int((sqrt + 1) ** 2) if sqrt.is_integer() else -1

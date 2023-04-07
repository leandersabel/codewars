# https://www.codewars.com/kata/526571aae218b8ee490006f4

def count_bits(n):
    """
    A function that takes an integer as input, and returns the number of bits that are equal to one in the
    binary representation of that number. You can guarantee that input is non-negative.

    Example:
    >>> count_bits(1234)
    5
    """
    return bin(n).count('1')

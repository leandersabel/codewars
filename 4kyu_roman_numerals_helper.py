# https://www.codewars.com/kata/51b66044bce5799a7f000003/

"""Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will
be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008
is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
"""
import itertools
import math


class RomanNumerals:

    @staticmethod
    def to_roman(int_value):
        """
        Input range : 1 <= n < 4000

        >>> RomanNumerals.to_roman(2008)
        'MMVIII'
        >>> RomanNumerals.to_roman(2000)
        'MM'
        >>> RomanNumerals.to_roman(1990)
        'MCMXC'
        >>> RomanNumerals.to_roman(1666)
        'MDCLXVI'
        >>> RomanNumerals.to_roman(1000)
        'M'
        >>> RomanNumerals.to_roman(400)
        'CD'
        >>> RomanNumerals.to_roman(90)
        'XC'
        >>> RomanNumerals.to_roman(40)
        'XL'
        >>> RomanNumerals.to_roman(1)
        'I'
        """

        numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                    5: 'V', 4: 'IV', 1: 'I'}
        numeral = ''

        for val, num in numerals.items():
            if int_value / val > 0:
                numeral += num * (int_value // val)
                int_value = int_value % val

        return numeral

    @staticmethod
    def from_roman(roman_num):
        """
        Input range : 1 <= n < 4000
        >>> RomanNumerals.from_roman('MM')
        2000
        >>> RomanNumerals.from_roman('MDCLXVI')
        1666
        >>> RomanNumerals.from_roman('M')
        1000
        >>> RomanNumerals.from_roman('CD')
        400
        >>> RomanNumerals.from_roman('XC')
        90
        >>> RomanNumerals.from_roman('XL')
        40
        >>> RomanNumerals.from_roman('I')
        1
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        v = sum([cv if cv >= nv else -cv for cv, nv in itertools.pairwise([values[num] for num in roman_num])])
        return v + values[roman_num[-1]]

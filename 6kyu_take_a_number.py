# https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b):
    """
    range(a, b + 1) will be studied by the function

    The number 89 is the first integer with more than one digit that fulfills the property partially introduced in
    the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number:
    89 = 8^1 + 9^2

    The next number in having this property is 135
    135 = 1^1 + 3^2 + 5^3

    Task:
    We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b]
    (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

    >>> sum_dig_pow(1, 10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> sum_dig_pow(1, 100)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

    >>> sum_dig_pow(90, 100)
    []
    """
    numbers = []
    for number in range(a, b + 1):
        sum_of_dig_pow = sum([int(digit) ** (d + 1) for d, digit in enumerate(str(number))])
        if sum_of_dig_pow == number: numbers.append(number)
    return numbers

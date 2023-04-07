# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    """
    Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
    number of characters then it should replace the missing second character of the final pair with an underscore (
    '_').

    Examples:
    >>> solution('')
    []
    >>> solution('abc')
    ['ab', 'c_']
    >>> solution('abcdef')
    ['ab', 'cd', 'ef']
    >>> solution("asdfads")
    ['as', 'df', 'ad', 's_']
    """

    if len(s) % 2 == 1: s += '_'
    return [s[i] + s[i+1] for i in range(0, len(s), 2)]

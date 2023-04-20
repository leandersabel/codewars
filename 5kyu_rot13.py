# https://www.codewars.com/kata/52223df9e8f98c7aa7000062

import string


def rot13(message):
    """
    How can you tell an extrovert from an introvert at NSA?
    Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
    According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

    For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

    Test examples:

    >>> rot13('EBG13 rknzcyr.')
    'ROT13 example.'

    >>> rot13("This is my first ROT13 excercise!")
    'Guvf vf zl svefg EBG13 rkprepvfr!'
    """

    alphabet = list(string.ascii_lowercase)
    alphabet_dic = {val: i for i, val in enumerate(alphabet)}
    rot = ""

    for char in message:
        if not char.isalpha():
            rot += char
        else:
            rot_char = alphabet[(alphabet_dic[char.lower()] + 13) % 26]
            rot += rot_char if char.islower() else rot_char.upper()

    return rot

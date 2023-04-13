# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

import re


def strip_comments(strng, markers):
    """
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any
    whitespace at the end of the line should also be stripped out.

    >>> strip_comments("apples, pears # and bananas\\ngrapes\\nbananas !apples", ["#", "!"])
    'apples, pears\\ngrapes\\nbananas'

    >>> strip_comments("apples, pears $ and bananas\\ngrapes\\nbananas !apples", ["$", "!"])
    'apples, pears\\ngrapes\\nbananas'

    >>> strip_comments("a #b\\nc\\nd $e f g", ["#", "$"])
    'a\\nc\\nd'

    >>> strip_comments(" a #b\\nc\\nd $e f g", ['#', '$'])
    ' a\\nc\\nd'

    """
    if len(markers) == 0:
        return strng

    r = r''.join('\\' + marker + '|' for marker in markers)[:-1]
    return ''.join(re.split(r, line)[0].rstrip() + '\n' for line in strng.split('\n'))[:-1]

    #s = ''
    #for line in strng.split('\n'):
    #    sub = re.split(r, line)[0].strip() + '\n'
    #    s += sub

    #return s[:-1]

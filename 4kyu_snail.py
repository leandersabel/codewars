# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

from enum import Enum


def snail(snail_map):
    """
    Snail Sort Given an n x n array, return the array elements arranged from outermost elements to the middle
    element, traveling clockwise.

    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]

    For better understanding, please follow the numbers of the next array consecutively:

    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]
    This image will illustrate things more clearly:


    NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array
    in a clockwise snailshell pattern.

    NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

    >>> snail([[]])
    []

    >>> snail([[1,2,3],[4,5,6],[7,8,9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> snail([[1,2,3],[8,9,4],[7,6,5]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """

    if len(snail_map) == 0 or len(snail_map[0]) == 0:
        return []

    row = 0
    col = 0
    direction = 'right'
    snail_path = []

    while len(snail_path) < len(snail_map) * len(snail_map[0]):

        if direction == 'right':
            while col < len(snail_map[0]) and snail_map[row][col] != '#':
                snail_path.append(snail_map[row][col])
                snail_map[row][col] = '#'
                col += 1

            direction = 'down'
            row += 1
            col -= 1

        elif direction == 'down':
            while row < len(snail_map) and snail_map[row][col] != '#':
                snail_path.append(snail_map[row][col])
                snail_map[row][col] = '#'
                row += 1

            direction = 'left'
            row -= 1
            col -= 1

        elif direction == 'left':
            while col >= 0 and snail_map[row][col] != '#':
                snail_path.append(snail_map[row][col])
                snail_map[row][col] = '#'
                col -= 1

            direction = 'up'
            row -= 1
            col += 1

        elif direction == 'up':
            while row >= 0 and snail_map[row][col] != '#':
                snail_path.append(snail_map[row][col])
                snail_map[row][col] = '#'
                row -= 1

            direction = 'right'
            row += 1
            col += 1

    return snail_path
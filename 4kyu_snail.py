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


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


"""snail([[417, 639, 957, 715, 870, 972, 828, 976, 27, 859, 389, 777, 115, 653, 53, 464, 874, 309, 827, 342],
       [267, 192, 315, 363, 569, 543, 383, 370, 483, 572, 436, 718, 880, 402, 673, 998, 745, 729, 178, 191],
       [998, 977, 76, 6, 899, 309, 991, 463, 184, 537, 679, 252, 580, 704, 553, 107, 697, 152, 955, 967],
       [349, 41, 243, 762, 183, 876, 326, 106, 548, 814, 17, 206, 143, 366, 34, 538, 416, 322, 301, 935],
       [981, 923, 289, 446, 725, 59, 11, 338, 149, 82, 729, 426, 289, 370, 281, 112, 611, 797, 103, 247],
       [20, 150, 518, 246, 859, 162, 601, 666, 769, 441, 382, 268, 205, 295, 497, 353, 59, 193, 986, 979],
       [471, 197, 1000, 166, 530, 723, 8, 718, 648, 476, 893, 834, 850, 813, 577, 476, 304, 118, 254, 660],
       [110, 961, 116, 349, 769, 256, 67, 685, 747, 285, 156, 149, 845, 656, 871, 714, 410, 752, 140, 564],
       [248, 335, 183, 184, 548, 172, 213, 516, 925, 338, 459, 424, 352, 560, 812, 978, 810, 455, 377, 523],
       [244, 830, 710, 728, 688, 980, 43, 223, 997, 906, 879, 367, 448, 397, 950, 677, 65, 468, 811, 180],
       [196, 144, 962, 476, 997, 825, 590, 790, 792, 949, 671, 906, 188, 356, 174, 999, 39, 591, 417, 564],
       [940, 103, 634, 929, 436, 803, 553, 341, 16, 28, 63, 566, 199, 464, 220, 711, 695, 942, 945, 699],
       [452, 648, 959, 260, 862, 283, 486, 928, 796, 569, 680, 533, 278, 927, 180, 466, 703, 892, 765, 41],
       [296, 99, 365, 231, 862, 965, 88, 331, 474, 137, 495, 568, 422, 510, 311, 601, 61, 851, 431, 269],
       [602, 729, 864, 232, 177, 19, 269, 533, 453, 618, 675, 985, 266, 851, 393, 588, 448, 322, 907, 481],
       [240, 540, 189, 249, 649, 888, 381, 428, 147, 840, 80, 690, 11, 287, 838, 713, 284, 24, 198, 419],
       [899, 534, 554, 671, 192, 354, 733, 567, 978, 420, 325, 294, 291, 567, 848, 113, 369, 906, 448, 901],
       [379, 209, 435, 583, 1, 355, 803, 492, 679, 291, 269, 311, 214, 497, 50, 432, 640, 799, 896, 671],
       [914, 195, 544, 625, 20, 269, 856, 453, 719, 253, 168, 505, 790, 930, 228, 173, 907, 343, 875, 582],
       [154, 701, 354, 251, 216, 636, 299, 31, 709, 18, 518, 77, 253, 483, 474, 767, 821, 716, 518, 907]])
"""
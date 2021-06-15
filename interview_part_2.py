# ***************************** 1 *****************************
# -------------------------------------------------------------
# Дан список, состоящий из целых чисел. Нужно 'поднять' нули
# в конец списка с сохранением порядка за один проход


def popup_zeros(nums):
    """
    >>> popup_zeros([0, 1, 2, 3, 1, 0, 0, 0, 2])
    [1, 2, 3, 1, 2, 0, 0, 0, 0]

    >>> popup_zeros([0, 1, 0, 0, 2, 3, 0])
    [1, 2, 3, 0, 0, 0, 0]

    >>> popup_zeros([0, 1, 2, 0, 3])
    [1, 2, 3, 0, 0]

    >>> popup_zeros([3, 0, 2, 0])
    [3, 2, 0, 0]

    >>> popup_zeros([3, 2, 0, 3])
    [3, 2, 3, 0]

    >>> popup_zeros([0])
    [0]

    >>> popup_zeros([3])
    [3]

    >>> popup_zeros([])
    []
    """
    copied = nums[:]
    first_zero_pos = 0
    for i in range(len(copied) - 1):
        if copied[i] != 0:
            first_zero_pos += 1

        elif copied[i + 1] != 0:
            copied[first_zero_pos], copied[i + 1] = copied[i + 1], copied[first_zero_pos]
            first_zero_pos += 1

    return copied

# == == == == == == == == == == == == == == == == == == == == == == =

"""
Дан массив точек с целочисленными координатами (x, y).
Определить, существует ли вертикальная прямая, 
делящая точки на 2 симметричных относительно этой прямой множества.
Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}
"""
#   .
#  /\
# /  \

# is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)])  # True
# is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0)])  # False
# is_vert_sym([])  # True
# is_vert_sym([(0, 0)])  # True
# is_vert_sym([(0, 0), (10, 0)])  # True
# is_vert_sym([(0, 0), (11, 1)])  # False
# is_vert_sym([(0, 0), (1, 0), (3, 0)])  # False
#
# is_vert_sym([(4, 1), (4, 2), (6, 1), (6, 2)]])  # поломались


def comparator(a, b):
    return a - b


def sort_(comparators):
    return comparators[0] or comparators[1]


def is_vert_sym(lst):
    if not lst:
        return True

    points = sorted(lst, key=lambda x: x[0])

    psevdo_center = len(points) // 2

    if len(points) % 2:
        center_x = points[psevdo_center][0]
    else:
        center_x = points[psevdo_center - 1][0] + (points[psevdo_center][0] - points[psevdo_center - 1][0]) / 2

    for i in range(psevdo_center):
        left = points[i]
        right = points[-i - 1]
        if left[1] != right[1]:
            return False

        if center_x - left[0] != right[0] - center_x:
            return False

    return True

#
# def is_vert_sym(lst):
#     if not lst:
#         return True
#
#
# points = sorted(lst, key=lambda x: x[0])
# center_x = points[0][0] + (points[-1][0] - points[0][0]) / 2
# for i in range(psevdo_center):
#     left = points[i]
#     right = points[-i - 1]
#
#

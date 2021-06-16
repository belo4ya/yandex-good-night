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


# ***************************** 2 *****************************
# -------------------------------------------------------------
# Дан массив точек с целочисленными координатами (x, y).
# Определить, существует ли вертикальная прямая,
# делящая точки на 2 симметричных относительно этой прямой множества.


# is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)])  # True
# is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0)])  # False
# is_vert_sym([])  # True
# is_vert_sym([(0, 0)])  # True
# is_vert_sym([(0, 0), (10, 0)])  # True
# is_vert_sym([(0, 0), (11, 1)])  # False
# is_vert_sym([(0, 0), (1, 0), (3, 0)])  # False
#
# is_vert_sym([(4, 1), (4, 2), (6, 1), (6, 2)]])  # поломались


def is_vert_sym(points):
    """
    >>> is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)])
    True

    >>> is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0)])
    True

    >>> is_vert_sym([(4, 1), (4, 2), (6, 1), (6, 2)])
    True

    >>> is_vert_sym([(0, 0), (1, 0), (3, 0)])
    False

    >>> is_vert_sym([(0, 0), (11, 1)])
    False

    >>> is_vert_sym([(0, 0), (10, 0)])
    True

    >>> is_vert_sym([(0, 0)])
    True

    >>> is_vert_sym([])
    True
    """

    if not points:
        return True

    sym_points = set(points)  # допущение, что несколько одинаковых точек симметричны одной

    left_x = min(points, key=lambda p: p[0])[0]
    right_x = max(points, key=lambda p: p[0])[0]
    center_x = left_x + (right_x - left_x) / 2

    for point in sym_points:
        point_x, point_y = point[0], point[1]

        distance = abs(center_x - point_x)
        if point_x < center_x:
            mirror_x = center_x - distance
        elif point_x > center_x:
            mirror_x = center_x + distance
        else:
            continue

        mirror_point = (mirror_x, point_y)
        if mirror_point not in sym_points:
            return False

    return True


print(is_vert_sym([(0, 0), (0, 0), (1, 1), (2, 2), (3, 1), (4, 0), (4, 0)]))

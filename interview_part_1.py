import math

# ***************************** 1 *****************************
# -------------------------------------------------------------
# В коде ниже допущены ошибки, нужно исправить их:
#
# def get_first_matching_object(predicate, objects=[]):
#   matching_objects = (obj for obj in objects if predicate(object))
#   if matching_objects:
#     object = matching_objects[0]
#     return object
#   else:
#     return None


def get_first_matching_object(predicate, objects):
    matching_objects = (obj for obj in objects if predicate(obj))
    return next(matching_objects, None)  # допущение что нет функции is_none


# ***************************** 2 *****************************
# -------------------------------------------------------------
# Стек с константным поиском максимального элемента.
# push, pop, max должны работать за O(1) по времени.


class MaxStack:

    def __init__(self):
        self._stack = []
        self._max_values = [-math.inf]

    def push(self, elem):
        self._stack.append(elem)

        if elem >= self._peek_max():
            self._max_values.append(elem)

    def pop(self):
        elem = self._stack.pop()

        if elem == self._peek_max():
            self._max_values.pop()

        return elem

    def max(self):
        if self._stack:
            return self._peek_max()

    def _peek_max(self):
        return self._max_values[-1]


# ***************************** 3 *****************************
# -------------------------------------------------------------
# Дан список целых чисел, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.


def compress(int_array):
    """
    >>> compress([1, 4, 5, 2, 3, 9, 8, 11, 0])
    '0-5,8-9,11'

    >>> compress([1, 4, 3, 2])
    '1-4'

    >>> compress([1, 4])
    '1,4'

    >>> compress([1, 4, 5, 2, 3, 9, 8, 0])
    '0-5,8-9'

    >>> compress([0, 1, 2, 3, 5, 8, 10, 12])
    '0-3,5,8,10,12'

    >>> compress([0, 2, 4, 5, 8])
    '0,2,4-5,8'
    """

    def render(begin, end=None):
        begin = str(begin)
        return begin + '-' + str(end) if end else begin

    array_length = len(int_array)

    if array_length == 0:
        return ''
    elif array_length == 1:
        return render(int_array[0])

    sorted_array = sorted(int_array)
    ranges = []
    start_range_index = 0

    for i in range(1, array_length):
        prev_el = sorted_array[i - 1]
        current_el = sorted_array[i]
        start_range_el = sorted_array[start_range_index]

        if current_el != prev_el + 1:
            if start_range_index == i - 1:
                ranges.append(render(start_range_el))
            else:
                ranges.append(render(start_range_el, prev_el))

            start_range_index = i

    if start_range_index == array_length - 1:
        ranges.append(render(sorted_array[-1]))
    else:
        ranges.append(render(sorted_array[start_range_index], sorted_array[-1]))

    return ','.join(ranges)


# ***************************** 4 *****************************
# -------------------------------------------------------------
# SQL
# таблица (продукт - дата - цена)
# если цена изменилась заносятся данные
# актуальный срез цен на заданную дату

stmt_0 = """
SELECT product_name, price FROM products p1
WHERE updated_at = (
    SELECT MAX(updated_at) FROM products p2
    WHERE p1.product_name == p2.product_name AND p2.updated_at <= :slice_date
    GROUP BY p2.product_name
    );
"""

stmt_1 = """
SELECT *, (
    SELECT price FROM PRODUCTS sub
    WHERE sub.product_name == p.product_name AND sub.updated_at <= :slice_date
    ORDER BY sub.updated_at DESC LIMIT 1
    ) AS target_price
FROM PRODUCTS p;
"""

stmt_2 = """
SELECT product_name, price FROM (
    SELECT product_name, price, ROW_NUMBER() OVER (
        PARTITION BY product_name ORDER BY updated_at DESC
        ) row FROM PRODUCTS WHERE updated_at <= :slice_date
    ) t
WHERE t.row = 1;
"""

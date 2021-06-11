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
#
# Примеры:
# - [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
# - [1, 4, 3, 2] => "1-4"
# - [1, 4] => "1,4"
# - [1, 4, 5, 2, 3, 9, 8, 0] => "0-5,8-9"
# - [0, 1, 2, 3, 5, 8, 10, 12] => "0-3, 5, 8, 10, 12"
# - [0, 2, 4, 5, 8] => "0, 2, 4-5, 8"


def render(start, end=None):
    start = str(start)
    if end:
        return start + '-' + str(end)

    return start


def compress(int_array):
    """
    TODO: переделать
    TODO: doctests
    """
    if len(int_array) == 0:
        return ''
    if len(int_array) == 1:
        return render(int_array[0])

    sorted_array = sorted(int_array)
    ranges = []
    start_index = 0

    for i in range(1, len(sorted_array)):
        current = sorted_array[i]
        prev = sorted_array[i - 1]
        start = sorted_array[start_index]

        if current - prev > 1:
            if start_index == i - 1:
                ranges.append(render(start))
            else:
                ranges.append(render(start, prev))
            start_index = i

    if start_index == len(sorted_array) - 1:
        ranges.append(render(sorted_array[-1]))
    else:
        ranges.append(render(sorted_array[start_index], sorted_array[-1]))

    return ','.join(ranges)


# ***************************** 4 *****************************
# -------------------------------------------------------------
# SQL
# таблица (продукт дата цена)
# если цена изменилась заносится данные
# актуальный срез цен на заданную дату
stmt = """
SELECT product_name, price FROM products p1
WHERE updated_at = (
    SELECT MAX(updated_at) FROM products p2
    WHERE p1.product_name == p2.product_name AND
          p2.updated_at <= :slice_date
    GROUP BY p2.product_name
    );
"""

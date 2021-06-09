# SQL
# таблица (продукт дата цена)
# если цена изменилась заносится данные
# актуальный срез цен на заданную дату


def get_first_matching_object(predicate, objects):
    matching_objects = [obj for obj in objects if predicate(obj)]
    if matching_objects:
        return matching_objects[0]


# 1) изменяемый
# дефолтный
# аргумент
# 2) object -> obj
# 3) matching_objects - генератор
# 4) излишний None

# ------------------------------------------------------------
# 5
# 5
# 5


class MaxStack(object):
    """
    Стек с константным поиском максимального элемента.

    push, pop, max должны работать за O(1) по времени.
    """

    def __init__(self):
        self._store = []
        self._stack_for_max_values = [float('-inf')]

    def push(self, elem):
        self._store.append(elem)

        if elem >= self._stack_for_max_values[-1]:
            self._stack_for_max_values.append(elem)

    def pop(self):
        elem = self._store.pop()

        if elem == self._stack_for_max_values[-1]:
            self._stack_for_max_values.pop()

    def max(self):
        return self._stack_for_max_values[-1]


# -----------------------------------------------------------

"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку, 
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"  
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
- [1, 4, 5, 2, 3, 9, 8, 0] => "0-5,8-9"
- [0, 1, 2, 3, 5, 8, 10, 12] => "0-3, 5, 8, 10, 12"
- [0, 2, 4, 5, 8] => "0, 2, 4-5, 8"
"""


def pretty(start, end=None):
    return str(start) + "-" + str(end) if end is not None else str(start)


def compress(int_array):
    if len(int_array) == 0:
        return ''
    if len(int_array) == 1:
        return pretty(int_array[0])

    sorted_array = sorted(int_array)
    ranges = []
    start_index = 0

    for i in range(1, len(sorted_array)):
        current = sorted_array[i]
        prev = sorted_array[i - 1]
        start = sorted_array[start_index]

        if current - prev > 1:
            if start_index == i - 1:
                ranges.append(pretty(start))
            else:
                ranges.append(pretty(start, prev))
            start_index = i

    if start_index == len(sorted_array) - 1:
        ranges.append(pretty(sorted_array[-1]))
    else:
        ranges.append(pretty(sorted_array[start_index], sorted_array[-1]))

    return ','.join(ranges)

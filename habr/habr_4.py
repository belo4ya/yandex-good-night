# Дан массив из нулей и единиц.
# Нужно определить, какой максимальный по длине интервал единиц можно получить,
# удалив ровно один элемент массива.
# пример: [0, 0, 1, 1, 0, 1, 1, 0] -> 4


def max_ones_length(lst):
    """
    >>> max_ones_length([0, 0, 1, 1, 0, 1, 1, 0])
    4

    >>> max_ones_length([0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1])
    5

    >>> max_ones_length([1, 1, 1, 1, 1, 1, 1])
    7

    >>> max_ones_length([0, 0, 0, 0])
    0

    >>> max_ones_length([])
    0
    """
    ones_len_current = 0
    ones_len_prev = 0

    zeros_len = 0
    max_ones_len = 0

    prev_el = None
    for i, el in enumerate(lst):

        if el == 1:  # считаем 1
            ones_len_current += 1
        else:  # считаем 0
            zeros_len += 1

        if prev_el != el:  # произошла смена

            if el == 0:  # с 1 на 0

                if zeros_len == 1:
                    ones_len_prev = ones_len_current
                else:
                    ones_len_prev = 0

                ones_len_current = 0
            else:  # с 0 на 1
                zeros_len = 0

        max_ones_len = max(max_ones_len, ones_len_current + ones_len_prev)
        prev_el = el

    return max_ones_len

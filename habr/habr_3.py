# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"


def render(start, end=None):
    start = str(start)
    if end:
        return start + '-' + str(end)

    return start


def compress(int_array):
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

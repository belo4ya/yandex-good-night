# Слияние отрезков:
#
# Вход: [1, 3] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]


def merge(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

    if not ranges:
        return []

    result_ranges = []
    last_range = None  # последний отрезок, что мы видели

    for rng in sorted(ranges):  # обязательно сортируем

        if not last_range:
            last_range = rng
            continue

        # если начало текущего отрезка меньше конца предыдущего
        if rng[0] <= last_range[1]:
            # расширяем предыдущий отрезок на текущий
            last_range = (last_range[0], max(rng[1], last_range[1])

        # старый отрезок всё, начинаем новый
        else:
            result_ranges.append(last_range)
            last_range = rng

    else:
        # граничный случай для последнего элемента
        result_ranges.append(last_range)

    return result_ranges

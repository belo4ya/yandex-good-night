# Даны даты заезда и отъезда каждого гостя.
# Для каждого гостя дата заезда строго раньше даты отъезда
# (то есть каждый гость останавливается хотя бы на одну ночь).
# В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые.
# Найти максимальное число постояльцев, которые одновременно проживали в гостинице
# (считаем, что измерение количества постояльцев происходит в конце дня).
#
# sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]

from collections import defaultdict


def max_num_guests(guests):
    res = 0

    # для каждого дня посчитаем, сколько приехало и сколько отъехало
    arriving = defaultdict(int)
    leaving = defaultdict(int)

    for guest in guests:  # O(n)
        arriving[guest[0]] += 1
        leaving[guest[1]] += 1

    current = 0
    # едем по дням в порядке увеличения, добавлем приехавших и убавляем уехавших,
    # считаем сколько стало
    for day in sorted(set(arriving.keys()).union(set(leaving.keys()))):  # O(n*log(n)) + O(n)
        current -= leaving[day]
        current += arriving[day]

        if current > res:
            res = current

    return res


max_num_guests([(1, 2), (1, 3), (2, 4), (2, 3)])

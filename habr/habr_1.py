# https://habr.com/ru/post/550088/

# Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть [1, 2, 2, 3] (порядок неважен)
from collections import defaultdict


def count(collection):
    counter = defaultdict(int)
    for el in collection:
        counter[el] += 1

    return counter


def solve(arr_1, arr_2):
    counter_2 = count(arr_2)

    result = []
    for el in arr_1:
        if counter_2[el] > 0:
            result.append(el)
            counter_2[el] -= 1

    return result

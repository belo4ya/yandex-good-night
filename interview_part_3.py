# ***************************** 1 *****************************
# -------------------------------------------------------------
# Даны две отсортированный последовательности.
# Найти элементы из первой последовательности, которых нет во второй.


def minus(it1, it2):
    """
    >>> minus(iter([0, 1, 3, 3, 4, 6, 8, 8, 10]), iter([1, 2, 4, 4, 8]))
    [0, 3, 3, 6, 10]

    >>> minus(iter([0, 1, 3, 5, 10]), iter([2, 4, 6]))
    [0, 1, 3, 5, 10]

    >>> minus(iter([3, 5, 5, 7]), iter([2, 3, 4, 6, 10]))
    [5, 5, 7]

    >>> minus(iter([1, 2, 5, 7]), iter([]))
    [1, 2, 5, 7]

    >>> minus(iter([1]), iter([1, 1, 1, 1, 2, 3, 4]))
    []
    """
    result = []

    el2 = next(it2, None)
    for el1 in it1:

        while el2 is not None and el1 != el2:
            if el1 < el2:
                result.append(el1)
                break

            el2 = next(it2, None)

        if el2 is None:
            result.append(el1)

    return result


a1 = 'ABCBABCBDAB'
a2 = 'ABCDABCDEFA'


def length_of_longest_substr(s):
    checklist = {}
    start = 0
    max_l = 0
    for i, v in enumerate(s):
        if v in checklist:
            if checklist[v] >= start:
                start = checklist[v] + 1

        current_l = i - start
        max_l = max(current_l, max_l)
        checklist[v] = i

    return max_l

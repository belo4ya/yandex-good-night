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


# ***************************** 2 *****************************
# -------------------------------------------------------------
# a1 = 'ABCBABCBDAB'
# a2 = 'ABCDABCDEFA'


def length_of_longest_substr(string):
    """
    >>> length_of_longest_substr('ABCBABCBDAB')
    4
    >>> length_of_longest_substr('ABCDEFABCDEFABCDEFG')
    7
    >>> length_of_longest_substr('ABABABBC')
    2
    >>> length_of_longest_substr('ABCB')
    3
    >>> length_of_longest_substr('')
    0
    """
    last_meted = {}
    start = 0
    max_length = 0
    for i, ch in enumerate(string):
        if ch in last_meted:
            if last_meted[ch] >= start:
                start = last_meted[ch] + 1

        current_length = i + 1 - start
        max_length = max(current_length, max_length)
        last_meted[ch] = i

    return max_length

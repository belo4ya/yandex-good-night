# [0, 1, 3, 3, 4, 6, 8, 8, 10]
# [1, 2, 4, 4, 8]
# Последовательности отсортированы
# [0, 3, 3, 6, 10]
# next(it, None) -> None, если всё закончилось

# [2, 3, 6, 7, 9]
# [-1, 2, 6, 6, 6]
# [3, 7, 9]


def minus(it1, it2):
    result = []
    el2 = next(it2, None)

    for el1 in it1:

        while el2 is not None:

            if el1 < el2:
                result.append(el1)
                break
            elif el1 == el2:
                break
            el2 = next(it2, None)

        if el2 is None:
            result.append(el1)

    return result


# [6, 8, 8, 10]
# [8, 9]
# [6, 10]


# "ABCBAB > CBDA < B"
#    ^^
#  ABCDEFG....ZABCDEFG...Z
#   ^^^^^^^^^^^^^
def solution(string):
    i = 0
    j = 0
    n = 0

    answer_i = 0
    answer_j = 0
    max_len = 0

    dct = {}
    max_len = 0
    while j < len(string):
        ch_j = string[j]
        while ch_j in dct:
            ch_i = string[i]
            del dct[ch_i]
            i += 1
        dct[ch_j] = j
        j += 1
        if j - i > max_len:
            answer_j = j
            answer_i = i
            max_len = j - i

    return max_len

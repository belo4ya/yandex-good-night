# ***************************** 1 *****************************
# -------------------------------------------------------------
# Дана строка. Найти самый часто встречающийся в ней символ.
# Если несколько символов встречаются одинаково часто,
# то можно вывести любой
from collections import defaultdict


def get_most_common(string: str) -> str:
    """
    >>> get_most_common('aabbcaaaabcadeeef')
    'a'
    """
    if not string:
        return string

    counter = defaultdict(int)
    for ch in string:
        counter[ch] += 1

    most_common = 1
    most_common_ch = string[0]
    for ch in counter:
        if counter[ch] > most_common:
            most_common = counter[ch]
            most_common_ch = ch

    return most_common_ch

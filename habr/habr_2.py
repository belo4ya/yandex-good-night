# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.
import itertools


def rle(string):
    """
    >>> rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
    'A4B3C2XYZD4E3F3A6B28'
    """
    result = []
    cnt = 0
    prev_ch = string[0]
    for i, ch in enumerate(string[1:]):
        if ch == prev_ch:
            cnt += 1
        else:
            result.append(prev_ch)
            if cnt:
                result.append(str(cnt + 1))

            cnt = 0
            prev_ch = ch

    result.append(string[-1])
    if cnt:
        result.append(str(cnt + 1))

    return ''.join(result)


def cheat_rle(string):
    for char, same in itertools.groupby(string):
        count = sum([1 for _ in same])
        yield char if count == 1 else str(count) + char

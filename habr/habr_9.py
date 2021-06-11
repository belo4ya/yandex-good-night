# Даны две строки.
#
# Написать функцию, которая вернёт True,
# если из первой строки можно получить вторую,
# совершив не более 1 изменения (== удаление / замена символа).
from itertools import zip_longest


def no_more_than_one_change(string1: str, string2: str) -> bool:
    # string1: a b c d
    # string2: a b c

    max_length = max(len(string1), len(string2))  # наибольшая длина строк
    diff = abs(len(string1) - len(string2))  # разница в длине строк

    # дополняем строки до максимальной длины при помощи zip_longest,
    # то есть на место "недостающих" элементов ставим None, и строки
    # теперь одинаковой длины;
    #          ---->
    # string1: a b c d
    # string2: a b c None

    # идём слева направо по обеим строкам и сравниваем символы,
    # находим индекс, при котором строки начинают отличаться:
    change_left = None
    for i, (char1, char2) in enumerate(zip_longest(string1, string2)):  # O(n)
        if char1 != char2:
            change_left = i  # в нашем примере будет 3
            break
    else:
        # если мы такой индекс не нашли, то строки просто совпадают
        return True

    # теперь делаем то же, но идём справа налево:
    # string1:    a b c d
    # string2: None a b c
    #               <----
    change_right = None
    for j, (char1, char2) in enumerate(zip_longest(reversed(string1), reversed(string2))):  # O(n)
        if char1 != char2:
            # тут строки прям сразу отличаются, т.е. в индексе j=0;
            # но это у нас индекс в системе "справа налево",
            # а мы его переводим в индекс в системе "слева направо":
            i = max_length - j - 1 + diff
            break
    else:
        assert False, 'Я дебил и что-то не учёл'

    # ну а теперь смотрим, если строки отличаются в одном и том же месте
    # при сканировании слева направо и справа налево, то это нам подходит
    return change_left == change_right

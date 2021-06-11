# Дан массив из нулей и единиц.
# Нужно определить, какой максимальный по длине интервал единиц можно получить,
# удалив ровно один элемент массива.
# [1, 1, 0]

# пример: [0, 0, 1, 1, 0, 1, 1, 0]


# def max_ones_length(lst):
#     max_ones_length = 0
#
#     # тут мы хотим получить сгруппированные 0 или 1 и их количество:
#     subranges = []  # [(0, 2), (1, 2), (0, 1), (1, 2), (0, 1)]
#     last_el = None  # последний элемент, который мы просмотрели
#
#     # идём по элементам списка
#     for el in lst + [0]:  # [0] - это ручной триггер для обработки последнего элемента
#
#         if last_el != el:  # если произошла смена 0 на 1 или наоборот
#             if el == 0:  # если это была смена 1 на 0
#
#                 # пример: subranges == [(0, 2), (1, 2), (0, 1), (1, 2)]
#                 # у нас произошла смена 1 на 0, до смены единица шла 2 раза
#                 # (см последний элемент subranges) - проверяем, вдруг это
#                 # максимальная длина
#                 try:
#                     last_ones_length = subranges[-1][1]
#                     max_ones_length = max(last_ones_length, max_ones_length)
#                 except IndexError:
#                     pass
#
#                 # а может если мы удалим один ноль между элементами 1 и 3,
#                 # то получится более длинная последовательность единиц?
#                 try:
#                     gap_length = subranges[-2][1]
#                     if gap_length == 1:
#                         combined_ones_length = subranges[-1][1] + subranges[-3][1]
#                         max_ones_length = max(combined_ones_length, max_ones_length)
#                 except IndexError:
#                     pass
#
#             # добавляем новый счётчик последовательности в subranges
#             subranges.append((el, 1))
#         else:
#             # увеличиваем счётчик последней последовательности на 1
#             subranges[-1] = (el, subranges[-1][1] + 1])
#
#             last_el = el
#
#             # костыль, граничное условие
#             if len(subranges) == 2 and subranges[1][1] == 1:
#                 return subranges[0][1] - 1
#
#     return max_ones_length


def max_ones_length(lst):
    max_length = 0

    last_el = None
    current_length = 0
    groups = []

    for i in range(len(lst)):
        el = lst[i]
        if el == 1:
            current_length += 1
        else:
            next_i = i + 1
            if next_i < len(lst):
                next_el = lst[next_i]


data = [0, 0, 1, 1, 0, 1, 1, 0]
max_ones_length(data)

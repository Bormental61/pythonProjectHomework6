# 5. Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры :
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"
# def list_pres(list):
#    new_list = list.sort()
#    for i in range(len.list):
#       if new_list

# def gr_str(start, end, last):
#     result = f"{start}" if start == end else f"{start}-{end}"
#     if not last:
#         result += ", "
#     return result
# def lst_compress(lst):
#     result = ''
#     sorted_lst = sorted(lst)
#     group_start, group_end, prev_el = None, None, None
#     for el in sorted_lst:
#         if group_start is None:
#             group_start = el
#         if prev_el is not None:
#             if el != prev_el + 1:
#                 group_end = prev_el
#                 result += gr_str(group_start, group_end, False)
#                 group_start = el
#         prev_el = el
#     result += gr_str(group_start, prev_el, True)
#     return result
#
# lst = [1, 4, 5, 2, 3, 9, 8, 11, 0]
# print(lst)
# print(lst_compress(lst))
#
# lst = [1,4,3,2]
# print(lst)
# print(lst_compress(lst))
#
# lst = [1,4]
# print(lst)
# print(lst_compress(lst))

# 6. Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

# import re
# def rle_crypt(in_str):
#     crypt = ''
#     i = 0
#     while i < len(in_str):
#         count = 1
#         while i + 1 < len(in_str) and in_str[i] == in_str[i + 1]:
#             count += 1
#             i += 1
#         crypt += in_str[i] + str(count)
#         i += 1
#     return crypt
#
# input_str = input('Введите строку: ')
# pattern = re.search('[A-Z]', input_str)
# if not pattern:
#     print('Введена неверная строка!')
# else:
#     print(rle_crypt(input_str))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

list_1 = [random.randint(0, 10) for _ in range(10)]
print(list_1)

min_number = int(input('Введите минимальное значение: '))
max_number = int(input('Введите максимальное значение: '))

list_index = []
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        list_index.append(i)
print(list_index)

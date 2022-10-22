# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

# lst = [2, 3, 5, 9, 3]

# # lst = []
# # for i in range(11):
# #     lst.append(randint(-10,10)) # добавляется новый элемент в список
# print(lst)
lsts = [randint(-i,i) for i in range(6)]

# sum = 0

# for n in range(len(lst)):
#     if n%2 != 0:
#         sum = sum + int(lst[n])
#         print("нечетное =",int(lst[n]))
# print(sum)

# НОВОЕ РЕШЕНИЕ:

# from random import randint
# lst = [randint(-i,i) for i in range(6)]

lst = [2, 3, 5, 9, 3]
sum = 0

# b = [int(lst[n]) for n in range(len(lst)) if n%2 != 0 ]
# [sum := sum + x for x in b]

[sum := sum + x for x in [int(lst[n]) for n in range(len(lst)) if n % 2 != 0 ]]

print(sum)

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным з
# начением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

lst = [1.1, 1.2, 3.1, 5, 10.01] 
# lst : float = []

# for i in range(11):
#     lst.append((round(random.uniform(-10.0,10.0),3))) # добавляется новый элемент в список
# print(lst)

# lst_new = []
# drob = 0.00

# for i in range(len(lst)):
#     drob = lst[i]-int(lst[i])
#     if drob !=0: # добавление для проверки наличия дробной части
#         lst_new.append(round(drob,3)) # добавляется новый элемент в список
# print(lst_new)

# max_ = lst_new[0]
# min_ = lst_new[0]
# for i in range (len(lst_new)):
#     if lst_new[i]>max_:
#         max_= lst_new[i]
#     if lst_new[i]<min_:
#         min_ = lst_new[i]
# sub_ = max_ - min_
# print("разница между максимальным ", max_,"и минимальным значением",min_, " равна: " , sub_)

# [1.1, 1.2, 3.1, 5, 10.01] => 0.2 потому что дробная часть 5 равна 0 ведь список вещественных чисел
# но раз считается, что должен быть 0.19 ответ, значит будем считать что у числа 5 нет дробной части, 
# и список не полностью вещественный

# НОВОЕ РЕШЕНИЕ:

b = [round(lst[i] - int(lst[i]) , 3)  for i in range(len(lst)) if lst[i] - int(lst[i]) !=0]
maks = max(b)
minn = min(b)
print ("макс = ", maks,"мин = ", minn,"равна = ", maks - minn)
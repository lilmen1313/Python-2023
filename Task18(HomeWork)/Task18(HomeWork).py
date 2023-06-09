# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите количество элементов в списке: "))
list_1 = []
from random import randint
for i in range(n):
    a = randint(-10, 10)
    list_1.append(a)
print(list_1)
x = int(input("Введите число Х: "))

new_list = list()
for i in range(n):
    diff = abs(list_1[i] - x)
    new_list.append(diff)

min_diff = new_list[0]
for j in range(0, n):
    if new_list[j] < min_diff:
        min_diff = new_list[j]

result = list_1[new_list.index(min_diff)]
print(f"Самый близкий по величине элемент к числу {x} --> {result}")
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def CreateListRnd(size ,min_value, max_value):
    from random import randint
    list_1 = [randint(min_value, max_value) for i in range(size)]
    return list_1

min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
list_new = CreateListRnd(10, 1, 50)
print(list_new)

for i in range(len(list_new)):
    if max > list_new[i] > min:
        print(i, end= " ")
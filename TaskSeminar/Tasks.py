#Вывод Да если число четырехзначное, НЕТ в противном случае

# number = int(input("Введите целое число: "))
# if 999 < number < 10000 or -999 > number > -10000:
#     print("YES")
# else:
#     print("NO")

#Описание введеного числа(четность, +/-, 0)
# number = int(input("Введите целое число: "))
# if number % 2 == 0 and number > 0:
#     print("Положительное четное число")
# elif number % 2 != 0 and number > 0:
#     print("Положительное нечетное число")
# elif number % 2 == 0 and number < 0:
#     print("Отрицательное четное число")
# elif number % 2 != 0 and number < 0:
#     print("Отрицательное нечетное число")

#Задача с машиной
# n = int(input('Введите скорость машины (км/день):'))
# m = int(input('Введите длину маршрута (км):'))
# m = -m
# result = -(m // n)
# print(f'Машине потребуется {result} дня(-ей) для преодоления маршрута длиной {-m} км')

###ЦИКЛЫ FOR, WHILE###
# Задача №9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input('Введите целое неотрицательное число: '))
# i = 1
# multi = 1
# while i <= n:
#     multi *= i
#     i += 1
# print(f"Факториал {n} равен {multi}")

# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input:     5 Output:  6

# a = int(input('Введите целое число (A > 1): '))

# a1 = 0
# a2 = 1
# a3 = a1 + a2
# count = 3

# while a3 < a:
#     a1 = a2
#     a2 = a3
#     a3 = a1 + a2
#     count += 1
# if a3 == a:
#     print(count)
# else:
#     print(-1)

# Задача №13. Решение в группах Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая 
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись 
# исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50 
# Input:    6 -> -20 30 -40 50 10 -10 Output: 2

# n = int(input('Введите количество рассматриваемых дней (1 ≤ N ≤ 100): '))
# from random import randint
# count = 0

# if 1 <= n <= 100:
#     for i in range(1, n+1):
#         t = randint(-50, 50)
#         print(t, end=' ')
#         if t > 0:
#             count += 1
    
#     print(f"\nКоличество дней оттепели равно {count}")
# else:
#     print("Введено неверное количество дней!")


# Задача №15. Решение в группах 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает 
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза 
# Input:5 -> 5 1 6 5 9 Output:1 9

# n = int(input('Введите количество арбузов: '))
# from random import randint

# for i in range(1, n + 1):
#     m = randint(1, 15)
#     print(m)
#     if i == 1:
#         max = m
#         min = m
#     if i > 2:
#         if m > max:
#             max = m
#         else:
#             if m < min:
#                 min = m
# print(f"MAX - {max}, MIN - {min}")

#  17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# n = int(input("Введите количество элементов в списке: "))
# list_1 = list()
# from random import randint

# for i in range(n):
#     list_1.append(randint(1, 5))
# print(list_1)
# new_list = []
# for el in list_1:
#     if el not in new_list:
#         new_list.append(el)
# print(f"Количество различных чисел равно {len(new_list)}")

# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# n = int(input("Введите количество элементов в списке: "))
# k = int(input("Введите число К: "))
# list_1 = list()
# from random import randint
# for i in range(n):
#     list_1.append(randint(1, 9))
# print(list_1)
# list_richt = list_1[len(list_1)-k:]
# list_left = list_1[:n-k]
# list_1 = list_richt + list_left
# print(list_1)

# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# n = int(input("Введите количество элементов в списке: "))
# list_1 = []
# from random import randint
# count = 0
# for i in range(n):
#     list_1.append(randint(-15, 15))
#     if i > 0:
#         if list_1[i-1] < list_1[i]:
#             count += 1
# print(list_1)
# print(count)


# Множетсва (set) - работают намного быстроее списков (List) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import random
# import time
#
# some_set = set()
# for _ in range(10 ** 6):
# some_set.add(random.randint(100, 1100))
# some_list = list(some_set)
#
# start = time.perf_counter()
# print(99 in some_list)
# end = time.perf_counter()
# first_duration = end - start
#
# start = time.perf_counter()
# print(99 in some_set)
# end = time.perf_counter()
# second_duration = end - start
# print(first_duration / second_duration)


# Словари ('key':'value')
# some_dict = {'яблоко': 'apple', 'виноград': 'grape', 'банан': 'ban'}
# some_dict['банан'] = 'banana'
# print(some_dict['виноград'])

# for i in some_dict:
#     print(i, some_dict[i])

# for j in some_dict.values():
#     print(j)

# for i in sorted(some_dict):
#     print(i, some_dict[i])

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским 
# алфавитом очки распределяются так: 
# ●A, E, I, O, U, L, N, S, T, R – 1 очко; 
# ●D, G – 2 очка; 
# ●B, C, M, P – 3 очка;
# ●F, H, V, W, Y – 4 очка;
# ●K – 5 очков; 
# ●J, X – 8 очков; 
# ●Q, Z – 10 очков. 

# А русские буквы оцениваются так:
# ●А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# ●Д, К, Л, М, П, У – 2 очка; 
# ●Б, Г, Ё, Ь, Я – 3 очка; 
# ●Й, Ы – 4 очка; 
# ●Ж, З, Х, Ц, Ч – 5 очков; 
# ●Ш, Э, Ю – 8 очков; 
# ●Ф, Щ, Ъ – 10 очков. 

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# word = tuple(input("Введите слово: ").upper())
# print(word)

# count = 0
# for i in word:
#     if i in point1:
#         count += 1
#     elif i in point2:
#         count += 2
#     elif i in point3:
#         count += 3
#     elif i in point4:
#         count += 4
#     elif i in point5:
#         count += 5
#     elif i in point8:
#         count += 8
#     elif i in point10:
#         count += 10
# print(f"Количество очков = {count}")

# word = input("Введите слово: ").upper()
# dict_rus = {'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1, 'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2, 'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3, 'Й':4, 'Ы':4, 'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5, 'Ш':8, 'Э':8, 'Ю':8, 'Ф':10, 'Щ':10, 'Ъ':10}
# count = 0
# for i in word:
#     count += dict_rus[i]
# print(count)

# Задача №25. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый 
# символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

# import time
# a = input("Введите предлеожение: ")

# start = time.perf_counter()
# a = list(a)
# dict_new = {}
# for i in a:
#     if i == " ":
#         a.remove(i)
# for i in a: 
#     if i not in dict_new:
#         dict_new[i] = 1
#     else:
#         dict_new[i] += 1
# for j in dict_new:
#     print(f"{j} - {dict_new[j]}")
# end = time.perf_counter()
# result_time = end - start
# print(result_time)

# Рекурсия

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(6))

# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные 
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# from random import randint

# a = int(input("Введите оценок в классном журнале: "))
# list_new = []
# for _ in range(a):
#     list_new.append(randint(1, 5))
# print(list_new)
# for i in range(a):
#     if list_new[i] == min(list_new):
#         list_new.insert(i, max(list_new))
#         list_new.pop(i+1)
# print(list_new)

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии

# def exponentiation(a, b):
#     if b == 0:
#         return 1
#     return a * exponentiation(a, b-1)

# a = int(input("Введите число А: "))
# b = int(input("Введите число В: "))
# print(exponentiation(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a - 1, b +1 )

# a = int(input("Введите число А: "))
# b = int(input("Введите число В: "))
# print(sum(a, b))

# Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве 
# определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.  (каждое число вводится с новой строки)

# from random import randint
# n = int(input("Введите кол-во элементов в списке: "))

# list_new = []

# for _ in range(n):
#     # list_new.append(randint(1, 20))
#     list_new.append(int(input("Введите элемент: ")))
# print(list_new)

# count = 0
# for i in range(1, n):
#     if list_new[i-1] < list_new[i] and list_new[i+1] < list_new[i]:
#         count +=1
# print(count)

# Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными, если сумма 
# делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз 
# (перестановка чисел новую пару не дает).

# k = 1500 #int(input("Введите k: ")) 
# list_k = [i for i in range(3, k+1)] 
# print(list_k) 

# printed_numbers = set()

# sum_of_divisors = [] 
# for i in range(len(list_k)): 
#     sum_div = 1 
#     for div in range(2, list_k[i]): 
#         if list_k[i] % div == 0: 
#             sum_div += div 
#     sum_of_divisors.append(sum_div) 
# print(sum_of_divisors) 
 
# for y in range(len(sum_of_divisors)): 
#     for h in range(len(list_k)): 
#         if sum_of_divisors[y] == list_k[h] and sum_of_divisors[h] == list_k[y] and y != h:
#             if list_k[h] not in printed_numbers and list_k[y] not in printed_numbers:
#                 print(list_k[h], list_k[y])
#                 printed_numbers.add(list_k[h])
#                 printed_numbers.add(list_k[y])

# Функции высшего порядка 

# def sq1(x):
# print(x ** 2)
#
#
# print(sq1(10))
#
# def sq2(x):
# return x ** 2
#
#
# print(sq2(20))

# def c(x):
# return x ** 3
#
#
# some_list = [1, 2, 3, 4, 5]
#
# new_list = []
#
# for el in some_list:
# new_list.append(c(el))
#
# print(new_list)

# def c(x):
#     return x ** 3

# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, some_list))
# print(new_list)

# def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)

# import random
#
# some_list = []
# for _ in range(100): # 0, 1, 2, 3, 4, 5, 6, 7... 99
# number = random.randint(1, 10)
# if number % 2 == 0:
# some_list.append(number)
#
#
# some_list = [random.randint(1, 10) for _ in range(100)]
#
# some_list = [int(input()) for _ in range(int(input()))]

# Задача №47. Решение в группах У вас есть код, который вы не можете менять (так часто бывает, когда код в 
# глубине программы используется множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список 
# transormed_values = list(map(transformation, values)) 
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. 
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation = lambda i: i
# transormed_values = list(map(transformation, values))
# print(values)
# print(transormed_values)


# Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, 
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды 
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, 
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - 
# полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: 
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, 
# что самая далекая планета ровно одна

# def CreateTupleFloat(size ,min_value, max_value):
#     import random
#     return tuple([round(random.random()*(max_value - min_value) + min_value, 2) for _ in range(size)])

# def find_farthest_orbit(list_of_orbits):
#     import math
#     list_1 = []
#     for el in list_of_orbits:
#         if el[0] != el[1]:
#             list_1.append(el[0] * el[1] * math.pi)
#         else:
#             list_1.append(0)
#     print(list_1)
#     return list_of_orbits[list_1.index(max(list_1))]

# siz = int(input("Введите кол-во планет: "))
# orbits = [CreateTupleFloat(2, 5, 20) for _ in range(siz)]
# orbits = [(1, 3), (2, 2), (1.5, 2), (6, 6), (12, 78)]
# print(orbits)
# print(find_farthest_orbit(orbits))

# Задача №51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
# одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# def CreateListRnd(size ,min_value, max_value):
#     from random import randint
#     return [randint(min_value, max_value) for i in range(size)]

# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(objects) == len(new_objects) or len(new_objects) == 0: 
#         return True
#     return False

# # values = CreateListRnd(5, 2, 16)
# values = [2, 4, 8, 88, 6]
# print(values)
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
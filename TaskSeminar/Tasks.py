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
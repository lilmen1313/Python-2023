# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def primeNumber(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("No")
#                 break
#         else:
#             print("Yes")

# n = int(input("Введите число: "))
# primeNumber(n)

def primeNumbers(n, i = 2):
    if i != n:
        if n % i == 0:
            return "NO"
        return primeNumbers(n, i + 1)
    return "YES"

n = int(input("Введите число: "))
print(primeNumbers(n))
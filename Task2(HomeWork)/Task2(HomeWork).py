# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите число: '))
sum = 0
while number != 0:
    if number > 0:
        sum = sum + number % 10
        number = int(number / 10)
    else:
        number = -number
        sum = sum + number % 10
        number = int(number / 10)
print(sum)
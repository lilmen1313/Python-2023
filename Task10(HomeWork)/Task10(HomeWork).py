# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите 
# минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
from random import randint
count0 = 0
count1 = 0

if n > 1:
    for i in range(1, n+1):
        t = randint(0, 1)
        print(t, end=' ')
        if t == 0:
            count0 += 1
        if t == 1:
            count1 += 1
    if count0 < count1:
        print(f"\nНужно перевернуть {count0} монет(-у, -ы)")
    else:
        print(f"\nНужно перевернуть {count1} монет(-у, -ы)")
else:
    print("Попрубуй снова")
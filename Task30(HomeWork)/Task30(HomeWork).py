# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(a1, diff, count):
    an = a1 + (count - 1)*diff
    list_1 = [i for i in range(a1, an + 1, diff)]
    return list_1

print(arithmetic_progression(7, 2, 5))
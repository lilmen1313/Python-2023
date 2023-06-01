# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите кол-во столбцов: '))
m = int(input('Введите кол-во строк: '))
k = int(input('Введите кол-во долек, которые хотите отломить: '))

if k % n == 0 and k >= n:
    flag = True
    i = 1
    while flag or i <= m:
        multi = i * n
        if multi == k:
            print("YES")
            flag = False
        i += 1
elif k % m == 0 and k >= m:
    flag = True
    i = 1
    while flag or i <= n:
        multi = i * m
        if multi == k:
            print("YES")
            flag = False
        i += 1
else:
    print("NO")
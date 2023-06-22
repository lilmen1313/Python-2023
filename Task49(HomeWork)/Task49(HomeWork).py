# Задача №49. Решение в группах Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1.Программа должна выводить данные 
# 2.Программа должна сохранять данные в текстовом файле 
# 3.Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека) 
# 4.Использование функций. Ваша программа не должна быть линейной

def imp(): #вход
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open("C:/Users/lilme/Desktop/TESTING(Seminar)/1. Знакомство с языком Python (семинары)/Task49(HomeWork)/directory.txt", 'a', encoding='UTF-8') as file:
        file.write(f"\n{surname}\n{name}\n{patronymic}\n{phone_number}\n")

def exp():
    surname = input("Введите фамилию: ")
    with open("C:/Users/lilme/Desktop/TESTING(Seminar)/1. Знакомство с языком Python (семинары)/Task49(HomeWork)/directory.txt", 'r', encoding='UTF-8') as file:
        f = file.read().split()
        for i in range(len(f)):
            if f[i] == surname:
                print(f"{f[i]}\n{f[i+1]}\n{f[i+2]}\n{f[i+3]}\n")

mode = int(input("Введите режим работы со справочником:\n1 - ввод нового контакта;\n2 - поиск контакта по фамилии\n"))
if mode == 1:
    imp()
elif mode == 2:
    exp()
else:
    print("Введён неверный режим работы, повторите попытку")
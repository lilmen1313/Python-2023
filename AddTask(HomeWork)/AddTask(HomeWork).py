# Доп. задача:
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте. НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ МЕТОД SPLIT

word = input("Введите предложение: ")

list_new = []
el = ""
for i in word:
    if i != " ":
        el += i
    else:
        if el != "":
            list_new.append(el)
            el = ""
        continue
else:
    list_new.append(el)
print(list_new)
print(len(set(list_new)))
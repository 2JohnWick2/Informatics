'''
1. Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». Преобразовать ее, заменив точками все восклицательные знаки.
'''
'''a = str(input("Введитпе строку: "))
total = 1
mx = -1

for i in range(len(a)-1):
    if a[i] == a[i + 1 ] == "н":
        total += 1
        long = max(mx, total)
    if a[i] != a[i + 1] != "н":
        total = 1
a = a.replace("!", ".")
print("Самая длинная последовательность н:", long, "Новая строка: ", a )
'''

'''
2. Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. Вывести на экран все символы, расположенные внутри этих скобок.
'''
'''a = str(input("Введите строку: "))
for i in range(len(a)):
    if a[i] == "(":
        b = a[i +1 : len(a)]
        for g in range(len(b)):
            if b[g] == ")":
                c = b[0 : g]
print(c)
'''

'''
3. Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я". Например: Абстракция, авария, аллея.
'''
a = str(input("Введите строку: "))
word = a.split()
result = []
for i in word:
    if i.lower()[0] == "а" and i.lower()[len(i) - 1] == "я":
        result.append(i)

for i in result:
    print(i, end=" " )
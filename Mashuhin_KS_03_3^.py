'''
1. Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно. Верхний предел должен вводиться с клавиатуры и не должен превышать числа 100.
'''
'''
n = int(input("Введите верхний предел числовой числовой последовательности:"))
n = min(n, 100) # ограничин верхний предел
summ = 0
for i in range(1, n+1):
    summ += i ** 3
print("Сумма кубов натуральных чисел от 1 до ", n, " равна:", summ)
'''

'''
2. Выведите на экран таблицу умножения чисел от одного до девяти.
'''
# Первый вариант решения
'''
length = 9  # определяем размеры таблицы
width = 9
for i in range(1, length + 1):
    for g in range(1, width + 1):
        print(i, "x", g, "=", i * g, end="\t")
    print()
'''

# Второй вариант решения
'''
for i in range(1, 10):
    for g in range(1, 10):
        print(i, "x", g, "=", i*g,)
'''

'''
3. Вывести алфавит 
'''
'''for i in range(0, 32):
    print("|", chr(i + 1040) + chr(i + 1072), end="|")

    if (i + 1) % 5 == 0:
        print()

'''
'''
4. Нарисовать прямоугольник с помощью символа @
'''
width = int(input("Введите ширину прямоугольника: "))
height = int(input("Введите высоту прямоугольника: "))

for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("@", end="")
        else:
            print(" ", end="")
    print()







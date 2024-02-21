# Постомтрите мой GitHub пожалуйста: https://github.com/2JohnWick2

'''
1. Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
'''

'''from random import randint
n = 3
arr = list()
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(randint(10, 80))
    arr.append(brr)
for i in range(n):
    for j in range(n):
       print(arr[i][j], end = ' ')
    print()

max_third_column = max(arr[0][2], arr[1][2], arr[2][2])
max_second_row = max(arr[1])

print(f"Максимальное значение среди элементов третьего столбца: {max_third_column}")
print(f"Максимальное значение среди элементов второй строки: {max_second_row}")
'''

'''
2. Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.
'''
'''from random import randint
n = int(input())
m = int(input())
arr = list()
print("Исходная матрица:")
for i in range(n):
    brr = list()
    for j in range(m):
         brr.append(randint(-15, 15))
    arr.append(brr)
for i in range(n):
    for j in range(m):
        print(arr[i][j], end= ' ')
    print()

new_arr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            new_arr[i][j] = 1
        if arr[i][j] < 0:
            new_arr[i][j] = 0
print("Новая матрица: ")
for i in range(n):
    for j in range(m):
        print(new_arr[i][j], end= ' ')
    print()
    '''

'''
3. Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
'''
'''from random import randint


def check(lister):
    summer = sum(lister[0])
    for s in lister:
        if summer != sum(s):
            return False
    for i in range(0, len(lister)):
        if summer != sum(lister[j][i] for j in range(0, len(lister))):
            return False
    return True


n = int(input('Введи порядок матрицы: '))
arr = [[randint(10, 80) for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
       print(arr[i][j], end = ' ')
    print()

if check(arr):
    print('Матрица является магическим квадратом')
else:
    print('Матрица не является магическим квадратом')
'''

'''
4. Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
'''
'''from random import randint

k = 0
n = int(input("Введите порядок матрицы: "))
arr = list()
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    for j in range(n):
       print(arr[i][j], end = ' ')
    print()

for i in range(n):
    for j in range(n):
        if j != i:
            if arr[i][j] == arr[j][i]:
                k += 1
if k == (n**2 - n):
    print("Матрица симметричная")
else: print("Мартица не симметричная")
'''

'''
5. Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
'''
'''from random import randint

n = int(input("Введите длину матрицы: "))
m = int(input("Введите ширину матрицы: "))
a = -999999999999
b = 999999999999
arr = list()

print("Исходная матрица:")
for i in range(n):
    brr = list()
    for j in range(m):
         brr.append(randint(-15, 15))
    arr.append(brr)
for i in range(n):
    for j in range(m):
        print(arr[i][j], end= ' ')
    print()
for j in range(n):
    summer_1 = min(sum(arr[j]), b)
    if b != summer_1:
        min_string = arr[j]
    b = summer_1
print(summer_1, min_string)
for i in range(n):
    summer_2 = max(sum(arr[i]), a)
    if a != summer_1:
        max_string = arr[i]
    a = summer_2
print(summer_2, max_string)
'''

'''
6. Дана действительная матрица размером n х m, все элементы которой различны. 
В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.
'''
from random import randint

def generator(n, m, current_list=[]):
    while len(set(current_list)) < n * m:
        current_list = [randint(-10 * (n * m), 10 *(n * m)) for _ in range(n * m)]
    return list(set(current_list))

n = int(input())
m = int(input())

print("Исходная матрица:")
arr = []
k = 0
for i in range(n):
    brr = []
    for j in range(m):
        brr.append(generator(n, m)[k])
        k += 1
    arr.append(brr)  

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
print()

total = 999999999999
print("Преобразованная матрица: ")
for i in range(n):
    total = min(arr[i])
    for j in range(m):
        if arr[i][j] == total:
            if total % 2 == 0:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
        print(arr[i][j], end=' ')
    print()


'''
1. Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры. В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.
'''
'''from random import randint
n = int(input("Введите длинну массива:"))
l = [randint(10, 80) for x in range(n)]
print(l)

def pr(a):
    a[0], a[-1] = a[-1], a[0]
    print(a)

pr(l)
'''

'''
2. Даны две дроби A/B и C/D (A, B, C, D - натуральные числа). Составить программу деления дроби на дробь. Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.
'''
'''a = int(input("Введите числитель первой дроби: "))
b = int(input("введите знаменатель первой дроби: "))
c = int(input("Введите числитель второй дроби: "))
d = int(input("Введите знаменатель второй дроби: "))
division_1 = a*d
division_2 = c*b

def ev(division_1, division_2):
    while division_1 != 0 and division_2 != 0:
        if division_1 >= division_2:
            division_1 = division_1 % division_2
        else:
            division_2 = division_2 % division_1
    return division_1 or division_2

print(division_1 / ev(division_1, division_2), "/", division_2 / ev(division_1, division_2))
'''

'''
3. Задана окружность (x-a)^2 + (y-b)^2 = r^2 и точки P(p1, p2), F(f1, f2), L(l1, l2). Выяснить и вывести на экран, сколько точек и какие лежить внутри окружности. Проверку сформировать в виде процедуры.
'''
import math
x = int(input("Ведите x: "))
y = int(input("Введите y: "))
a = int(input("Введите a: "))
b = int(input("Ведите b: "))
p1 = int(input("Координата p1: "))
p2 = int(input("Координаты p2: "))
f1 = int(input("Координаты f1: "))
f2 = int(input("Координаты f2: "))
l1 = int(input("Координаты l1: "))
l2 = int(input("Координаты l2: "))
r = math.sqrt(((x-a)**2) + ((y-b)**2))
rp = math.sqrt((p1**2) + (p2**2))
rf = math.sqrt((f1**2) + (f2**2))
rl = math.sqrt((l1**2) + (l2**2))
n = 0
def circle(x, y, name):
    global n
    if x < y:
        print(name)
        n += 1
circle(rp, r, "Точка, лежащая в окружности: P")
circle(rf, r, "Точка, лежащая в окружности: F")
circle(rl, r, "Точка, лежащая в окружности: L")
print("Количесво точек, вошедших в окружность: ", n)
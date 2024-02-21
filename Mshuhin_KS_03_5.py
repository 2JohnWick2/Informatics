'''
1. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.
'''
'''x1 = int(input("Координаты точки x1: "))
x2 = int(input("Координаты точки x2: "))
y1 = int(input("Координаты точки y1: "))
y2 = int(input("Коордитаны точки y2: "))
z1 = int(input("Координаты точки z1: "))
z2 = int(input("Координаты точки z2:"))
def dots(x1, x2, y1, y2, z1, z2):
    a = abs(x2) / abs(x1)
    j = abs(y2) / abs(y1)
    w = abs(z2) / abs(z1)
    if min(a,j,w) == a:
         print("X", "(", x1, ";", x2, ")")
    if min(a, j, w) == j:
         print("Y", "(", y1, ";", y2, ")")
    else:
         print("Z", "(", z1, ";", z2, ")")
print(dots(x1, x2, y1, y2, z1, z2))
'''

'''
2. Найти все простые наруральные числа, не прtвосходящие n, двоичная запись которых представляет собой полиндром, т.е. читается одинаково слева направо и справа налево.
'''
'''def is_prime(number):
    """Проверка числа на простоту."""
    
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def palindrome(number):
    """Проверка, является ли двоичное представление числа палиндромом."""
    
    number = bin(number)[2:]
    return number == number[::-1]


def find_primes_with_palindrome(n):
    """Поиск всех простых чисел до n, двоичное представление которых является палиндромом."""
    
    result = []
    
    for i in range(2, n + 1):
        if is_prime(i) and palindrome(i):
            result.append(i)
            
    return result


n = int(input("Введите число n: "))
print(find_primes_with_palindrome(n))
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

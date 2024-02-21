'''a = input("Введите первое целое число \n")
b = input("Введите второе целое число \n")
c = input("Введите третье целое число \n")

if a<b:
  if a<c:
    y=a
  else:
    y=c
else:
  if b<c:
    y=b
  else:
    y=c
print("Минимальное число ", y)
'''

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if numbers:
    sum(numbers)
    len(numbers)
    a = sum(numbers)/len(numbers)
    print("Среднее арифметическое: ", a)
else:
    print(0)
'''
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(sum(numbers)/len(numbers)) if numbers else print(0)

'''numbers = []
try:
    print(sum(numbers)/len(numbers))
except ZeroDivisionError:
    print(0)
'''

'''
Даны три числа. Выбрать из них те, которые принадлежат интервалу [1,3].
'''
'''a = float(input("Введмте первое число: "))
b = float(input("Введмте второе число: "))
d = float(input("Введмте третье число число: "))
if 1 <= a and a <= 3:
    print(a)
if 1 <= b and b <= 3:
    print(b)
if 1 <= d and d <= 3:
    print(d)
    '''
'''
Написать программу, решающую квадратные уравнения 
'''
import math
a = float(input())
b = float(input())
c = float(input())
d = (b**2 - (4*a*c))
print("d= ", d)
if d > 0:
    print((-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a))
if d == 0:
    print(-b/(2*a), 1)
if d < 0:
    print("Корней нет")


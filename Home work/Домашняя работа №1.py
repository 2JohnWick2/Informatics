print("Задача 1:")
import math
R = float(input("Введите радиус окружности в сантиметрах: R="))
l = round(2*math.pi*R,2)
S = round(math.pi*math.pow(R,2),2)
print("Длина окружности в сантиметрах: ",l)
print("Площадь круга в квадратных сантиметрах: ", S)

print("Задача 2:")
x = 10
y = 35
print("Значения переменных до замены: ", x,y)
x,y = y,x
print("Значения переменных после замены:", x,y)

 
print("Задача 3:")
import math
L= float(input("Введите значение длины маятника в метрах: L="))
g= 9.81
T = round(2*math.pi* math.sqrt(L/g), 2)
print("Значение периода колебаний маятника в секундах: ", T)

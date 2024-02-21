# Задание 1
import math

R = float(input("Введите радиус окружности в сантиметрах: R="))
l = round(2 * math.pi * R, 2)
S = round(math.pi * math.pow(R, 2), 2)
print("Длина окружности в сантиметрах: ", l)
print("Площадь круга в квадратных сантиметрах: ", S)

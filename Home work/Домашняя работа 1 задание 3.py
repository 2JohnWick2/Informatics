import math
L= float(input("Введите значение длины маятника в метрах: L="))
g= 9.81
T = round(2*math.pi* math.sqrt(L/g), 2)
print("Значение периода колебаний маятника в секундах: ", T)
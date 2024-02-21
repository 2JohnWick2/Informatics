import re

while True:
    a = str(input("Введите регистрационный номер: "))
    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$', a):
        print("Частный автомобиль")
    if re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$', a):
        print("Такси")
    else: print("Неверный номер")
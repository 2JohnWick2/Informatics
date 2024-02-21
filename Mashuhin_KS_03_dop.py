def m(arr, a, b): # функция для сжатия массива
    new_array = []
    for x in arr:
        if x < a or x > b:
            new_array.append(x)
    new_array += [0] * (len(arr) - len(new_array))
    return new_array

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Исходный массив:", array)
begin = float(input("Нижняя граница промежутка:"))
end = float(input("Ввержняя граница промежутка:"))
compressed_array = m(array, begin, end)
print("Сжатый массив: ", compressed_array)


def compute_expression(s):
    # Разделяем строку на отдельные элементы (числа с буквами)
    elements = s.split()

    # Извлекаем букву и соответствующее число из каждого элемента
    letters = []
    numbers = []
    for elem in elements:
        number = ""
        for char in elem:
            if char.isalpha():
                letters.append(char)
            else:
                number += char
        numbers.append(int(number))

    # Объединяем буквы и числа в пары, а затем сортируем их
    combined_data = list(zip(letters, numbers))
    sorted_data = sorted(enumerate(combined_data), key=lambda x: (x[1][0], x[0]))

    # Извлекаем отсортированные числа
    sorted_numbers = [x[1][1] for x in sorted_data]

    # Выполняем последовательность вычислений (+, -, *, /) на отсортированных числах
    result = sorted_numbers[0]
    operations = ['+', '-', '*', '/']
    for i in range(1, len(sorted_numbers)):
        operation = operations[(i-1) % 4]
        if operation == '+':
            result += sorted_numbers[i]
        elif operation == '-':
            result -= sorted_numbers[i]
        elif operation == '*':
            result *= sorted_numbers[i]
        else:
            result /= sorted_numbers[i]

    # Округляем результат до ближайшего целого числа и возвращаем
    return round(result)

# Проверяем функцию на приведенных примерах

print(compute_expression("24z6 1x23 y369 89a 900b"))  # 1299
print(compute_expression("24z6 1z23 y369 89z 900b"))  # 1414
print(compute_expression("10a 90x 14b 78u 45a 7b 34y"))  # 60

'''
ПРОВЕРЬТЕ ПОЖАЛУЙСТА МОЙ GitHub: https://github.com/2JohnWick2
'''

'''
Все пути файлов написаны для системы windows
'''

'''
1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
'''

'''n = int(input("Введите количество строк: "))
def read_last(lines, file):
    f = open(file, 'r', encoding='utf-8')
    d = f.readlines()
    dl = len(d)
    if lines <= 0 and n > dl:
        print('Неверное число строк')
        return
    for line in d[dl - n:]:
        print(line, end='')
    return


read_last(n, r'C:\Informatics\article.txt')
'''


'''
2. Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
'''
'''import os 


def print_docs(directory, level = 0):
    print('|' + '--' * level + directory)
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            print('|' + '--' * (level + 1) + name)
        else:
            print_docs(path, level + 1)


directory = input('Введи папку из C:\, которую я прочитаю: ')
print_docs(directory)
'''

'''
4. Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:

Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
Если строка пустая или спец. символ - программа сохраняет файл.
'''
def editor():
    file_name = input("Введите имя будущего файла (без расширения): ") + ".txt"
    with open(file_name, "w", encoding='utf-8') as file:
        while True:
            line = input("Введите строку(для сохранение нужно нажать ENTER): ")
            # Если строка пустая или содержит спец. символ, сохраняем файл и выходим
            if not line or line in ["!", "@", "#", "$", "%", "^", "&", "*"]:
                break
            file.write(line + "\n")
    print(f"Файл {file_name} успешно сохранен!")


editor()

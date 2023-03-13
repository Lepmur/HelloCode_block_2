# Дан список целых чисел. Нужно вывести список кортежей,
# состоящих из пар чётных чисел данного списка и их квадратов

my_list = [1, 2, 3, 5, 8, 15, 23, 38]

# # решение Comprehension
# print([(i, i**2) for i in my_list if i % 2 == 0])

# # решение через функции ===============lambda======================
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# res = select(int, my_list)
# res = where(lambda x: x % 2 == 0, res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# решение через функции lambda, map, filter
# res = map(int, my_list)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

#////////////////////////==MAP==////////////////////////////////////

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки.
# Как правильно превратить list строк в list чисел?

# решение Comprehension
# my_list = [int(i) for i in input('Enter numbers separated by spaces: ').split()]
# print(my_list, type(my_list[0]))
# # решение ===Map=== Comprehension
# my_list_1 = list(map(int, input('Enter numbers separated by spaces: ').split()))
# print(my_list_1, type(my_list_1[0]))

#////////////////////////==MAP==////////////////////////////////////

# data = [15, 65, 9, 36, 175]
# print(list(filter(lambda x: x % 10 == 5, data)))

#///////////////////////==ZIP==/////////////////////////////////////

users = ['Petya', 'Masha', 'Dasha', 'Glasha', 'Uebasha', 'Dima']
ids = [1, 2, 3, 4, 5, 6]
salary = [111, 222, 333]

print(list(zip(users, ids)))
print(list(zip(users, ids, salary))) # Пробегает по минимальному входящему набору

#//////////////////////==ENUMERATE==///////////////////////////////

users = ['Petya', 'Masha', 'Dasha', 'Glasha', 'Uebasha', 'Dima']
print(list(enumerate(users)))

#/////////////////////==ФАЙЛЫ==////////////////////////////////////

# режимы:
# a - добавление информации в файл (создаст)
# r - чтение информации из файла
# w - запись информации в файл(затирает старый, добавляет новый)
# w+ - запись в файл и чтение из него(если его нет, будет создан)
# r+ - открыть файл и дописать в него(если нет выдаст ошибку)

colors = ['red', 'green', 'blue']
data = open('lection_4.txt', 'a', encoding='utf-8') # кодировка utf-8 по умолчанию
data.writelines(colors) # разделителей не будет
data.close() # обязательно закрываем файл

with open('lection_4.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n') # добавит всё в рамках одной сессии

with open('lection_4.txt', 'r') as data:
    for line in data:
        print(line)

#/////////////////////==МОДУЛИ_OS==////////////////////////////////////

# import os
# os.chdir('path') - смена текущей директории
# os.getcwd() - текущая рабочая директория
# os.path.basename('path') - базовое имя пути
# os.path.abspath('path') - возвращает нормализованный абсолютный путь

#/////////////////////==SHUTIL==////////////////////////////////////

# import shutil
# shutil.copyfile(src, dst) - копирует содержимое файла src в dst (без метаданных)
# shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst
# shutil.rmtree(path) - удаляет текущую директорию и все поддиректории


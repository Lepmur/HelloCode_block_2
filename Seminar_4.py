# Напишите программу, которая принимает на вход строку и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов
# добавляется к символам с помощью постфикса формата _n.

# my_string = input("Enter the string: ")
# my_dict = dict()
# for item in my_string:
#     my_dict[item] = my_dict.get(item, 0) + 1
#     print(f'{item}_{my_dict[item]}')

# Пользователь вводит текст. Словом считается последовательность
# непробельных символов идущих подряд. Слова разделены одним или
# несколькими пробелами, или символами конца строки. Определите
# сколько различных слов содержится в этом тексте.

# text = input("Enter text: ")
# print(len(set(text.lower().split())))

# Написать программу которая состоит из 4 этапов:
# 1 - создаём список из рандомных 4-значных чисел,
# 2 - принимает с консоли цифру и удаляет её из всех элементов списка,
# 3 - цифры всех элементов суммирует, пока результат не станет однозначным числом,
# 4 - из финального списка убирает все дублирующиеся элементы
# пример:
# 1 - [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# 2 - 3, [264, 694, 7286, 5, 4602, 176, 796]
# 3 - 264 -> 12 -> 3, [3, 1, 5, 5, 3, 5, 4]
# 4 - [3, 1, 5, 4]

import random
my_list = [random.randint(1000, 9999) for _ in range(7)] # 1 stage
print(*my_list)
number_for_delete = input('Enter number for delete: ') # 2 stage
for i in range(len(my_list)):
    if number_for_delete in str(my_list[i]):
        my_list[i] = int(str(my_list[i]).replace(number_for_delete, ''))
print(*my_list)
for i in range(len(my_list)): # 3 stage
    while my_list[i] > 9:
        my_list[i] = sum(int(j) for j in str(my_list[i]))
print(*my_list)
print(*set(my_list)) # 4 stage

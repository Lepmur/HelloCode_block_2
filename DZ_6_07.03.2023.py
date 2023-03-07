# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import random

# first, length, difference = input('Enter first, length and difference of sequence in the format x y z : ').split()
# my_list = [int(first)]
# for i in range(1, int(length)):
#     my_list.append(my_list[i-1] + int(difference))
# print(my_list)

#  Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

array = [random.randint(0, 100) for _ in range(10)]
print(array)
first, last = input('Enter diapason in the format a b : ').split()
result = []
for i in range(len(array)):
    if int(first) <= array[i] <= int(last):
        result.append(i)
print(result)

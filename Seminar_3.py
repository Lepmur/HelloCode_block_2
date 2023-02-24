# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

import random

# my_list = [random.randint(0, 10) for _ in range(20)]
# print(my_list)
# shift = int(input('Enter number: '))
# # result = []
# # for i in range(len(my_list)):
# #     result.append(my_list[(i + shift) % len(my_list)])
# # print(result)
#
# for i in range(shift):
#     my_list.insert(0, my_list.pop(-1))
# print(my_list)

my_list = [random.randint(0, 10) for _ in range(20)]
print(my_list)
result = []
for item in my_list:
    if my_list.count(item) == 1:
        result.append(item)
print(result)






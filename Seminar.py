# a1 = 0
# a2 = 1
#
# number = int(input('Enter number: '))
# result = 0
# count = 2
#
# while result < number:
#     result = a1 + a2
#     a1 = a2
#     a2 = result
#     count += 1
# if result == number:
#     print(f'Yes, his number = {count}')
# else:
#     print(-1)




# import random
#
# ranger = int(input('Enter number: '))
# min_limit, max_limit = 1, 10
# max = min_limit
# min = max_limit
#
# for i in range(ranger):
#     a = random.randint(min_limit, max_limit)
#     print(a)
#     if a > max:
#         max = a
#     if a < min:
#         min = a
#
# print(f'мой арбуз весит {max}, арбуз тёщи весит {min}')


import random
temp = 0
days = 30
count = 0
count_max = 0
for i in range(days):
    temp += random.randint(-3, 3)
    print(temp, end=', ')
    if temp > 0:
        count += 1
        if count > count_max:
            count_max = count
    else:
        count = 0
print(f'\n period = {count_max}')

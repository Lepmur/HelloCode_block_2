# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def pow(number, base):
    return number * pow(number, base - 1) if base > 1 else number
print(f'A^B = {pow(int(input("Enter A: ")), int(input("Enter B: ")))}')

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(number_one, number_two):
    return 1 + sum(number_one, number_two - 1) if number_two > 0 else number_one
print(f'A + B = {sum(int(input("Enter A: ")), int(input("Enter B: ")))}')

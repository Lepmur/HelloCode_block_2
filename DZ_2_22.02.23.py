# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import math
import random

n = int(input('Enter quantity of coins: '))
heads = 0
tails = 0
for i in range(n):
    if random.randint(0, 1) == 0:           # допустим 0 это решка, 1 это орёл
        heads += 1
    else:
        tails += 1
print(f'You must be rotated at least {heads if heads < tails else tails} coins.')

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('You are Petya, made 2 numbers and tell me their sum: '))
p = int(input('You are Petya, made 2 numbers and tell me their product: '))
discriminant = s * s - 4 * p                 # D = a2 - 4ac
number_one_result = int((s + math.sqrt(discriminant)) / 2)
number_two_result = int((s - math.sqrt(discriminant)) / 2)
print(f'Katya guessed the numbers {number_one_result} and {number_two_result}.')

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

max = int(input('Enter number: '))
power_of_two = 2
while max >= power_of_two * 2:
    power_of_two *= 2
print(power_of_two if max >= power_of_two else 'no no no no... ;)')

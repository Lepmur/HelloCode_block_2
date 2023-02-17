# Найдите сумму цифр трехзначного числа.

number = int(input('Enter number: '))
result = int(number / 100) + int((number / 10) % 10) + int(number % 10)
print(result)

# Петя, Катя и Сережа вместе сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

amount = int(input('Enter amount of cranes: '))
if amount % 6 != 0:
    print('Someone lied!')
else:
    katya = amount / 1.5
    petya_or_sereja = amount / 6
    print(f'Katya made {int(katya)} cranes, Petya make {int(petya_or_sereja)} cranes, Sereja make {int(petya_or_sereja)} cranes')

# Вам требуется написать программу, которая проверяет счастливость билета.

number_ticket = int(input('Enter number of ticket: '))
left_side = int(number_ticket / 1000)    ## разбил на разные переменные для наглядности, конечно все эти вычисления можно было поместить прямо в IF
right_side = int(number_ticket % 1000)
left_sum = int(left_side / 100) + int(left_side % 100 / 10) + int(left_side % 10)
right_sum = int(right_side / 100) + int(right_side % 100 / 10) + int(right_side % 10)
if left_sum == right_sum:
    print('This ticket is happy!')
else:
    print('This ticket is not happy!')

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

side_a = int(input('Enter the first side of the chocolate: '))
side_b = int(input('Enter the second side of the chocolate: '))
desired_piece = int(input('How many pieces do you want? '))
if desired_piece % side_a == 0 or desired_piece % side_b == 0:
    print('It can be done')
else:
    print('That won\'t work')


# Методом рекурсии написать функцию возвращающую
# число фибонначи под заданным номером

def fibonnachi(n):
    if n < 3:
        return 1
    for i in range(n):
        return fibonnachi(n-2) + fibonnachi(n-1)
print(fibonnachi(30))

#=========================================================
# Напишите программу которая принимает на вход число
# и проверяет является ли оно простым

def simple_number(n):
    for i in range(3, n//2, 2):
        if not n % i:
            return False
    return True
number = int(input('Enter the simple number: '))
print(simple_number(number))

#=========================================================
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке
# Запрещено использовать списки и циклы

string = input('Enter string: ')
print(string[::-1])

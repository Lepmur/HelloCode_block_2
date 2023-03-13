# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

def quantity_vowels(text: str) -> int:
    vowels = 'аеёиоуыэюя'
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count

def check_poem(poem: str) -> bool:
    phrases = poem.split()
    quantity = quantity_vowels(phrases[0])
    for i in range(1, len(phrases)):
        if quantity_vowels(phrases[i]) != quantity:
            return False
    return True

print('Парам пам-пам!' if check_poem(input('Enter phrase: ')) else 'Ни**я себе!')


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        str = ""
        for j in range(1, num_columns + 1):
            str += f'{operation(i, j)} '
        print(str)

print_operation_table(eval(input('Enter function in the format "lambda x, y: x * y": ')))

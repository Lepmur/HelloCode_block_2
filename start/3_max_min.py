import random


numbers = [random.randint(-1000000, 1000000) for _ in range(0, int(input('Введите размер списка: ')))]

if numbers[0] > numbers[1]:
    max_number, min_number, max_index, min_index = numbers[0], numbers[1], 0, 1
else:
    max_number, min_number, max_index, min_index = numbers[1], numbers[0], 1, 0

for i in range(2, len(numbers)):
    max_number, max_index = (numbers[i], i) if max_number < numbers[i] else (max_number, max_index)
    min_number, min_index = (numbers[i], i) if min_number > numbers[i] else (min_number, min_index)

print(f"Максимальное число {max_number}[{max_index}]. Минимальное число {min_number}[{min_index}]")

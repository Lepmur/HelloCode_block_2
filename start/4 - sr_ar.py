import random

numbers = [random.randint(-1000, 1000) for _ in range(0, int(input("Введите количество чисел: ")))]

print(f"Даны числа", *numbers, f"\nСреднее арифметическое этих чисел = {sum(numbers) / len(numbers)}")

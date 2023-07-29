import random

my_list = [random.randint(-10, 10) for _ in range(0, 10)]
print(my_list)


def quadro_sorted(array: list[int]) -> list[int]:
    return sorted([number ** 2 for number in array])


print(quadro_sorted(my_list))


def max_of_third(array: list[int], k: int) -> list[int]:
    result = []
    for i in range(0, len(array) - k + 1):
        result.append(max(array[i], array[i + 1], array[i + 2]))
    return result


print(max_of_third(my_list, 3))


my_list_mono_up = [1, 2, 3, 6, 9]
my_list_mono_down = [9, 8, 7, 5, 1]


def check_mono(array: list[int]) -> bool:
    if array[-1] > array[-2]:
        for i in range(1, len(array) - 1):
            if array[i] < array[i-1]:
                return False
    if array[-1] < array[-2]:
        for i in range(1, len(array) - 1):
            if array[i] > array[i-1]:
                return False
    return True


print(check_mono(my_list_mono_up))
print(check_mono(my_list_mono_down))
print(check_mono(my_list))


import random
indexes = {}
indexes[0] = '\u2070'
indexes[1] = '\u00B9'
indexes[2] = '\u00B2'
indexes[3] = '\u00B3'
indexes[4] = '\u2074'
indexes[5] = '\u2075'
indexes[6] = '\u2076'
indexes[7] = '\u2077'
indexes[8] = '\u2078'
indexes[9] = '\u2079'
# first equation generation
n_1 = int(input('Enter the maximum degree of the first equation: '))
multipliers_1 = [random.randint(1, 9) for _ in range(n_1+1)]
equation_1 = ""
for i in range(n_1-1):
    equation_1 += f'{multipliers_1[i] if multipliers_1[i] > 1 else ""}x{indexes[n_1-i]} + '
equation_1 += f'{multipliers_1[-2] if multipliers_1[-2] > 1 else ""}x + {multipliers_1[-1]} = 0'
print(equation_1)
# second equation generation
n_2 = int(input('Enter the maximum degree of the second equation: '))
multipliers_2 = [random.randint(1, 9) for _ in range(n_2+1)]
equation_2 = ""
for i in range(n_2-1):
    equation_2 += f'{multipliers_2[i] if multipliers_2[i] > 1 else ""}x{indexes[n_2-i]} + '
equation_2 += f'{multipliers_2[-2] if multipliers_2[-2] > 1 else ""}x + {multipliers_2[-1]} = 0'
print(equation_2)
# addition of two equations
if n_1 > n_2:
    n_max, n_min, multipliers_max, multipliers_min = n_1, n_2, multipliers_1, multipliers_2
else:
    n_max, n_min, multipliers_max, multipliers_min = n_2, n_1, multipliers_2, multipliers_1
for i in range(len(multipliers_max)-n_min-1, len(multipliers_max)):
    multipliers_max[i] += multipliers_min[i - (n_max-n_min)]
equation_result = ""
for i in range(n_max-1):
    equation_result += f'{multipliers_max[i]}x{indexes[n_max-i]} + '
equation_result += f'{multipliers_max[-2]}x + {multipliers_max[-1]} = 0'

print(f'Result: \n{equation_result}')


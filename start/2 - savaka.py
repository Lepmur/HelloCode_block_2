range = 10000
speed_hum_1 = 1
speed_hum_2 = 2
speed_dog = 5
score_dog = 0
go_to_first = True
range_limit = 10

while range > range_limit:
    if go_to_first:
        speed = speed_dog + speed_hum_1
        go_to_first = False
    else:
        speed = speed_dog + speed_hum_2
        go_to_first = True
    time = range / speed
    range = range - time * (speed_hum_1 + speed_hum_2)
    score_dog += 1

print(f"Собака успеет пробежать {score_dog} раз.")

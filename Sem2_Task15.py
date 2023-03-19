# 2) Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint
n = int(input("Введите количество арбузов для выбора: "))
minimum = 100
maximum = 0
i = 0
while i < n:
    melon = randint(1, 20)
    print(melon)
    if melon < minimum:
        minimum = melon
    elif melon > maximum:
        maximum = melon
    i+=1
print()
print(minimum, maximum)
print()


# from random import randint

# watermelon = int(input("введите количество арбузов: "))
# max = randint(1, 50)
# print(max)
# min = max
# for i in range(watermelon-1):
# x = randint(1, 50)
# print(x)
# if max < x:
# max = x
# elif min > x:
# min = x
# print(f"самый тяжелый арбуз весит {max} кг, а самый легкий {min} кг")
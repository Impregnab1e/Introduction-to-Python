# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 > 1 2 4 8

n = int(input('Введите число N: '))
mainNumber = 2
i = 0
number = 0

while number < n:
    number = mainNumber**i
    i+=1
    if number < n:
        print (number)


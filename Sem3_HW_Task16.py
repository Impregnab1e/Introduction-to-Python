# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

n = int (input("Введите количество элементов в массиве: "))
x = int (input("Введите искомое число: "))
counter = 0

elements = [randint(1, 10) for _ in range(n)]
print(elements)
for i in range(n):
    if elements[i] == x:
        counter += 1
print(f"Число {x} встречается {counter} раза")


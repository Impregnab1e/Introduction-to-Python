# # Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstElement = int(input("Введите первый элемент:  "))
step = int(input("Введите шаг прогрессии:  "))
n = int(input("Введите количество элементов на выходе:  "))

array1 = []

for i in range(n):
    array1.append(firstElement)
    firstElement += step
print(array1)

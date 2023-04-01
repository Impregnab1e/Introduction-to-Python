# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# list_num = input('Введите список чисел: ').split()
# counter = 0
# for i in range(len(list_num) - 1):
#     num = list_num[i + 1:].count(list_num[i])
#     counter += num
# print(f'Количество пар элементов: {counter}')

array1 = [int(i) for i in input().split()]
print(array1)
count = 0
for i in range(len(array1)-1):
    for j in range(i+1,len(array1)-1):
        if array1[i] == array1[j] and array1[i+1]==array1[j+1]:
            count += 1

print(count)
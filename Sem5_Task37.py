# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def max_new (n,f):
#     if n==0:
#         print(f)
#         print(f[::-1])
#         return
#     f+=input("Введите элемент = ")+ " "
#     return max_new(n-1,f)
# n=int(input("число = "))
# max_new(n, "")

# def f(n):
#     if n == 0:
#         print()
#         return
#     k = int(input())
#     f(n-1)
#     print(k, end=' ')
# n = int(input())
# f(n)

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'
#$ return f(n-1) + ' ' + str(k)
n = int(input())
print(f(n)[1:])
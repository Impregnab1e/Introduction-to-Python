# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def power_number(A, B):
    if B == 1:
        return A
    return A * power_number(A, B-1)


A = int(input("Введите число A = "))
B = int(input("Введите число B = "))
print(power_number(A, B))

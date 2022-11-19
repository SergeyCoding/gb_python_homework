# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random


def generate_matrix(n: int):
    result = list()

    for _ in range(n):
        result.append(list(random.randint(1, 100) for _ in range(n)))

    return result


def print_matrix(matrix: list):
    for row in matrix:
        print(row)


print("Семинар 8. Задача 2")

number = int(input("Введите размер матрицы: "))

if number < 1:
    print("Ошибка!!! Проверьте введенные данные")
    exit()

m = generate_matrix(number)
print("\nМатрица:")
print_matrix(m)
print()

sum_diag = sum(list(m[i][i] for i in range(number)))
print(f"сумма диагонали: {sum_diag}")
sum_rows = list(sum(row) for row in m)
print(f"Суммы строк: {sum_rows}")


for i in range(number):
    if sum_rows[i] > sum_diag:
        print(f"{i+1} строка")

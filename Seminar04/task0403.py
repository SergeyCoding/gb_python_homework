# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
# 3 -> 3.142
# 5 -> 3.14159

import math

print("Семинар 4. Задача 3")

number = int(input("Number: "))

print(round(math.pi, number))
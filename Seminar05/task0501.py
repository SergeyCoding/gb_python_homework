# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random


print("Семинар 5. Задача 1")

number = int(input("Количество чисел: "))

lst = list(random.randint(1, 10) for _ in range(number))
print(lst)
print(list(filter(lambda x: x > 5, lst)))

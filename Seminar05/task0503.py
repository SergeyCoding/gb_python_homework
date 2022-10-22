# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]


import random


print("Семинар 5. Задача 3")

number = int(input("Количество чисел: "))

lst = list(random.randint(1, 10) for _ in range(number))
print(lst)

print()

lst_uniq = dict.fromkeys(lst, 0)

for el in lst:
    lst_uniq[el] += 1

cnt = sum(list(v for (_, v) in lst_uniq.items() if v > 1))
print(f"Совпадают: {cnt}")
print(f"Уникальные: {list(lst_uniq.keys())}")

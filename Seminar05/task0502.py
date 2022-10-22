# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


import random


print("Семинар 5. Задача 2")

number = int(input("Количество чисел: "))

lst = list(random.randint(1, 10) for _ in range(number))
print(lst)

print()

# убрать одинаковые рядом стоящие числа
enum = filter(lambda x: x[0] != x[1], zip(lst, lst[1:]+[None]))
lst = list(map(lambda x: x[0], enum))

result = []
for i in range(len(lst)-1):
    el = lst[i]
    local_result = [el]
    for j in range(i, len(lst)):
        if lst[j] > el:
            el = lst[j]
            local_result.append(el)
    result.append(local_result)

for ls in filter(lambda x: len(x) > 1, result):
    print(ls)

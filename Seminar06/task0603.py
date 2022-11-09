# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import random


print("Семинар 6. Задача 3")

number = int(input("Количество чисел: "))

lst = list(random.randint(1, 10) for _ in range(number))
print(lst)
print(list(filter(lambda x: x > 5, lst)))

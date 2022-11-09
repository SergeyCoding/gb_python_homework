# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

print("Семинар 6. Задача 3")

max_denominator = 11


def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


lst = []

for denominator in range(2, max_denominator+1):
    lst += [(numerator, denominator) for numerator in range(1, denominator)]

print(list(filter(lambda x: NOD(x[0], x[1]) == 1, lst)))

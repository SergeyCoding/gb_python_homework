# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

print("Семинар 4. Задача 1")

number = int(input("Number: "))

result = []

k = 2
while number > 1:
    if number % k == 0:
        result += [k]
        number /= k
    else:
        k += 1


print(result)

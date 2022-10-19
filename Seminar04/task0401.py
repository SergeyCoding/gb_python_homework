# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def find_factors(num):
    result = []
    k = 2
    while num > 1:
        if num % k == 0:
            result += [k]
            num /= k
        else:
            k += 1
    return result


print("Семинар 4. Задача 1")

number = int(input("Number: "))

print(find_factors(number))

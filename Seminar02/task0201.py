# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


print("Семинар 2. Задача 1")

number = int(input('Number: '))

result = [1]*number

for i in range(1, number):
    result[i] = result[i-1]*(i+1)

print(result)

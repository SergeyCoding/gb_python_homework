#!/usr/bin/python3
# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

print("Семинар 1. Задача 3")

num_quart = int(input('Четверть: '))

if(num_quart == 1):
    print('x > 0, y > 0')
elif(num_quart == 2):
    print('x < 0, y > 0')
elif(num_quart == 3):
    print('x < 0, y < 0')
elif(num_quart == 4):
    print('x > 0, y < 0')
else:
    print('Ошибка!')

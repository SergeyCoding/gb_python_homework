# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

print("Семинар 2. Задача 4")

number = int(input('Number: '))
shift = int(input('Shift: '))

lst = [*range(-number, number+1)]

print([*lst[len(lst)-shift:], *lst[:len(lst)-shift]])

""" homework 01 """

# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imprative(numbers):
    "sort list imprative"
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(i+1,len(numbers)):
            if num1>num2:
                numbers[i]=num2
                numbers[j]=num1
    return numbers



# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    "sort list declarative"
    return numbers.sort()

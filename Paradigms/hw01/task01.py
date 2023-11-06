# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

arr=[2,3,4,5,2,3,1,23]

print(arr)

def sort_list_imprative(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(i,j)
    pass
    return numbers

def sort_list_declarative(numbers):
    
    pass
    return numbers
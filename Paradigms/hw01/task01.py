# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imprative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
              k=numbers[i]
              numbers[i]=numbers[j]
              numbers[j]=k
    return numbers



# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return numbers.sort()

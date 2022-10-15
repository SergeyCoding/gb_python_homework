# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fibo_next(fibo_cash=[]):
    if len(fibo_cash) == 0:
        return [1]

    if len(fibo_cash) == 1:
        return [1, 1]

    return fibo_cash[-2:] + [fibo_cash[-1]+fibo_cash[-2]]


def save_fibo(file_name: str, n: int):
    f = open(file=file_name, mode='w', encoding='utf-8')

    fibo = fibo_next()
    for _ in range(n):
        f.write(f"{fibo[-1]} ")
        fibo = fibo_next(fibo)

    f.close


print("Семинар 3. Задача 1")

number = int(input('Number: '))

save_fibo("data0301.txt", number)

# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

print("Семинар 2. Задача 3")

str_first = input('first: ')
str_second = input('second: ')


def char_in_str_count(char, str):
    result = 0
    for c in str:
        if c == char:
            result = result+1
    return result


for c in str_first:
    print(f"{c} - {char_in_str_count(c, str_second)}, ", end='')

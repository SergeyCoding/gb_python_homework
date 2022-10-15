# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def fruit_filter(file_name: str, str_begin: str):
    str_begin = str_begin.capitalize()

    f = open(file_name, mode='r', encoding='utf-8')

    line = f.readline()
    while line != '':
        if line[0].capitalize() == str_begin:
            print(line.strip())
        line = f.readline()

    f.close()


print("Семинар 3. Задача 2")

letter = input('Letter: ')


fruit_filter("data0302.txt", letter)

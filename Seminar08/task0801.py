# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random


def generate_eval():
    return random.randint(1, 5)


def generate_group():
    return list(generate_eval() for _ in range(random.randint(20, 30)))


def generate_course(num: int):
    return list(generate_group() for _ in range(num))


def print_course(course: list):
    for group in course:
        print(group)


def avg_of_group(group: list):
    return sum(group)/len(group)


print("Семинар 8. Задача 1")

number = int(input("Введите количесвто групп: "))

if number < 1:
    print("Ошибка!!! Проверьте введенные данные")
    exit()

course = generate_course(number)
print("\nСписок групп:")
print_course(course)
print()

avg = list(avg_of_group(gr) for gr in course)
print("Средние баллы:")
print(avg)

print(f"\nЛучший бал у {1+avg.index(max(avg))}-ой группы")

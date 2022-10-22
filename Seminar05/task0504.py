# Задача 4*. Создайте игру в крестики-нолики.


import random


print("Семинар 5. Задача 4")

gg_fld = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
gg_eg = [""]


def global_field(g_fld=gg_fld):
    return g_fld


def global_end_game(g_end_game=gg_eg):
    return g_end_game


def check_line(line, ch):
    for (v, h) in line:
        if global_field()[v][h] != ch:
            return

    global_end_game()[0] = ch


def is_end_game():

    for v in range(3):
        check_line([(v, 0), (v, 1), (v, 2)], "X")
        check_line([(v, 0), (v, 1), (v, 2)], "O")

    for h in range(3):
        check_line([(0, h), (1, h), (2, h)], "X")
        check_line([(0, h), (1, h), (2, h)], "O")

    check_line([(0, 0), (1, 1), (2, 2)], "X")
    check_line([(0, 0), (1, 1), (2, 2)], "X")
    check_line([(2, 0), (1, 1), (0, 2)], "O")
    check_line([(2, 0), (1, 1), (0, 2)], "O")

    if global_end_game()[0] == "":
        if len(available_positions()) == 0:
            global_end_game()[0] = "XO"


def print_hint():
    for v in range(3):
        for h in range(3):
            print(f" {v}{h} ", end="")
        print()


def print_fld():
    for v in global_field():
        for h in v:
            print(f" {h} ", end="")
        print()


def available_positions():
    move = []
    for v in range(3):
        for h in range(3):
            if global_field()[v][h] == ".":
                move += [str(v) + str(h)]
    return move


print_hint()

while global_end_game()[0] == "":
    print_fld()

    move = available_positions()

    number = input(f"{move} X: ")

    if number not in move:
        print("неверный ход")
        print_hint()
        print()
        continue

    global_field()[int(number[0])][int(number[1])] = "X"

    is_end_game()

    if global_end_game()[0] == "":
        move = available_positions()

        move0 = move[random.randint(0, len(move) - 1)]

        global_field()[int(move0[0])][int(move0[1])] = "O"

        is_end_game()


print_fld()
print()
print(f"Выиграли: {global_end_game()[0]}")

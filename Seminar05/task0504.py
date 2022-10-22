# Задача 4*. Создайте игру в крестики-нолики.


import random


print("Семинар 5. Задача 4")

print("Вводим два числа:")

g_fld = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
g_end_game = ['']


def check_line(line, ch, end_game):
    for (v, h) in line:
        if g_fld[v][h] != ch:
            return

    end_game[0] = ch


def is_end_game(end_game):

    for v in range(3):
        check_line([(v, 0), (v, 1), (v, 2)], 'X', end_game)
        check_line([(v, 0), (v, 1), (v, 2)], 'O', end_game)

    for h in range(3):
        check_line([(0, h), (0, h), (0, h)], 'X', end_game)
        check_line([(0, h), (0, h), (0, h)], 'O', end_game)

    check_line([(0, 0), (1, 1), (2, 2)], 'X', end_game)
    check_line([(0, 0), (1, 1), (2, 2)], 'X', end_game)
    check_line([(2, 0), (1, 1), (0, 2)], 'O', end_game)
    check_line([(2, 0), (1, 1), (0, 2)], 'O', end_game)

    if end_game[0] == '':
        if len(available_positions()) == 0:
            end_game[0] = 'XO'


def print_fld():
    for v in g_fld:
        for h in v:
            print(f" {h} ", end='')
        print()


def available_positions():
    move = []
    for v in range(3):
        for h in range(3):
            if g_fld[v][h] == '.':
                move += [str(v)+str(h)]
    return move


while g_end_game[0] == '':
    print_fld()

    move = available_positions()

    number = input(f"{move} X: ")

    if number not in move:
        print('неверный ход')
        continue

    g_fld[int(number[0])][int(number[1])] = 'X'

    is_end_game(g_end_game)

    if g_end_game == '':
        move = available_positions()

        move0 = move[random.randint(0, len(move))]

        g_fld[int(move0[0])][int(move0[1])] = 'O'

        is_end_game(g_end_game)


print_fld(g_fld)
print()
print(f"Выиграли: {g_end_game[0]}")

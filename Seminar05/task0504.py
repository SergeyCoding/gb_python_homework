# Задача 4*. Создайте игру в крестики-нолики.


print("Семинар 5. Задача 4")

# number = int(input("Number: "))


def is_end_game():
    pass


def print_fld():
    fld = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    for v in fld:
        for h in v:
            print(h, end='')
        print()


print_fld()

from random import randint

game_in_process = False
secret_number = 0
counter = 0


def init():
    global secret_number
    global game_in_process
    global counter
    secret_number = randint(1, 1000)
    game_in_process = True
    counter = 0


def check(number: int):
    global game_in_process
    global counter
    counter += 1
    if number > secret_number:
        return "Ваше число больше"
    if number < secret_number:
        return "Ваше число меньше"
    game_in_process = False
    return f"Да, это число {secret_number}. Количество попыток: {counter}"

import model


def info(str):
    print(str)


def get_char():
    c = input("Ваша буква: ")
    return c


def get_yes_no():
    answer = ''

    while(len(answer) == 0 or (answer[0].lower() not in {'n', 'y', 'д', 'н'})):
        answer = input()

    return answer[0].lower() in {'y', 'д'}


def show_current_word():
    w = model.get_current_word_state()
    print(w)

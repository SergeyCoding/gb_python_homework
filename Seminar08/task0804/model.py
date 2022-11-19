question = ''
hidden_word = ''
knownChars = set()


def init():
    f = open('db/data.txt', 'a')
    f.close()

    set_question("Можно дать на кассе")
    set_word("\u043f\u044f\u0442\u0438\u0434\u0435\u0441\u044f\u0442\u0438\u0440\u0443\u0431\u043b\u0451\u0432\u043a\u0430")
    knownChars.clear()


def set_question(q):
    global question
    question = q


def get_question():
    return question


def set_word(w: str):
    global hidden_word
    hidden_word = w.upper()


def get_word():
    return hidden_word


def add_knownChars(c: str):
    knownChars.add(c)
    return knownChars


def get_knownChars():
    return knownChars


def get_current_word_state():
    w = get_word()
    unknown = set(get_word())-get_knownChars()
    for c in unknown:
        w = w.replace(c, '*')
    return w


def encrypt_word():
    pass


def decrypt_word():
    pass


def add_char(c: str):
    add_knownChars(c.capitalize())


def is_game_end():
    return get_current_word_state().find('*') == -1
